# AI Agent Instructions: Computational Alchemy Framework

## Project Overview

This is a scientific research project exploring **atomic impedance** as a unifying principle for chemistry. The framework derives a single impedance value from atomic properties (ionization energy, electronegativity, radius) to predict chemical bonding, metal toxicity, and biological interactions.

**Core thesis:** Elements organize into three categories by impedance—GIVERS (electron donors), TAKERS (electron acceptors), and BRIDGES (catalysts/transformers). The seven classical "planetary metals" cluster statistically in the Bridge category (p=0.00005).

## Key Files

- [element_framework.py](element_framework.py) — Complete Python implementation with atomic data, impedance calculations, frequency analysis, and interactive CLI
- [COMPUTATIONAL_ALCHEMY_PAPER.md](COMPUTATIONAL_ALCHEMY_PAPER.md) — Research paper documenting theory, statistical validation, applications (lithium therapy, heavy metal toxicity)

## Core Concepts

### Impedance Formula
```python
Z_atom = sqrt(E_ionization × electronegativity) / atomic_radius
```
Physical interpretation: Balance between electron-holding forces (numerator) normalized by spatial extent (denominator).

### Three Categories (Emergent from Data)
- **GIVERS** (Z < 2): Na, K, Ca, Mg — electron donors, s-block
- **BRIDGES** (2 ≤ Z ≤ 4): Fe, Cu, Zn, Au, Ag — catalysts, d-block, planetary metals
- **TAKERS** (Z > 4): O, N, Cl, F — electron acceptors, p-block

### Impedance Matching Between Elements
```python
R = (4 × Z1 × Z2) / (Z1 + Z2)²
```
Predicts bond types: R ≈ 1.0 (metallic/alloys), 0.5–0.9 (covalent), <0.5 (ionic)

## Code Architecture

### Data Structures
- `ELEMENT_DATA`: Dict of 46 elements with atomic properties (NIST data)
- `PLANETARY_METALS`: The seven alchemical metals with planetary correspondences
- `ElementProfile`: Dataclass containing raw properties + framework-derived values (impedance, frequencies, consciousness affinity)

### Core Functions
1. `calculate_atomic_impedance()` — Computes Z from ionization/χ/radius
2. `calculate_frequencies()` — Three channels: quantum (E/h), acoustic (M^(-1/3)), chemical (bond energy proxy)
3. `analyze_element()` — Generates complete ElementProfile
4. `calculate_impedance_match()` — Predicts bonding between two elements
5. `predict_compound_frequency()` — Mass-weighted acoustic properties of compounds

### Interactive CLI
Run without args for demo, or pass element symbol: `python element_framework.py Zn`
Interactive mode has 7 options including comparison tables, impedance matching, compound prediction.

## Scientific Context

### Key Results Validated
- **Bond prediction**: 82.6% accuracy (beats electronegativity difference Δχ at 73.9%)
- **Planetary metal clustering**: p=5×10⁻⁵ via 100k Monte Carlo simulations
- **Lithium-sodium match**: R=0.992 (explains Na⁺ channel permeation in bipolar treatment)
- **Heavy metal toxicity**: Pb/Hg impedances near Cu (substitution mechanism)

### Limitations (Document These)
- **Does NOT explain** reactive toxicity (As, Se) — requires additional redox chemistry
- **40 Hz consciousness link weakened** — initial claims revised in paper
- **Cannot predict which Bridge elements became essential** — evolution + bioavailability matter

### Connection to Broader Framework
Extends "Channel-Energy Selection Framework" (consciousness studies) — impedance matching principle across scales from atoms to neural oscillations.

## Development Conventions

### When Adding Elements
1. Add data to `ELEMENT_DATA` dict with format: `(Z, mass, E_ion, χ, radius, electron_config)`
2. Update `ELEMENT_NAMES` dict
3. For alchemically significant metals, add to `PLANETARY_METALS`

### When Modifying Impedance Calculation
- **Preserve dimensional consistency**: Z must yield eV/length units
- **Maintain symmetry**: IE and χ should contribute equally (multiplicative, not additive)
- **Test against 23-compound validation set** documented in paper
- Noble gases (χ=None) use simplified formula: Z = E_ion / r

### Physical Constants Location
Top of file: `H_PLANCK`, `C_LIGHT`, `PHI` (golden ratio), `AMU_TO_KG`

### Frequency Calculations
Three channels scale differently:
- **Quantum**: f = E_ion/h (PHz range, electronic transitions)
- **Acoustic**: f ∝ M^(-1/3) (THz range, mass-dependent vibrations)
- **Chemical**: f ≈ 0.3×E_ion/h (bond energy proxy)

### Consciousness Affinity Calculation
Looks for harmonic relationships (subharmonics of atomic frequencies matching brain wave bands: delta/theta/alpha/beta/gamma). Moderate impedance (Z≈3) weighted higher for biological relevance.

## Testing & Validation

### No automated tests currently exist — opportunities for contribution:
1. **Unit tests** for impedance formula edge cases (noble gases, extreme radii)
2. **Regression tests** on 23-compound bond prediction set
3. **Monte Carlo reproducibility** of planetary metal p-value
4. **Frequency calculation validation** against known spectroscopic data

### Manual validation workflow:
```python
# Verify known patterns
Na = analyze_element('Na')  # Should be GIVER (Z=1.15)
Fe = analyze_element('Fe')  # Should be BRIDGE (Z=2.44)
O = analyze_element('O')    # Should be TAKER (Z=9.38)

# Check impedance match
R, _ = calculate_impedance_match('Cu', 'Zn')  # Should be ~1.0 (brass alloy)
```

## Common Tasks

### Analyzing New Elements
If adding heavier elements (lanthanides, actinides), ensure NIST data sources are current. Electronegativity data sparse for f-block.

### Modifying Output Formats
- `print_element_profile()` — Single element, detailed
- `print_comparison_table()` — Multiple elements, tabular
- `print_planetary_metals()` — Seven alchemical metals only

### Impedance Matching for Biological Systems
When analyzing ion substitution (e.g., drug design), focus on Z-ratio near 1.0 AND similar atomic radii. Impedance alone insufficient — spatial size matters for binding sites.

## Scientific Rigor Guidelines

### Claims to Support with Evidence
- "Impedance predicts bonding" → Cite 82.6% accuracy, compare to Δχ
- "Planetary metals cluster" → State p=5×10⁻⁵, 100k trials
- "Li mimics Na" → R=0.992, best of all biological ion pairs

### Claims to Avoid or Qualify
- ❌ "Impedance explains all toxicity" → Only substitution mimicry, not reactive
- ❌ "Elements resonate at consciousness frequencies" → Revised, harmonics only
- ✓ "Framework suggests mechanism" → Not "proves"

### When Uncertain
State limitations explicitly. The paper's honest limitations section (4.1-4.2) is a strength, not weakness.

## Paper Synchronization

Changes to code formulas must update paper equations. Key sections:
- **Section 2.1**: Impedance formula definition
- **Section 2.4**: Matching formula R = 4Z₁Z₂/(Z₁+Z₂)²
- **Section 3.1**: Bond prediction accuracy results
- **Appendix A**: Complete element table (auto-generate from code)

## Future Directions

Opportunities for extension:
1. Multi-element compounds (beyond binary impedance matching)
2. Integration with quantum chemistry codes (DFT, wavefunction overlap)
3. Machine learning on impedance features for property prediction
4. Experimental validation: tin-copper substitution prediction
5. Biological pathway analysis using cofactor impedance networks

---

**Philosophy**: This framework connects ancient metallurgical wisdom to modern atomic physics. Maintain scientific rigor while respecting the empirical insights that identified these patterns millennia before we had equations to describe them.
