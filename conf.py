# -*- coding: utf-8 -*-
import os
import sphinx_rtd_theme

project = u"jsobj"
copyright = u"2016, Mateusz 'novo' Klos"
author = u"Mateusz 'novo' Klos"


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    'sphinx.ext.viewcode',
]

version = read('VERSION').strip()
release = read('VERSION').strip()
doctest_test_doctest_blocks='default'
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'README'
language = None
exclude_patterns = [
    '_build',
    'env',
    'tmp',
    '.tox',
    'Thumbs.db',
    '.DS_Store'
]
todo_include_todos = False
intersphinx_mapping = {'https://docs.python.org/': None}

default_role = 'any'
pygments_style = 'monokai'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme = "sphinx_rtd_theme"
html_static_path = ['docs/_static']
htmlhelp_basename = 'jsobjdoc'

latex_elements = {}
latex_documents = [
    (master_doc, 'jsobj.tex', 'jsobj Documentation',
     author, 'manual'),
]
man_pages = [
    (master_doc, 'jsobj', 'jsobj Documentation', [author], 1)
]
texinfo_documents = [
    (master_doc, 'jsobj', 'jsobj Documentation',
     author, 'jsobj', 'Utility class around dict for easier use.',
     'Miscellaneous'),
]
