master_doc = 'index'
extensions = [
    "myst_parser",
    'sphinx_rtd_theme',
]
latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
'pointsize': '12pt',

'fontpkg': r"""
\PassOptionsToPackage{bookmarksnumbered}{hyperref}

""",

# Additional stuff for the LaTeX preamble.
'preamble': r"""
\usepackage{setspace}
""",

'footer': r"""
""",

'maketitle': r'''
\pagenumbering{arabic}
''',
'extraclassoptions': 'openany,oneside'    
}
html_theme = "sphinx_rtd_theme"
