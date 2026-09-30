# -*- coding: utf-8 -*-
"""章节识别器回归测试：锁定 ACS/Nature 全大写标题、行内 ABSTRACT:、
首行正文 off-by-one、EXPERIMENTAL SECTION/REFERENCES AND NOTES 四类修复。"""

import sys
import unittest
from pathlib import Path

# 使 `from rsk.parser...` 可从插件根导入（测试运行于插件根目录）
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from rsk.parser.litmind_parser.sectionizer import sectionize  # noqa: E402


ACS_TEXT = """ABSTRACT
We study the adsorption of water on Pt(111) surfaces.
The second sentence of the abstract follows.

INTRODUCTION
Water-metal interfaces play a key role in electrocatalysis.
More introduction text here.

EXPERIMENTAL SECTION
All calculations were performed with VASP.
More methods text.

RESULTS AND DISCUSSION
The computed overpotential is 0.42 V.
More results text.

REFERENCES AND NOTES
(1) Smith, J.; Jones, K. J. Am. Chem. Soc. 2020.
"""

NATURE_TEXT = """Catalytic Activity of Single-Atom Catalysts

Hu, W.^1^, Wang, L.^1^
^1^Department of Chemistry, Example University

Single-atom catalysts (SACs) offer maximal atom efficiency. Here we report a series of M-N-C catalysts with tunable activity for the oxygen reduction reaction.

The sluggish kinetics of the oxygen reduction reaction limit fuel cell performance. Recent studies have shown that nitrogen-coordinated metal sites are the active centers.

RESULTS
The Fe-N-C catalyst achieved a half-wave potential of 0.85 V. The Pt-N-C analogue reached 0.88 V.

Methods
All catalysts were synthesized by pyrolysis at 900 C.

References
1. Jones, A. et al. J. Am. Chem. Soc. 2020.
"""


class TestCaseInsensitiveHeadings(unittest.TestCase):
    """问题 1：全大写标题（ACS/Nature 格式）必须被识别，不流入上一节。"""

    def test_all_caps_standalone_sections(self):
        s = sectionize(ACS_TEXT)
        self.assertIn("Water-metal interfaces", s.introduction)
        self.assertIn("All calculations were performed", s.methods)
        self.assertIn("computed overpotential", s.results)
        self.assertIn("J. Am. Chem. Soc", s.references)
        # 摘要不得吞掉后续章节正文
        self.assertNotIn("Water-metal interfaces", s.abstract)

    def test_all_caps_heading_not_in_other(self):
        s = sectionize(ACS_TEXT)
        for heading in ("ABSTRACT", "INTRODUCTION", "EXPERIMENTAL SECTION",
                        "RESULTS AND DISCUSSION", "REFERENCES AND NOTES"):
            self.assertNotIn(heading, s.other)

    def test_title_case_still_works(self):
        s = sectionize("Introduction\nBody line about catalysts.\n")
        self.assertEqual(s.introduction, "Body line about catalysts.")


class TestInlineAbstract(unittest.TestCase):
    """问题 2：行内摘要支持 "ABSTRACT: ..."（ACS 格式），前缀被剥离。"""

    def test_inline_acs_colon(self):
        s = sectionize("ABSTRACT: We study water adsorption on Pt(111).\nSecond line.")
        self.assertEqual(s.abstract, "We study water adsorption on Pt(111).\nSecond line.")

    def test_inline_dot(self):
        s = sectionize("Abstract. We report a new descriptor.\nSecond line.")
        self.assertEqual(s.abstract, "We report a new descriptor.\nSecond line.")


class TestFirstBodyLinePreserved(unittest.TestCase):
    """问题 3：独立标题后第一行正文不得丢失（off-by-one 修复）。"""

    def test_first_sentence_kept(self):
        s = sectionize(ACS_TEXT)
        self.assertTrue(s.abstract.startswith("We study the adsorption of water"))

    def test_heading_line_excluded_from_content(self):
        s = sectionize(ACS_TEXT)
        for content in (s.abstract, s.introduction, s.methods, s.results):
            self.assertNotIn("\nINTRODUCTION", content)
            self.assertNotIn("\nEXPERIMENTAL SECTION", content)


class TestAcsSectionPatterns(unittest.TestCase):
    """问题 4：EXPERIMENTAL SECTION → methods；REFERENCES AND NOTES → references。"""

    def test_experimental_section_goes_to_methods(self):
        s = sectionize("EXPERIMENTAL SECTION\nUsed VASP 6.3.\n")
        self.assertIn("Used VASP 6.3", s.methods)

    def test_references_and_notes(self):
        s = sectionize("REFERENCES AND NOTES\n(1) Doe, J.\n")
        self.assertIn("Doe", s.references)

    def test_standard_references_still_works(self):
        s = sectionize("References\n(1) Doe, J.\n")
        self.assertIn("Doe", s.references)


class TestUnlabeledLayoutBackfill(unittest.TestCase):
    """问题 P4：Nature/NC 无标题布局——摘要/引言从首章节前的块回填，
    标题/作者/单位留在 other；结构不足或无数达标长段时放弃回填。"""

    def test_nature_backfill(self):
        s = sectionize(NATURE_TEXT)
        self.assertTrue(s.abstract.startswith("Single-atom catalysts (SACs) offer"))
        self.assertIn("The sluggish kinetics of the oxygen reduction reaction", s.introduction)
        # 标题与作者留在 other，不混入摘要
        self.assertIn("Catalytic Activity of Single-Atom Catalysts", s.other)
        self.assertIn("Hu, W.", s.other)
        self.assertNotIn("Hu, W.", s.abstract)

    def test_no_backfill_without_structure(self):
        # 仅 1 个章节边界（References）→ 结构不清，不回填
        text = (
            "Title Line\n\nAuthor Line\n\nA long paragraph with two sentences. "
            "It discusses something important enough to be fairly long indeed.\n\n"
            "References\n(1) Doe, J.\n"
        )
        s = sectionize(text)
        self.assertEqual(s.abstract, "")
        self.assertEqual(s.introduction, "")
        self.assertIn("Title Line", s.other)

    def test_no_backfill_without_long_paragraph(self):
        # 有 2 个边界但首块无达标长段（纯短行）→ 放弃回填
        text = (
            "Title Line\n\nAuthor Line\n\nAffiliation Line\n\n"
            "RESULTS\nSome result text here.\n\nMethods\nSome methods text.\n"
        )
        s = sectionize(text)
        self.assertEqual(s.abstract, "")
        self.assertEqual(s.introduction, "")
        self.assertIn("Title Line", s.other)

    def test_regular_papers_unaffected(self):
        # 有 Abstract/Introduction 标题的常规论文不触发回填
        s = sectionize(ACS_TEXT)
        self.assertTrue(s.abstract.startswith("We study the adsorption"))


class TestChineseSections(unittest.TestCase):
    """中文模式回归：不受 re.I 改造影响。"""

    def test_cn_sections(self):
        s = sectionize("摘 要\n本文研究水吸附。\n引 言\n背景介绍。\n")
        self.assertIn("本文研究水吸附", s.abstract)
        self.assertIn("背景介绍", s.introduction)


if __name__ == "__main__":
    unittest.main()
