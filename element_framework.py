#!/usr/bin/env python3
"""
ELEMENT FRAMEWORK - Computational Alchemy Through Impedance
===========================================================

Derive elemental properties from first principles:
- Atomic impedance from ionization energy, radius, electronegativity
- Three channel frequencies (quantum, acoustic, chemical)
- Impedance matching between elements
- Consciousness resonance identification

NO biological assumptions - pure atomic physics.

Z_atom = √(E_ionization × χ) / r

Where:
- E_ionization = First ionization energy (resistance to electron loss)
- χ = Electronegativity (field strength / electron affinity)
- r = Atomic radius (spatial extent)

Author: Dionte Robinson
Date: January 15, 2026
"""

import numpy as np
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
from enum import Enum
import sys

# =============================================================================
# PHYSICAL CONSTANTS
# =============================================================================

H_PLANCK = 6.62607e-34      # Planck constant (J·s)
H_PLANCK_EV = 4.135667e-15  # Planck constant (eV·s)
C_LIGHT = 299792458         # Speed of light (m/s)
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio
AMU_TO_KG = 1.66054e-27     # Atomic mass unit to kg

# =============================================================================
# ELEMENT DATA - First 36 Elements + Key Heavy Elements
# Data from NIST and CRC Handbook
# =============================================================================

# Format: Symbol -> (atomic_number, atomic_mass_amu, ionization_energy_eV, 
#                    electronegativity_pauling, atomic_radius_pm, electron_config)

ELEMENT_DATA = {
    # Period 1
    'H':  (1, 1.008, 13.598, 2.20, 53, '1s1'),
    'He': (2, 4.003, 24.587, None, 31, '1s2'),  # Noble gas - no electronegativity
    
    # Period 2
    'Li': (3, 6.941, 5.392, 0.98, 167, '[He]2s1'),
    'Be': (4, 9.012, 9.323, 1.57, 112, '[He]2s2'),
    'B':  (5, 10.81, 8.298, 2.04, 87, '[He]2s2 2p1'),
    'C':  (6, 12.01, 11.260, 2.55, 77, '[He]2s2 2p2'),
    'N':  (7, 14.01, 14.534, 3.04, 75, '[He]2s2 2p3'),
    'O':  (8, 16.00, 13.618, 3.44, 73, '[He]2s2 2p4'),
    'F':  (9, 19.00, 17.423, 3.98, 71, '[He]2s2 2p5'),
    'Ne': (10, 20.18, 21.565, None, 69, '[He]2s2 2p6'),
    
    # Period 3
    'Na': (11, 22.99, 5.139, 0.93, 190, '[Ne]3s1'),
    'Mg': (12, 24.31, 7.646, 1.31, 160, '[Ne]3s2'),
    'Al': (13, 26.98, 5.986, 1.61, 143, '[Ne]3s2 3p1'),
    'Si': (14, 28.09, 8.152, 1.90, 118, '[Ne]3s2 3p2'),
    'P':  (15, 30.97, 10.487, 2.19, 110, '[Ne]3s2 3p3'),
    'S':  (16, 32.07, 10.360, 2.58, 103, '[Ne]3s2 3p4'),
    'Cl': (17, 35.45, 12.968, 3.16, 99, '[Ne]3s2 3p5'),
    'Ar': (18, 39.95, 15.760, None, 97, '[Ne]3s2 3p6'),
    
    # Period 4
    'K':  (19, 39.10, 4.341, 0.82, 243, '[Ar]4s1'),
    'Ca': (20, 40.08, 6.113, 1.00, 194, '[Ar]4s2'),
    'Sc': (21, 44.96, 6.561, 1.36, 184, '[Ar]3d1 4s2'),
    'Ti': (22, 47.87, 6.828, 1.54, 176, '[Ar]3d2 4s2'),
    'V':  (23, 50.94, 6.746, 1.63, 171, '[Ar]3d3 4s2'),
    'Cr': (24, 52.00, 6.767, 1.66, 166, '[Ar]3d5 4s1'),
    'Mn': (25, 54.94, 7.434, 1.55, 161, '[Ar]3d5 4s2'),
    'Fe': (26, 55.85, 7.902, 1.83, 156, '[Ar]3d6 4s2'),
    'Co': (27, 58.93, 7.881, 1.88, 152, '[Ar]3d7 4s2'),
    'Ni': (28, 58.69, 7.640, 1.91, 149, '[Ar]3d8 4s2'),
    'Cu': (29, 63.55, 7.726, 1.90, 145, '[Ar]3d10 4s1'),
    'Zn': (30, 65.38, 9.394, 1.65, 142, '[Ar]3d10 4s2'),
    'Ga': (31, 69.72, 5.999, 1.81, 136, '[Ar]3d10 4s2 4p1'),
    'Ge': (32, 72.63, 7.900, 2.01, 125, '[Ar]3d10 4s2 4p2'),
    'As': (33, 74.92, 9.815, 2.18, 114, '[Ar]3d10 4s2 4p3'),
    'Se': (34, 78.97, 9.752, 2.55, 103, '[Ar]3d10 4s2 4p4'),
    'Br': (35, 79.90, 11.814, 2.96, 94, '[Ar]3d10 4s2 4p5'),
    'Kr': (36, 83.80, 14.000, None, 88, '[Ar]3d10 4s2 4p6'),
    
    # Key heavier elements (alchemical metals, consciousness-relevant)
    'Rb': (37, 85.47, 4.177, 0.82, 265, '[Kr]5s1'),
    'Sr': (38, 87.62, 5.695, 0.95, 219, '[Kr]5s2'),
    'Ag': (47, 107.87, 7.576, 1.93, 165, '[Kr]4d10 5s1'),  # Silver - Moon
    'Sn': (50, 118.71, 7.344, 1.96, 145, '[Kr]4d10 5s2 5p2'),  # Tin - Jupiter
    'I':  (53, 126.90, 10.451, 2.66, 133, '[Kr]4d10 5s2 5p5'),
    'Cs': (55, 132.91, 3.894, 0.79, 298, '[Xe]6s1'),
    'Ba': (56, 137.33, 5.212, 0.89, 253, '[Xe]6s2'),
    'Au': (79, 196.97, 9.226, 2.54, 174, '[Xe]4f14 5d10 6s1'),  # Gold - Sun
    'Hg': (80, 200.59, 10.438, 2.00, 171, '[Xe]4f14 5d10 6s2'),  # Mercury - Mercury
    'Pb': (82, 207.2, 7.417, 2.33, 154, '[Xe]4f14 5d10 6s2 6p2'),  # Lead - Saturn
    'U':  (92, 238.03, 6.194, 1.38, 196, '[Rn]5f3 6d1 7s2'),
}

# Alchemical planetary correspondences
PLANETARY_METALS = {
    'Au': {'planet': 'Sun', 'symbol': '☉', 'day': 'Sunday', 'quality': 'Perfection, illumination'},
    'Ag': {'planet': 'Moon', 'symbol': '☽', 'day': 'Monday', 'quality': 'Reflection, intuition'},
    'Hg': {'planet': 'Mercury', 'symbol': '☿', 'day': 'Wednesday', 'quality': 'Transformation, communication'},
    'Cu': {'planet': 'Venus', 'symbol': '♀', 'day': 'Friday', 'quality': 'Love, beauty, harmony'},
    'Fe': {'planet': 'Mars', 'symbol': '♂', 'day': 'Tuesday', 'quality': 'Strength, action, will'},
    'Sn': {'planet': 'Jupiter', 'symbol': '♃', 'day': 'Thursday', 'quality': 'Expansion, abundance'},
    'Pb': {'planet': 'Saturn', 'symbol': '♄', 'day': 'Saturday', 'quality': 'Structure, limitation, time'},
}

# =============================================================================
# DATA STRUCTURES
# =============================================================================

class ChannelType(Enum):
    QUANTUM = "quantum"      # f = E/h (electronic transitions)
    ACOUSTIC = "acoustic"    # f ∝ M^(-1/3) (mass-dependent)
    CHEMICAL = "chemical"    # f = E_binding/h (bond energies)

@dataclass
class ElementProfile:
    """Complete framework profile for an element"""
    symbol: str
    name: str
    atomic_number: int
    atomic_mass: float
    
    # Raw atomic properties
    ionization_energy: float  # eV
    electronegativity: Optional[float]
    atomic_radius: float  # pm
    electron_config: str
    
    # Framework-derived properties
    impedance: float  # Derived atomic impedance
    impedance_log: float  # Log-scale for matching
    
    # Three channel frequencies
    f_quantum: float  # Hz - from ionization energy
    f_acoustic: float  # Hz - from mass scaling
    f_chemical: float  # Hz - estimated from typical bond energy
    
    # Consciousness resonance
    consciousness_affinity: float  # 0-1, how well it matches brain frequencies
    nearest_brainwave: str  # Which brainwave band it's closest to
    
    # Traditional correspondence
    planetary_metal: Optional[Dict]
    
    # Classification
    category: str  # alkali, noble gas, transition metal, etc.

# =============================================================================
# IMPEDANCE CALCULATION
# =============================================================================

def calculate_atomic_impedance(ionization_ev: float, electronegativity: Optional[float], 
                               radius_pm: float) -> Tuple[float, float]:
    """
    Calculate atomic impedance from first principles.
    
    Z_atom = √(E_ionization × χ) / r
    
    Physical interpretation:
    - High ionization energy = high resistance to change
    - High electronegativity = strong field, holds electrons tightly
    - Large radius = energy spread over larger volume = lower impedance
    
    For noble gases (no electronegativity), use ionization energy alone.
    """
    # Convert radius from pm to Angstroms for nicer numbers
    r_angstrom = radius_pm / 100.0
    
    if electronegativity is None:
        # Noble gas - use ionization energy as primary resistance
        # These are "high impedance" - don't want to interact
        Z = ionization_ev / r_angstrom
    else:
        # Standard calculation
        Z = np.sqrt(ionization_ev * electronegativity) / r_angstrom
    
    # Log-scale for framework matching (scale-invariant)
    Z_log = np.log(Z + 1)
    
    return Z, Z_log


def calculate_frequencies(ionization_ev: float, atomic_mass_amu: float) -> Tuple[float, float, float]:
    """
    Calculate three channel frequencies for an element.
    
    1. Quantum frequency: f = E_ionization / h
       This is the fundamental electronic transition frequency
       
    2. Acoustic frequency: f ∝ M^(-1/3)
       From the framework's acoustic scaling law
       Reference: 1 amu → ~10^13 Hz (molecular vibration scale)
       
    3. Chemical frequency: f = E_bond / h
       Typical bond energy ~3-5 eV, use ionization as proxy
    """
    # Quantum frequency (very high - PHz range)
    f_quantum = ionization_ev / H_PLANCK_EV  # Hz
    
    # Acoustic frequency (from mass scaling)
    # Calibrated so 1 amu ~ 10^13 Hz (molecular phonon scale)
    f_acoustic = 1e13 * (atomic_mass_amu ** (-1/3))
    
    # Chemical frequency (bond energy scale, typically lower than ionization)
    # Typical covalent bond ~2-4 eV, use 0.3 × ionization as estimate
    bond_energy_est = 0.3 * ionization_ev
    f_chemical = bond_energy_est / H_PLANCK_EV
    
    return f_quantum, f_acoustic, f_chemical


def calculate_consciousness_affinity(f_quantum: float, f_acoustic: float, 
                                    f_chemical: float, impedance: float) -> Tuple[float, str]:
    """
    Calculate how well an element's frequencies match consciousness frequencies.
    
    Brain frequencies:
    - Delta: 0.5-4 Hz
    - Theta: 4-8 Hz
    - Alpha: 8-13 Hz
    - Beta: 13-30 Hz
    - Gamma: 30-100 Hz
    
    We look for HARMONIC relationships, not direct matches
    (atomic frequencies are way higher than brain frequencies).
    
    Key insight: biological ion frequencies are SUBHARMONICS of atomic properties.
    """
    # Consciousness frequency targets
    consciousness_freqs = {
        'delta': 2,
        'theta': 6,
        'alpha': 10,
        'beta': 20,
        'gamma': 40,
        'high_gamma': 100
    }
    
    # Calculate subharmonic ratios
    # If f_atomic / N ≈ f_brain for some integer N, there's resonance
    best_match = 'none'
    best_affinity = 0.0
    
    for band, f_brain in consciousness_freqs.items():
        # Check acoustic frequency subharmonics (most relevant for bio)
        ratio = f_acoustic / f_brain
        log_ratio = np.log10(ratio)
        
        # How close is log_ratio to an integer? (octave relationship)
        nearest_octave = round(log_ratio)
        deviation = abs(log_ratio - nearest_octave)
        
        # Affinity based on how close to perfect harmonic
        affinity = np.exp(-deviation * 5)  # Sharp peak at harmonics
        
        if affinity > best_affinity:
            best_affinity = affinity
            best_match = band
    
    # Impedance factor - moderate impedance matches biology better
    # (Too high = inert, too low = unstable)
    optimal_impedance = 3.0  # Empirically, biological ions cluster here
    impedance_factor = np.exp(-((impedance - optimal_impedance) / 2) ** 2)
    
    final_affinity = best_affinity * impedance_factor
    
    return min(1.0, final_affinity), best_match


def classify_element(atomic_number: int, electron_config: str) -> str:
    """Classify element into periodic table category"""
    if atomic_number in [2, 10, 18, 36, 54, 86]:
        return "Noble Gas"
    elif atomic_number in [1]:
        return "Nonmetal"
    elif atomic_number in [3, 11, 19, 37, 55, 87]:
        return "Alkali Metal"
    elif atomic_number in [4, 12, 20, 38, 56, 88]:
        return "Alkaline Earth"
    elif atomic_number in [6, 7, 8, 15, 16, 34]:
        return "Nonmetal"
    elif atomic_number in [9, 17, 35, 53, 85]:
        return "Halogen"
    elif 21 <= atomic_number <= 30 or 39 <= atomic_number <= 48 or 72 <= atomic_number <= 80:
        return "Transition Metal"
    elif 57 <= atomic_number <= 71:
        return "Lanthanide"
    elif 89 <= atomic_number <= 103:
        return "Actinide"
    else:
        return "Other Metal"


# Element names
ELEMENT_NAMES = {
    'H': 'Hydrogen', 'He': 'Helium', 'Li': 'Lithium', 'Be': 'Beryllium',
    'B': 'Boron', 'C': 'Carbon', 'N': 'Nitrogen', 'O': 'Oxygen',
    'F': 'Fluorine', 'Ne': 'Neon', 'Na': 'Sodium', 'Mg': 'Magnesium',
    'Al': 'Aluminum', 'Si': 'Silicon', 'P': 'Phosphorus', 'S': 'Sulfur',
    'Cl': 'Chlorine', 'Ar': 'Argon', 'K': 'Potassium', 'Ca': 'Calcium',
    'Sc': 'Scandium', 'Ti': 'Titanium', 'V': 'Vanadium', 'Cr': 'Chromium',
    'Mn': 'Manganese', 'Fe': 'Iron', 'Co': 'Cobalt', 'Ni': 'Nickel',
    'Cu': 'Copper', 'Zn': 'Zinc', 'Ga': 'Gallium', 'Ge': 'Germanium',
    'As': 'Arsenic', 'Se': 'Selenium', 'Br': 'Bromine', 'Kr': 'Krypton',
    'Rb': 'Rubidium', 'Sr': 'Strontium', 'Ag': 'Silver', 'Sn': 'Tin',
    'I': 'Iodine', 'Cs': 'Cesium', 'Ba': 'Barium', 'Au': 'Gold',
    'Hg': 'Mercury', 'Pb': 'Lead', 'U': 'Uranium'
}


def analyze_element(symbol: str) -> Optional[ElementProfile]:
    """Generate complete framework profile for an element"""
    if symbol not in ELEMENT_DATA:
        return None
    
    data = ELEMENT_DATA[symbol]
    Z, mass, E_ion, chi, radius, config = data
    
    # Calculate impedance
    impedance, impedance_log = calculate_atomic_impedance(E_ion, chi, radius)
    
    # Calculate frequencies
    f_quantum, f_acoustic, f_chemical = calculate_frequencies(E_ion, mass)
    
    # Calculate consciousness affinity
    affinity, nearest_band = calculate_consciousness_affinity(
        f_quantum, f_acoustic, f_chemical, impedance
    )
    
    # Get planetary correspondence if exists
    planetary = PLANETARY_METALS.get(symbol)
    
    # Classify
    category = classify_element(Z, config)
    
    return ElementProfile(
        symbol=symbol,
        name=ELEMENT_NAMES.get(symbol, symbol),
        atomic_number=Z,
        atomic_mass=mass,
        ionization_energy=E_ion,
        electronegativity=chi,
        atomic_radius=radius,
        electron_config=config,
        impedance=impedance,
        impedance_log=impedance_log,
        f_quantum=f_quantum,
        f_acoustic=f_acoustic,
        f_chemical=f_chemical,
        consciousness_affinity=affinity,
        nearest_brainwave=nearest_band,
        planetary_metal=planetary,
        category=category
    )


# =============================================================================
# MIXTURE / COMPOUND ANALYSIS
# =============================================================================

def calculate_impedance_match(element1: str, element2: str) -> Tuple[float, str]:
    """
    Calculate impedance matching between two elements.
    
    R(Z1, Z2) = exp[-(ln(Z1) - ln(Z2))² / 2σ²]
    
    High R = elements combine easily (similar impedance)
    Low R = elements resist combination (mismatched impedance)
    """
    p1 = analyze_element(element1)
    p2 = analyze_element(element2)
    
    if not p1 or not p2:
        return 0.0, "Unknown element"
    
    # Log-space impedance matching (scale-invariant)
    sigma = 0.5  # Matching bandwidth
    delta_log = p1.impedance_log - p2.impedance_log
    R = np.exp(-(delta_log ** 2) / (2 * sigma ** 2))
    
    # Interpretation
    if R > 0.8:
        interpretation = "Excellent match - natural affinity"
    elif R > 0.5:
        interpretation = "Good match - can combine with moderate energy"
    elif R > 0.2:
        interpretation = "Weak match - requires significant energy to combine"
    else:
        interpretation = "Poor match - unlikely to form stable compound"
    
    return R, interpretation


def predict_compound_frequency(elements: List[str]) -> Dict:
    """
    Predict emergent frequency of a compound from its elements.
    
    Combined frequency depends on:
    1. Individual frequencies (wave superposition)
    2. Impedance matching (coupling efficiency)
    3. Mass weighting (heavier atoms dominate acoustic)
    """
    profiles = [analyze_element(e) for e in elements]
    profiles = [p for p in profiles if p is not None]
    
    if len(profiles) < 2:
        return {"error": "Need at least 2 valid elements"}
    
    # Mass-weighted acoustic frequency
    total_mass = sum(p.atomic_mass for p in profiles)
    f_acoustic_compound = 1e13 * (total_mass ** (-1/3))
    
    # Average chemical frequency (bonds involve multiple atoms)
    f_chemical_avg = np.mean([p.f_chemical for p in profiles])
    
    # Impedance of compound (geometric mean)
    Z_compound = np.exp(np.mean([p.impedance_log for p in profiles]))
    
    # Overall impedance matching between all pairs
    match_scores = []
    for i, p1 in enumerate(profiles):
        for p2 in profiles[i+1:]:
            R, _ = calculate_impedance_match(p1.symbol, p2.symbol)
            match_scores.append(R)
    
    avg_match = np.mean(match_scores) if match_scores else 0
    
    return {
        "elements": [p.symbol for p in profiles],
        "total_mass": total_mass,
        "f_acoustic_compound": f_acoustic_compound,
        "f_chemical_avg": f_chemical_avg,
        "compound_impedance": Z_compound,
        "average_impedance_match": avg_match,
        "stability_prediction": "Stable" if avg_match > 0.5 else "Unstable" if avg_match < 0.2 else "Metastable"
    }


# =============================================================================
# OUTPUT FUNCTIONS
# =============================================================================

def print_element_profile(profile: ElementProfile):
    """Pretty print element framework profile"""
    print("\n" + "=" * 70)
    print(f"     {profile.name.upper()} ({profile.symbol}) - Framework Profile")
    print("=" * 70)
    
    print(f"\n  ⚛️  ATOMIC PROPERTIES:")
    print(f"      Atomic Number: {profile.atomic_number}")
    print(f"      Atomic Mass: {profile.atomic_mass:.3f} amu")
    print(f"      Electron Config: {profile.electron_config}")
    print(f"      Category: {profile.category}")
    
    print(f"\n  ⚡ FRAMEWORK PROPERTIES:")
    print(f"      Ionization Energy: {profile.ionization_energy:.3f} eV")
    print(f"      Electronegativity: {profile.electronegativity or 'N/A (noble gas)'}")
    print(f"      Atomic Radius: {profile.atomic_radius} pm")
    
    print(f"\n  🔮 DERIVED IMPEDANCE:")
    print(f"      Z_atom: {profile.impedance:.4f}")
    print(f"      Z_log: {profile.impedance_log:.4f}")
    
    print(f"\n  〰️  CHANNEL FREQUENCIES:")
    print(f"      Quantum:  {profile.f_quantum:.3e} Hz ({profile.f_quantum/1e15:.2f} PHz)")
    print(f"      Acoustic: {profile.f_acoustic:.3e} Hz ({profile.f_acoustic/1e12:.2f} THz)")
    print(f"      Chemical: {profile.f_chemical:.3e} Hz ({profile.f_chemical/1e14:.2f} × 10¹⁴ Hz)")
    
    print(f"\n  🧠 CONSCIOUSNESS RESONANCE:")
    print(f"      Affinity: {profile.consciousness_affinity:.3f}")
    print(f"      Nearest Band: {profile.nearest_brainwave}")
    bar_len = int(profile.consciousness_affinity * 20)
    print(f"      [{'█' * bar_len}{'░' * (20-bar_len)}]")
    
    if profile.planetary_metal:
        pm = profile.planetary_metal
        print(f"\n  ✨ ALCHEMICAL CORRESPONDENCE:")
        print(f"      Planet: {pm['planet']} {pm['symbol']}")
        print(f"      Day: {pm['day']}")
        print(f"      Quality: {pm['quality']}")
    
    print("=" * 70)


def print_comparison_table(elements: List[str]):
    """Print comparison table of multiple elements"""
    profiles = [analyze_element(e) for e in elements]
    profiles = [p for p in profiles if p is not None]
    
    if not profiles:
        print("No valid elements")
        return
    
    print("\n" + "=" * 90)
    print("     ELEMENT COMPARISON - Framework Properties")
    print("=" * 90)
    
    # Header
    print(f"\n  {'Symbol':<6} {'Name':<12} {'Z':<4} {'Mass':<8} {'E_ion':<8} {'χ':<6} {'Z_atom':<8} {'Affinity':<8} {'Band':<10}")
    print(f"  {'-'*6} {'-'*12} {'-'*4} {'-'*8} {'-'*8} {'-'*6} {'-'*8} {'-'*8} {'-'*10}")
    
    for p in profiles:
        chi_str = f"{p.electronegativity:.2f}" if p.electronegativity else "N/A"
        print(f"  {p.symbol:<6} {p.name:<12} {p.atomic_number:<4} {p.atomic_mass:<8.2f} {p.ionization_energy:<8.3f} {chi_str:<6} {p.impedance:<8.3f} {p.consciousness_affinity:<8.3f} {p.nearest_brainwave:<10}")
    
    print("=" * 90)


def print_planetary_metals():
    """Print the 7 alchemical metals with framework analysis"""
    print("\n" + "=" * 70)
    print("     THE SEVEN PLANETARY METALS - Alchemical Framework")
    print("=" * 70)
    
    for symbol in ['Au', 'Ag', 'Hg', 'Cu', 'Fe', 'Sn', 'Pb']:
        profile = analyze_element(symbol)
        if profile and profile.planetary_metal:
            pm = profile.planetary_metal
            print(f"\n  {pm['symbol']} {pm['planet']:<10} → {profile.name} ({symbol})")
            print(f"     Impedance: {profile.impedance:.3f}")
            print(f"     Consciousness: {profile.nearest_brainwave} ({profile.consciousness_affinity:.3f})")
            print(f"     Quality: {pm['quality']}")
    
    print("\n" + "=" * 70)


# =============================================================================
# INTERACTIVE MODE
# =============================================================================

def interactive_mode():
    """Interactive element analysis"""
    print("\n" + "=" * 60)
    print("     ELEMENT FRAMEWORK ANALYZER")
    print("     Computational Alchemy Through Impedance")
    print("=" * 60)
    
    while True:
        print("\n  OPTIONS:")
        print("  1. Analyze single element")
        print("  2. Compare multiple elements")
        print("  3. Check impedance match between two elements")
        print("  4. Predict compound properties")
        print("  5. View planetary metals")
        print("  6. Find high consciousness-affinity elements")
        print("  7. Exit")
        
        choice = input("\n  Select (1-7): ").strip()
        
        if choice == '1':
            symbol = input("  Enter element symbol (e.g., Fe, Au, Zn): ").strip()
            profile = analyze_element(symbol)
            if profile:
                print_element_profile(profile)
            else:
                print(f"  Element '{symbol}' not found in database")
                
        elif choice == '2':
            symbols = input("  Enter element symbols (comma-separated): ").strip()
            elements = [s.strip() for s in symbols.split(',')]
            print_comparison_table(elements)
            
        elif choice == '3':
            e1 = input("  First element: ").strip()
            e2 = input("  Second element: ").strip()
            R, interp = calculate_impedance_match(e1, e2)
            print(f"\n  Impedance Match R({e1}, {e2}) = {R:.3f}")
            print(f"  Interpretation: {interp}")
            
        elif choice == '4':
            symbols = input("  Enter elements in compound (comma-separated): ").strip()
            elements = [s.strip() for s in symbols.split(',')]
            result = predict_compound_frequency(elements)
            print(f"\n  Compound Analysis: {result}")
            
        elif choice == '5':
            print_planetary_metals()
            
        elif choice == '6':
            print("\n  HIGH CONSCIOUSNESS-AFFINITY ELEMENTS:")
            ranked = []
            for symbol in ELEMENT_DATA:
                p = analyze_element(symbol)
                if p:
                    ranked.append((symbol, p.consciousness_affinity, p.nearest_brainwave))
            ranked.sort(key=lambda x: x[1], reverse=True)
            for symbol, affinity, band in ranked[:15]:
                print(f"    {symbol:<4} : {affinity:.3f} ({band})")
                
        elif choice == '7':
            print("\n  May your elements transmute! ✨")
            break
        else:
            print("  Invalid choice")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Command line mode
        symbol = sys.argv[1]
        profile = analyze_element(symbol)
        if profile:
            print_element_profile(profile)
        else:
            print(f"Element '{symbol}' not found")
    else:
        # Demo
        print("\n--- DEMO: Zinc (Consciousness Element) ---")
        print_element_profile(analyze_element('Zn'))
        
        print("\n--- DEMO: Biological Ions Comparison ---")
        print_comparison_table(['Na', 'K', 'Ca', 'Mg', 'Zn', 'Fe', 'Cu'])
        
        print("\n--- DEMO: Planetary Metals ---")
        print_planetary_metals()
        
        print("\n--- DEMO: NaCl Compound Prediction ---")
        result = predict_compound_frequency(['Na', 'Cl'])
        print(f"  NaCl Analysis: {result}")
        
        # Interactive
        interactive_mode()
