# -*- coding: utf-8 -*-
"""清洗器回归测试：锁定 P6 控制字符消毒（\x00 与 C0 控制符不进入输出）。"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from rsk.parser.litmind_parser.cleaner import clean, clean_with_captions  # noqa: E402

DIRTY = "Results body.\x00\nSecond line \x0bwith\x1c controls\x1f and \x0cformfeed.\r\n\nFigure 1. A caption\x00."


class TestControlCharSanitize(unittest.TestCase):
    """问题 P6：pymupdf 嵌入式字体映射残留的控制符必须被清除。"""

    def test_clean_removes_nul_and_c0(self):
        out = clean(DIRTY)
        self.assertNotIn("\x00", out)
        for ch in ("\x0b", "\x0c", "\x1c", "\x1f", "\x7f", "\r"):
            self.assertNotIn(ch, out)
        # 正文内容保留
        self.assertIn("Results body.", out)
        self.assertIn("Second line with controls and formfeed.", out)

    def test_captions_also_sanitized(self):
        result = clean_with_captions(DIRTY)
        self.assertNotIn("\x00", result["figure_captions"])
        self.assertIn("A caption", result["figure_captions"])
        self.assertNotIn("\x00", result["text"])

    def test_normal_text_unchanged(self):
        plain = "Normal paragraph.\n\nAnother sentence, 0.42 V at 10 mA.\n"
        self.assertEqual(clean(plain), "Normal paragraph.\n\nAnother sentence, 0.42 V at 10 mA.")

    def test_tab_preserved(self):
        out = clean("Value\t0.42\n")
        self.assertIn("\t", out)


if __name__ == "__main__":
    unittest.main()
