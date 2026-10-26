# Research illustrations

Eight research-theme illustrations for the homepage. All compositions are original diagrams; none of the current Research images reuses a paper figure. Molecular models come from verified public-domain reference artwork and retain their original PNG pixels and geometry. Grids, density envelopes, energy levels, spectral curves, arrows, matrices and computing symbols are newly drawn SVG elements.

| Research topic | Illustration | Source |
| --- | --- | --- |
| Machine Learning for Electronic Structure | [machine-learning-sourced.svg](machine-learning-sourced.svg) | Verified methane model with a conceptual symmetric Hamiltonian matrix and feedback loop |
| Scientific Benchmarks for LLMs | [scientific-benchmarks-sourced.svg](scientific-benchmarks-sourced.svg) | Verified methane model with conceptual evidence and evaluation symbols |
| Agentic AI Workflows | [spectroscopy-sourced.svg](spectroscopy-sourced.svg) | Verified methane model with a computing and spectroscopy workflow |
| GPU-Accelerated Quantum Chemistry | [quantum-simulation-original-v2.svg](quantum-simulation-original-v2.svg) | Verified CO₂ model above three GPUs in a new parallel-computation diagram |
| Real-Space Kohn–Sham DFT | [real-space-dft-original-v2.svg](real-space-dft-original-v2.svg) | Verified water model inside a newly drawn regular three-dimensional grid and qualitative density envelope |
| Quantum Monte Carlo | [quantum-monte-carlo-research-v1.png](quantum-monte-carlo-research-v1.png) | Original non-molecular conceptual illustration generated with the built-in ImageGen tool |
| Multireference Methods and Strongly Correlated Systems | [strong-correlation-schematic.svg](strong-correlation-schematic.svg) | Original two-configuration schematic with opposite-spin paired electrons |
| Excited-State Theory and Computational Spectroscopy | [excited-states-original-v2.svg](excited-states-original-v2.svg) | Original electronic-transition diagram and corresponding schematic absorption peaks |

## Source credits

- **Methane:** [Methane-CRC-MW-3D-balls.png](https://commons.wikimedia.org/wiki/File:Methane-CRC-MW-3D-balls.png), by Ben Mills (Benjah-bmm27), released into the public domain. The source cites microwave spectroscopy and the *CRC Handbook*, 88th edition. The full model has four C–H bonds in the original tetrahedral projection. The same unmodified source is used in the three AI for Science illustrations.

- **Water and CO₂:** [Water-3D-balls.png](https://commons.wikimedia.org/wiki/File:Water-3D-balls.png) and [Carbon-dioxide-3D-balls.png](https://commons.wikimedia.org/wiki/File:Carbon-dioxide-3D-balls.png), by Ben Mills (Benjah-bmm27), released into the public domain. Water has two O–H single bonds; the linear CO₂ model explicitly shows two C=O double bonds. Each original PNG is embedded unchanged, with proportional scaling only.
- **Grid concept:** The new real-space diagram follows the representation of wavefunctions, densities and potentials on regular grids described in the [Octopus grid documentation](https://www.octopus-code.org/documentation/main/developers/code_documentation/grids/). The diagram is newly drawn; no documentation image is copied.
- **Spectroscopy concept:** The new diagram connects many-electron excitation energies with qualitative broadened absorption bands, consistent with the [ORCA spectrum-plotting documentation](https://www.faccts.de/docs/orca/6.1/manual/contents/utilitiesvisualization/utilities.html#orca-mapspc). Larger excitation energy corresponds to a peak farther right on an energy axis. No documentation or paper image is copied.

[sources.json](sources.json) records source hashes, geometry checks, conceptual references, composition methods, and asset hashes. [prompts.json](prompts.json) records the final prompt for the retained non-molecular QMC illustration. Earlier generated molecular drafts and paper-panel Research compositions were retired; neither is used by the current Research section.

These are research-theme illustrations, not new calculated results. Matrices, arrows, spectra, density envelopes, and occupation diagrams are conceptual. The water-density envelope is not a computed density or a signed orbital. The excitation diagram represents many-electron states, not Kohn–Sham orbital energies; its spectral widths and heights are illustrative. The multireference diagram shows two paired configurations without assigning energies, coefficients, or relative phase; it is not a complete active-space expansion. The QMC image depicts electronic-state walkers and auxiliary-field propagation, not atom trajectories.

The SVG files contain both vector graphics and source raster panels; the original panels' resolution is retained. Desktop illustrations appear to the left of their text as static images, without links or click-to-enlarge behavior. Narrow screens stack the image above the text. Edit each topic's `image` object in `data/profile.json` to select a different asset or alternative text.
