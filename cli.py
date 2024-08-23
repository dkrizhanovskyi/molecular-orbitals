# molecular_orbitals/cli.py

import click
from molecular_orbitals.core.molecule import Molecule, Atom
from molecular_orbitals.core.orbital_calculation import OrbitalCalculation
from molecular_orbitals.visualization.orbital_visualization import OrbitalVisualizer
from molecular_orbitals.io.file_parsers import XYZParser
from molecular_orbitals.io.data_exporters import JSONExporter, CSVExporter

@click.group()
def cli():
    """
    The main CLI entry point for the Molecular Orbitals and Reaction Modeling tool.
    """
    pass

@click.command()
@click.argument('filepath')
def parse_xyz(filepath):
    """
    Parses an XYZ file and outputs information about the molecule.

    :param filepath: Path to the XYZ file to be parsed.
    """
    parser = XYZParser(filepath)
    atoms = parser.parse()
    molecule = Molecule([Atom(atom['element'], atom['position']) for atom in atoms])
    click.echo(f'Parsed Molecule: {molecule}')

@click.command()
@click.argument('filepath')
@click.argument('output')
@click.option('--format', default='json', help='Output format: json or csv')
def export_data(filepath, output, format):
    """
    Exports molecular data to the specified format (JSON or CSV).

    :param filepath: Path to the input XYZ file.
    :param output: Path to the output file.
    :param format: Format of the output file, either 'json' or 'csv'.
    """
    parser = XYZParser(filepath)
    atoms = parser.parse()
    if format == 'json':
        exporter = JSONExporter(atoms)
    elif format == 'csv':
        exporter = CSVExporter(atoms)
    else:
        click.echo('Unsupported format!')
        return
    exporter.export(output)
    click.echo(f'Data exported to {output} in {format.upper()} format')

@click.command()
@click.argument('filepath')
def visualize_orbitals(filepath):
    """
    Visualizes molecular orbitals based on the data from an XYZ file.

    :param filepath: Path to the input XYZ file.
    """
    parser = XYZParser(filepath)
    atoms = parser.parse()
    molecule = Molecule([Atom(atom['element'], atom['position']) for atom in atoms])
    calculation = OrbitalCalculation(molecule)
    orbital_data = calculation.calculate_orbitals()
    
    visualizer = OrbitalVisualizer(orbital_data)
    visualizer.plot_2d()

# Adding commands to the CLI group
cli.add_command(parse_xyz)
cli.add_command(export_data)
cli.add_command(visualize_orbitals)

if __name__ == '__main__':
    cli()
