from rst2pdf.createpdf import RstToPdf
from flask import current_app
from codecs import lookup


utf8codec = lookup('utf-8')

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


def rst2pdf(content, theme=None):
    topdf = RstToPdf(basedir=current_app.config.root_path, breaklevel=0)
    buf = StringIO()

    if not content:
        content = '\0'
    content_utf8 = utf8codec.encode(content)[0]
    topdf.createPdf(text=content_utf8, output=buf, compressed=False)

    return buf.getvalue()
