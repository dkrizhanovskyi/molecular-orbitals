# Molecular Orbitals and Reaction Modeling - Usage Guide

This guide provides detailed examples on how to use the Molecular Orbitals and Reaction Modeling library. Follow these examples to understand the main functionalities of the library.

## 1. Creating and Manipulating Molecules

The `Molecule` class is the core data structure representing a molecule in this library. Below is an example of how to create a molecule and add atoms to it.

```python
from molecular_orbitals.core.molecule import Molecule, Atom

# Define individual atoms
hydrogen1 = Atom('H', (0.0, 0.0, 0.0))
hydrogen2 = Atom('H', (0.0, 0.0, 0.74))

# Create a molecule (e.g., H2)
molecule = Molecule(atoms=[hydrogen1, hydrogen2])

# Accessing atoms in a molecule
for atom in molecule.get_atoms():
    print(f"Element: {atom.element}, Position: {atom.position}")
```

## 2. Calculating Molecular Orbitals

The `OrbitalCalculation` class allows you to compute molecular orbitals using different methods. The example below demonstrates a Hartree-Fock calculation.

```python
from molecular_orbitals.core.orbital_calculation import OrbitalCalculation

# Assume 'molecule' is already defined as in the previous example
calc = OrbitalCalculation(molecule)

# Calculate molecular orbitals using the Hartree-Fock method
orbitals = calc.calculate_orbitals(method='HF')

print("Orbital matrix:")
print(orbitals)
```

## 3. Analyzing Reaction Mechanisms

The `ReactionMechanism` class is used to analyze chemical reactions. The following example shows how to define reactants and products and analyze the reaction.

```python
from molecular_orbitals.core.reaction_mechanism import ReactionMechanism

# Define reactants and products
reactant1 = Molecule([Atom('H', (0.0, 0.0, 0.0)), Atom('Cl', (0.0, 0.0, 1.0))])  # HCl
reactant2 = Molecule([Atom('Na', (0.0, 0.0, 0.0))])  # Na
product1 = Molecule([Atom('Na', (0.0, 0.0, 0.0)), Atom('Cl', (0.0, 0.0, 1.0))])  # NaCl
product2 = Molecule([Atom('H', (0.0, 0.0, 0.0))])  # H

# Create and analyze the reaction
reaction = ReactionMechanism(reactants=[reactant1, reactant2], products=[product1, product2])
analysis_result = reaction.analyze_reaction()

print("Reaction analysis:")
print(f"Number of reactants: {analysis_result['num_reactants']}")
print(f"Number of products: {analysis_result['num_products']}")
print(f"Activation energy: {analysis_result['activation_energy']}")
print(f"Transition state: {analysis_result['transition_state']}")
```

## 4. Visualizing Molecular Orbitals

The `OrbitalVisualizer` class is used for visualizing molecular orbitals in 2D and 3D. Here is an example of how to visualize an orbital matrix.

```python
from molecular_orbitals.visualization.orbital_visualization import OrbitalVisualizer

# Assume 'orbitals' is obtained from a previous calculation
visualizer = OrbitalVisualizer(orbitals)

# Plot the orbitals in 2D
visualizer.plot_2d(title="H2 Molecular Orbital - 2D Plot")
```

## 5. Command-Line Interface (CLI)

The library also provides a CLI for interacting with the functionality directly from the command line.

### Parsing XYZ Files

```bash
molecular_orbitals parse_xyz molecule.xyz
```

### Exporting Data

```bash
molecular_orbitals export_data molecule.xyz output.json --format json
```

### Visualizing Orbitals

```bash
molecular_orbitals visualize_orbitals molecule.xyz
```

## 6. Advanced Usage

For more advanced use cases, such as integrating with Psi4 for quantum chemistry calculations, please refer to the full documentation available at [Read the Docs](https://molecular_orbitals.readthedocs.io).

