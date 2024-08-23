import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

# Project information
project = 'Molecular Orbitals and Reaction Modeling'
copyright = '2024, Daniil Krizhanovskyi'
author = 'Daniil Krizhanovskyi'
release = '0.1'

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']
exclude_patterns = []

# Options for HTML output
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# If you need LaTeX support
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
}

# Napoleon settings (for Google and NumPy style docstrings)
napoleon_google_docstring = True
napoleon_numpy_docstring = True
