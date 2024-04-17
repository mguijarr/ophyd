# -*- coding: utf-8 -*-
#
# ophyd documentation build configuration file, created by
# sphinx-quickstart on Fri Nov  7 11:18:58 2014.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.
import ophyd

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.autosummary",
    "IPython.sphinxext.ipython_directive",
    "IPython.sphinxext.ipython_console_highlighting",
    "matplotlib.sphinxext.plot_directive",
    "myst_parser",
    "sphinx.ext.inheritance_diagram",
    "numpydoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.intersphinx",
    # For the card element
    "sphinx_design",
]

# The name of a reST role (builtin or Sphinx extension) to use as the default
# role, that is, for text marked up `like this`
default_role = "any"

# If true, Sphinx will warn about all references where the target cannot
# be found.
# nitpicky = True

# The suffix of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "ophyd"
copyright = "2014, Brookhaven National Lab"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ophyd.__version__

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "pydata_sphinx_theme"
github_repo = project
github_user = "bluesky"

# Theme options for pydata_sphinx_theme
html_theme_options = dict(
    use_edit_page_button=True,
    github_url=f"https://github.com/{github_user}/{github_repo}",
    icon_links=[
        dict(
            name="PyPI",
            url=f"https://pypi.org/project/{project}",
            icon="fas fa-cube",
        ),
        dict(
            name="Gitter",
            url="https://gitter.im/NSLS-II/DAMA",
            icon="fas fa-person-circle-question",
        ),
    ],
    external_links=[
        dict(
            name="Bluesky Project",
            url="https://blueskyproject.io",
        )
    ],
)

# A dictionary of values to pass into the template engine’s context for all pages
html_context = dict(
    github_user=github_user,
    github_repo=project,
    github_version="master",
    doc_path="docs",
)

html_logo = "images/bluesky_ophyd_logo.svg"
html_favicon = "images/ophyd_favicon.svg"

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "bluesky": ("https://blueskyproject.io/bluesky/main", None),
    "numpy": ("https://numpy.org/devdocs/", None),
    "databroker": ("https://blueskyproject.io/databroker/", None),
    "event-model": ("https://blueskyproject.io/event-model/main", None),
}

# If False and a module has the __all__ attribute set, autosummary documents
# every member listed in __all__ and no others. Default is True
autosummary_ignore_module_all = False

# Look for signatures in the first line of the docstring (used for C functions)
autodoc_docstring_signature = True

# Both the class’ and the __init__ method’s docstring are concatenated and
# inserted into the main body of the autoclass directive
autoclass_content = "both"

# Order the members by the order they appear in the source code
autodoc_member_order = "bysource"

# numpydoc config
numpydoc_show_class_members = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# Where to put Ipython savefigs
ipython_savefig_dir = "../build/savefig"
