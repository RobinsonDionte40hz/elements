# Computational Alchemy: Atomic Impedance Framework

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Why do seven specific metals—gold, silver, mercury, copper, iron, tin, and lead—appear across civilizations as objects of profound significance?**

This framework provides a mathematical answer: **atomic impedance**—a single value derived from ionization energy, electronegativity, and atomic radius that predicts chemical bonding, biological interactions, and explains ancient metallurgical patterns.

**Key Finding:** The seven classical "planetary metals" cluster with extreme statistical significance (p = 0.00005), identifying them as "Bridge" elements capable of electron transformation.

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/RobinsonDionte40hz/elements.git
cd elements

# Install dependencies
pip install numpy

# Run interactive demo
python element_framework.py

# Analyze specific element
python element_framework.py Zn
```

## Core Formula

```python
Z_atom = √(E_ionization × electronegativity) / atomic_radius
```

**Physical meaning:** Balance between electron-holding forces (numerator) normalized by spatial extent (denominator).

## Three Categories

| Category | Z Range | Role | Examples |
|----------|---------|------|----------|
| **GIVERS** | Z < 2 | Electron donors | Na, K, Ca, Mg |
| **BRIDGES** | 2 ≤ Z ≤ 4 | Catalysts, transformers | Fe, Cu, Zn, Au, Ag |
| **TAKERS** | Z > 4 | Electron acceptors | O, N, Cl, F |

## Key Results

- ✅ **82.6% accuracy** predicting chemical bonds (beats electronegativity difference: 73.9%)
- ✅ **p = 0.00005** for planetary metal clustering (100,000 Monte Carlo trials)
- ✅ **Li-Na match (R = 0.992)** explains lithium therapy for bipolar disorder
- ✅ **Heavy metal toxicity** via impedance mimicry (Pb/Hg substitute for Cu)

## Usage Examples

### Analyze Single Element
```python
from element_framework import analyze_element

zinc = analyze_element('Zn')
print(f"Impedance: {zinc.impedance:.3f}")
print(f"Category: BRIDGE")
print(f"Consciousness affinity: {zinc.consciousness_affinity:.3f}")
```

### Compare Multiple Elements
```python
from element_framework import print_comparison_table

# Biological ions
print_comparison_table(['Na', 'K', 'Ca', 'Mg', 'Zn', 'Fe', 'Cu'])
```

### Predict Bond Type
```python
from element_framework import calculate_impedance_match

R, interpretation = calculate_impedance_match('Cu', 'Zn')
print(f"Cu-Zn match: {R:.3f}")  # Output: ~1.0 (brass alloy)
```

### Compound Analysis
```python
from element_framework import predict_compound_frequency

result = predict_compound_frequency(['Na', 'Cl'])
print(result['stability_prediction'])  # Output: Stable
```

## Interactive Mode

Run without arguments for interactive menu:

```
ELEMENT FRAMEWORK ANALYZER

OPTIONS:
1. Analyze single element
2. Compare multiple elements
3. Check impedance match between two elements
4. Predict compound properties
5. View planetary metals
6. Find high consciousness-affinity elements
7. Exit
```

## Scientific Validation

**Tested against 23 well-characterized compounds:**
- Ionic bonds: Z-ratio = 4.74–8.52
- Covalent bonds: Z-ratio = 1.00–2.06
- Metallic bonds: Z-ratio = 1.01–1.20

**Outperforms electronegativity difference** on hydrogen compounds (C-H, S-H, P-H) where spatial concentration of forces matters more than raw electronegativity values.

## The Planetary Metal Discovery

The seven alchemical metals cluster tightly in impedance:

| Metal | Planet | Z Value | Range |
|-------|--------|---------|-------|
| Gold | Sun | 2.78 | |
| Silver | Moon | 2.32 | **Width:** |
| Mercury | Mercury | 2.67 | **0.465** |
| Copper | Venus | 2.64 | |
| Iron | Mars | 2.44 | |
| Tin | Jupiter | 2.62 | |
| Lead | Saturn | 2.70 | |

**Statistical test:** Random selection of 7 metals from 35 candidates yields this tight clustering only 5 times in 100,000 trials.

**Why this matters:** Ancient metallurgists empirically identified the "Bridge" category—elements with variable oxidation states, alloy-forming ability, and catalytic properties—without the mathematics to explain what they observed.

## Applications

### Drug Design
**Lithium therapy:** R(Li, Na) = 0.992 explains why Li⁺ permeates Na⁺ channels, modulating neural excitability in bipolar disorder.

### Toxicology
**Heavy metal poisoning:** Pb (Z=2.70) and Hg (Z=2.67) sit near Cu (Z=2.64), substituting at enzyme binding sites but unable to perform catalytic functions.

### Materials Science
**Alloy prediction:** Perfect impedance matches (R ≈ 1.0) predict stable alloys:
- Cu-Zn (brass): R = 0.999
- Cu-Sn (bronze): R = 1.000
- Pb-Sn (solder): R = 1.000

## Files

- **[element_framework.py](element_framework.py)** — Complete implementation (640 lines)
- **[COMPUTATIONAL_ALCHEMY_PAPER.md](COMPUTATIONAL_ALCHEMY_PAPER.md)** — Full research paper with statistical validation
- **[.github/copilot-instructions.md](.github/copilot-instructions.md)** — AI agent development guide

## Data Sources

- **NIST Atomic Spectra Database** — Ionization energies
- **CRC Handbook of Chemistry and Physics** — Electronegativity, atomic radii
- **46 elements** included (H-Kr + key heavy elements: Rb, Sr, Ag, Sn, I, Cs, Ba, Au, Hg, Pb, U)

## Requirements

- Python 3.8+
- numpy

```bash
pip install numpy
```

## Limitations

**Honestly documented in the paper (Section 4):**

1. ❌ **Does NOT explain reactive toxicity** (As, Se) — requires redox chemistry
2. ⚠️ **40 Hz consciousness link weakened** — initial claims revised
3. ⚠️ **Cannot predict which Bridge elements became essential** — evolution matters

**The framework predicts mechanisms, not all outcomes.** Impedance explains substitution toxicity but not reactive toxicity. It identifies cofactor candidates but not evolutionary choices.

## Connection to Broader Framework

Extends the **Channel-Energy Selection Framework** demonstrating that impedance matching governs interactions from quantum exchanges to conscious experience. Same principle, different scales.

## Citation

```bibtex
@article{robinson2026alchemy,
  title={Computational Alchemy: Atomic Impedance as a Unifying Principle for Chemical Behavior},
  author={Robinson, Dionte},
  year={2026},
  url={https://github.com/RobinsonDionte40hz/elements}
}
```

## Contributing

This is research code prioritizing reproducibility over architecture. Contributions welcome:

- Add more elements (lanthanides, actinides)
- Implement automated testing (23-compound validation set)
- Extend to multi-element compounds
- Integrate with quantum chemistry codes (DFT, wavefunction overlap)
- Experimental validation of predictions

See [.github/copilot-instructions.md](.github/copilot-instructions.md) for development guidelines.

## License

MIT License - See [LICENSE](LICENSE) for details.

## Author

**Dionte Robinson**  
Date: January 15-16, 2026

---

*"The alchemists were observing real patterns. We now understand what they saw: elements organize by impedance, and those in the Bridge category—capable of transformation without permanent commitment—are the metals that shaped human civilization."*
