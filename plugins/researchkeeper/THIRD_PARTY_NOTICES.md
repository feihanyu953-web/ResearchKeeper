# Third-party notices

ResearchKeeper source code is MIT and original explanatory/knowledge content is CC BY 4.0. Neither license relicenses a dependency, downloaded model, paper content, or other third-party material. Installers obtain dependencies from upstream package sources; users must comply with the applicable upstream terms.

## Direct runtime dependencies

These are the direct runtime dependencies declared by this release. The links are upstream project or license references; transitive dependencies are governed by their own upstream notices.

| Dependency | Upstream license status | Upstream reference |
|---|---|---|
| NumPy | BSD 3-Clause | https://github.com/numpy/numpy/blob/main/LICENSE.txt |
| sentence-transformers | Apache-2.0 | https://github.com/huggingface/sentence-transformers/blob/master/LICENSE |
| huggingface-hub | Apache-2.0 | https://github.com/huggingface/huggingface_hub/blob/main/LICENSE |
| PyTorch | BSD-style; review upstream LICENSE and bundled notices | https://github.com/pytorch/pytorch/blob/main/LICENSE |
| PyYAML | MIT | https://github.com/yaml/pyyaml/blob/main/LICENSE |
| platformdirs | MIT | https://github.com/tox-dev/platformdirs/blob/main/LICENSE |
| ModelScope | Apache-2.0 | https://github.com/modelscope/modelscope/blob/master/LICENSE |
| PyMuPDF | Dual-licensed: GNU AGPL v3.0 or a commercial license from Artifex | https://pymupdf.readthedocs.io/en/latest/about.html |

The installed wheel/lockfile version, optional extras, and platform-specific PyTorch distribution can introduce additional notices. Consult installed package metadata and upstream terms before redistribution. For PyMuPDF, review AGPL v3.0 obligations for the intended use; where AGPL is unsuitable, obtain applicable commercial terms from Artifex. This is a licensing notice, not legal advice.

## BAAI/bge-m3 model

ResearchKeeper can download the `BAAI/bge-m3` embedding model during an explicitly confirmed setup. Attribution: Beijing Academy of Artificial Intelligence (BAAI), BGE-M3. The model card declares an MIT license.

- Model card and license label: https://huggingface.co/BAAI/bge-m3
- Associated BGE code project: https://github.com/FlagOpen/FlagEmbedding
- Citation: Chen et al., *BGE M3-Embedding: Multi-Lingual, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation*, arXiv:2402.03216.

The model remains BAAI-provided third-party material. It is downloaded to a user cache and is not redistributed or relicensed by ResearchKeeper. Verify the model card and any revision-specific files before reuse or redistribution.
