# Molecular Orbitals and Reaction Modeling

[![PyPI version](https://badge.fury.io/py/molecular_orbitals.svg)](https://badge.fury.io/py/molecular_orbitals)
[![Documentation Status](https://readthedocs.org/projects/molecular-orbitals-and-reaction-modeling/badge/?version=latest)](https://molecular-orbitals-and-reaction-modeling.readthedocs.io/en/latest/?badge=latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

Molecular Orbitals and Reaction Modeling is a Python library for modeling molecular orbitals and analyzing chemical reactions using quantum chemistry methods. The library is designed to be easy to use, extendable, and compatible with external quantum chemistry tools like Psi4.

### Key Features

- **Molecular Orbital Calculation:**
  - Supports Hartree-Fock and integration with Psi4.
  - Flexible input options for various molecular structures.
  - Customizable calculation methods.

- **Reaction Mechanism Analysis:**
  - Calculate activation energy and identify transition states.
  - Support for complex multi-step reactions.
  - Integration with visualization tools for reaction pathways.

- **Visualization:**
  - Generate 2D and 3D visualizations of molecular orbitals.
  - Save visualizations in various formats (PNG, PDF, etc.).
  - Interactive plotting support.

- **Data Handling:**
  - Parse XYZ files for molecular data.
  - Export data to JSON or CSV formats.
  - Easy integration with other data processing libraries.

### Installation

You can install the `molecular_orbitals` library directly from PyPI:

```bash
pip install molecular_orbitals
```

For advanced quantum chemistry calculations, you may also want to install Psi4:

```bash
conda install psi4 -c psi4
```

### Getting Started

Here is a quick example to get you started with calculating molecular orbitals:

```python
from molecular_orbitals.core.molecule import Molecule, Atom
from molecular_orbitals.core.orbital_calculation import OrbitalCalculation

# Define a molecule (e.g., H2)
atoms = [
    Atom('H', (0.0, 0.0, 0.0)),
    Atom('H', (0.0, 0.0, 0.74))
]
molecule = Molecule(atoms)

# Calculate orbitals using the Hartree-Fock method
calc = OrbitalCalculation(molecule)
orbitals = calc.calculate_orbitals(method='HF')

print("Orbital matrix:")
print(orbitals)
```

### Command-Line Interface (CLI)

The library also includes a command-line interface (CLI) for easier interaction. Here are some common commands:

#### Parsing XYZ Files

```bash
molecular_orbitals parse_xyz molecule.xyz
```

This command parses an XYZ file and outputs the molecular structure.

#### Exporting Data

Export molecular data to JSON or CSV format:

```bash
molecular_orbitals export_data molecule.xyz output.json --format json
```

#### Visualizing Orbitals

Generate a 2D or 3D visualization of molecular orbitals:

```bash
molecular_orbitals visualize_orbitals molecule.xyz
```

### Documentation

Full documentation, including detailed examples and API references, can be found on the [official documentation site](https://molecular-orbitals-and-reaction-modeling.readthedocs.io).

### Contributing

We welcome contributions from the community! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

For more details, see our [CONTRIBUTING.md](CONTRIBUTING.md) file.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

We would like to thank the open-source community for their invaluable contributions to this project.

