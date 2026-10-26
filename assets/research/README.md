# Research illustrations

Eight illustrations for the homepage's Research section. Molecular models are reused from verified source artwork or published paper panels: they are not generated or redrawn. SVG compositions preserve original source pixels with proportional scaling and viewports, retaining molecular geometry, connectivity, atom colors, and orbital artwork. The GPU figure embeds a lossless, exact pixel crop of Figure 9(a) to avoid downloading unused panels; its rendered output is pixel-identical to the full-source version. New arrows, matrices, computing symbols, and electronic-configuration diagrams are native SVG.

| Research topic | Illustration | Source |
| --- | --- | --- |
| Machine Learning for Electronic Structure | [machine-learning-sourced.svg](machine-learning-sourced.svg) | Verified methane model with a conceptual symmetric Hamiltonian matrix and feedback loop |
| Scientific Benchmarks for LLMs | [scientific-benchmarks-sourced.svg](scientific-benchmarks-sourced.svg) | Verified methane model with conceptual evidence and evaluation symbols |
| Agentic AI Workflows | [spectroscopy-sourced.svg](spectroscopy-sourced.svg) | Verified methane model with a computing and spectroscopy workflow |
| GPU-Accelerated Quantum Chemistry | [quantum-simulation-sourced.svg](quantum-simulation-sourced.svg) | Graphene and CO₂ panel from the real-space DFT review's Figure 9, with a separate GPU symbol |
| Real-Space Kohn–Sham DFT | [real-space-dft-sourced.svg](real-space-dft-sourced.svg) | Methane and grid panel from the real-space DFT review's graphical abstract |
| Quantum Monte Carlo | [quantum-monte-carlo-research-v1.png](quantum-monte-carlo-research-v1.png) | Original non-molecular conceptual illustration generated with the built-in ImageGen tool |
| Multireference Methods and Strongly Correlated Systems | [strong-correlation-schematic.svg](strong-correlation-schematic.svg) | Original two-configuration schematic with opposite-spin paired electrons |
| Excited-State Theory and Computational Spectroscopy | [excited-states-sourced.svg](excited-states-sourced.svg) | Molecular orbital and density panels from the ROKS-EDA graphical abstract |

## Source credits

- **Methane:** [Methane-CRC-MW-3D-balls.png](https://commons.wikimedia.org/wiki/File:Methane-CRC-MW-3D-balls.png), by Ben Mills (Benjah-bmm27), released into the public domain. The source cites microwave spectroscopy and the *CRC Handbook*, 88th edition. The full model has four C–H bonds in the original tetrahedral projection. The same unmodified source is used in the three AI for Science illustrations.
- **Real-space DFT:** *Real-space Kohn–Sham density functional theory for complex energy applications*, [DOI: 10.1039/D5CC01820J](https://doi.org/10.1039/D5CC01820J), graphical abstract and Figure 9(a), from the publisher's original high-resolution slide images. Crops select the original molecular panels; surrounding layout and GPU symbol are new. The small original “a)” marker is retained where removing it would overlap a carbon atom. See [publication figure provenance](../papers/sources.json) for the original figure sources and caption attribution.
- **Excited states:** *An Energy Decomposition Method for Electronic Excitations in Two-Determinant Restricted Open-Shell Kohn–Sham Theory*, [DOI: 10.1021/acs.jctc.5c01738](https://doi.org/10.1021/acs.jctc.5c01738), original graphical-abstract artwork extracted from the publisher PDF. Molecular and orbital pixels are unchanged.

[sources.json](sources.json) records source hashes, extraction bounds, composition methods, and asset hashes. [prompts.json](prompts.json) records the final prompt for the retained non-molecular QMC illustration. Earlier generated molecular drafts were rejected and are excluded from the website.

These are research-theme illustrations, not new calculated results. Matrices, arrows, spectra, and occupation diagrams are conceptual. The multireference diagram shows two paired configurations without assigning energies, coefficients, or relative phase; it is not a complete active-space expansion. The QMC image depicts electronic-state walkers and auxiliary-field propagation, not atom trajectories.

The SVG files contain both vector graphics and source raster panels; the original panels' resolution is retained. Desktop illustrations appear to the left of their text as static images, without links or click-to-enlarge behavior. Narrow screens stack the image above the text. Edit each topic's `image` object in `data/profile.json` to select a different asset or alternative text.
