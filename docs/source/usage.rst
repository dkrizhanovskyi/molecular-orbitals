Usage Guide
===========

This guide provides detailed instructions on how to use the Molecular Orbitals and Reaction Modeling library. Below are examples that cover a wide range of functionalities, from creating molecules to visualizing molecular orbitals.

Creating and Manipulating Molecules
-----------------------------------

The `Molecule` class is at the core of this library. It allows you to represent and manipulate molecular structures.

 **Creating a Simple Molecule**

You can create a molecule by defining its constituent atoms:

.. code-block:: python

    from molecular_orbitals.core.molecule import Molecule, Atom

    # Define individual atoms
    hydrogen1 = Atom('H', (0.0, 0.0, 0.0))
    hydrogen2 = Atom('H', (0.0, 0.0, 0.74))

    # Create a simple molecule (e.g., H2)
    molecule = Molecule(atoms=[hydrogen1, hydrogen2])

    print(f"Molecule has {len(molecule.get_atoms())} atoms.")

**Accessing and Modifying Atoms**

Once you've created a molecule, you can access and modify its atoms:

.. code-block:: python

    # Access the first atom
    first_atom = molecule.get_atoms()[0]
    print(f"First atom: {first_atom.element} at position {first_atom.position}")

    # Modify the position of an atom
    first_atom.position = (0.1, 0.1, 0.1)
    print(f"Updated position of first atom: {first_atom.position}")

Calculating Molecular Orbitals
-------------------------------

The `OrbitalCalculation` class allows you to compute molecular orbitals using quantum chemistry methods.

 **Hartree-Fock Calculation**

Here's how you can perform a Hartree-Fock calculation for a molecule:

.. code-block:: python

    from molecular_orbitals.core.orbital_calculation import OrbitalCalculation

    # Assume 'molecule' is already defined
    calc = OrbitalCalculation(molecule)

    # Calculate molecular orbitals using the Hartree-Fock method
    orbitals = calc.calculate_orbitals(method='HF')

    print("Orbital matrix:")
    print(orbitals)

**Integrating with Psi4**

If you have Psi4 installed, you can leverage its capabilities for more advanced calculations:

.. code-block:: python

    calc = OrbitalCalculation(molecule)
    psi4_orbitals = calc.calculate_orbitals(method='psi4')

    print("Psi4 orbital matrix:")
    print(psi4_orbitals)

Visualizing Molecular Orbitals
-------------------------------

The `OrbitalVisualizer` class enables visualization of molecular orbitals in both 2D and 3D.

**2D Visualization**

To create a 2D plot of molecular orbitals:

.. code-block:: python

    from molecular_orbitals.visualization.orbital_visualization import OrbitalVisualizer

    # Assume 'orbitals' is a matrix obtained from a previous calculation
    visualizer = OrbitalVisualizer(orbitals)

    # Plot the orbitals in 2D
    visualizer.plot_2d(title="H2 Molecular Orbital - 2D Plot")

**3D Visualization**

For a more detailed 3D visualization:

.. code-block:: python

    visualizer.plot_3d(title="H2 Molecular Orbital - 3D Plot")

**Saving Visualizations**

You can also save your visualizations to a file:

.. code-block:: python

    visualizer.save_figure("orbital_visualization.png")

Handling Input and Output
--------------------------

The library provides utilities for parsing molecular data from XYZ files and exporting results in various formats.

 **Parsing XYZ Files**

You can parse an XYZ file to create a `Molecule` object:

.. code-block:: python

    from molecular_orbitals.io.file_parsers import XYZParser

    # Parse the XYZ file to create a Molecule object
    parser = XYZParser()
    molecule = parser.parse("path/to/molecule.xyz")

    print(f"Parsed molecule with {len(molecule.get_atoms())} atoms.")

**Exporting Data**

Export the molecular data to JSON or CSV format:

.. code-block:: python

    from molecular_orbitals.io.data_exporters import JSONExporter

    # Export molecule to a JSON file
    exporter = JSONExporter()
    exporter.export(molecule, "molecule_data.json")

Command-Line Interface (CLI)
----------------------------

The library includes a command-line interface that provides a convenient way to perform common tasks directly from the terminal.

**Parsing XYZ Files**

To parse an XYZ file and print the molecular structure:

.. code-block:: bash

    molecular_orbitals parse_xyz path/to/molecule.xyz

**Exporting Data**

Export molecular data to a JSON file using the CLI:

.. code-block:: bash

    molecular_orbitals export_data path/to/molecule.xyz output.json --format json

**Visualizing Orbitals**

Generate a 2D visualization of molecular orbitals:

.. code-block:: bash

    molecular_orbitals visualize_orbitals path/to/molecule.xyz

Advanced Usage
--------------

For more advanced use cases, such as integrating with external quantum chemistry tools or performing custom analyses, please refer to the full documentation available at [Read the Docs](https://molecular_orbitals.readthedocs.io).
