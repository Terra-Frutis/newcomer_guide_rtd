master_doc = 'index'
extensions = [
    "myst_parser",
    'nature',
]
html_theme = 'epub'
html_theme_options = {
"footer": "false",
    
}
latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'letterpaper',
'classoptions':',openany',
# The font size ('10pt', '11pt' or '12pt').
'pointsize': '12pt',

'fontpkg': r"""
\PassOptionsToPackage{bookmarksnumbered}{hyperref}
""",
'maketitle': r'''
\pagenumbering{arabic}
''',
'extraclassoptions': 'openany,oneside'    
}
html_theme = "sphinx_rtd_theme"
