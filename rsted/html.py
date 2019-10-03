from docutils.core import publish_string
from os.path import join as path_join

from rsted.anethtml import AnetHtmlWriter

default_rst_opts = {
    'no_generator': True,
    'no_source_link': True,
    'tab_width': 4,
    'file_insertion_enabled': False,
    'raw_enabled': False,
    'stylesheet_path': None,
    'traceback': True,
    'halt_level': 5,
}


def rst2html(rst, theme=None, opts=None):
    rst_opts = default_rst_opts.copy()
    if opts:
        rst_opts.update(opts)
    rst_opts['template'] = 'var/themes/template.txt'

    stylesheets = ['basic.css']
    if theme:
        stylesheets.append('%s/%s.css' % (theme, theme))
    rst_opts['stylesheet'] = ','.join([path_join('var/themes/', p) for p in stylesheets])

    out = publish_string(rst, writer=AnetHtmlWriter, writer_name='html', settings_overrides=rst_opts)

    return out
