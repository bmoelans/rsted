"""
Anet's version to of rst to html
"""
from docutils.nodes import TextElement, Inline
from docutils.parsers.rst.roles import register_generic_role
from docutils.parsers.rst import Directive, directives
from docutils.writers.html4css1 import Writer, HTMLTranslator


class InlineText(Inline, TextElement):
    """
    This node class is a no-op -- just a fun way to define some parameters.
    There are lots of base classes to choose from in `docutils.nodes`.
    See examples in `docutils.nodes`
    """
    pass


class AnetIssue(Inline, TextElement):
    pass


class Foo(Directive):
    """
    This `Directive` class tells the ReST parser what to do with the text it
    encounters -- parse the input, perhaps, and return a list of node objects.
    Here, usage of a single required argument is shown.
    See examples in docutils.parsers.rst.directives.*
    """
    required_arguments = 1
    optional_arguments = 0
    has_content = True

    def run(self):
        thenode = InlineText(text=self.arguments[0])
        return [thenode]


class AnetHTMLTranslator(HTMLTranslator):
    """
    The `HTMLTranslator` turns nodes into actual source code. There is some
    serious magic here: when parsing nodes, `visit_[name](node)` then
    `depart_[name](node)` are called when a node named `[name]` is
    encountered.
    For details see docutils.writers.html4css1.__init__
    """
    def __init__(self, document):
        super(AnetHTMLTranslator, self).__init__(document)

    def visit_InlineText(self, node):
        # don't start tags; use
        #     self.starttag(node, tagname, suffix, empty, **attributes)
        # keyword arguments (attributes) are turned into html tag key/value
        # pairs, e.g. `{'style':'background:red'} => 'style="background:red"'`
        self.body.append(self.starttag(node, 'span', '', style='background:red'))

    def depart_InlineText(self, node):
        self.body.append('</span>')

    def visit_AnetIssue(self, node):
        self.body.append(f'<a href="https://anet.be/tracker/brocade/issue{node}">issue ')

    def depart_AnetIssue(self, node):
        self.body.append('</a>')

    settings_spec = ()


# register the directive, telling docutils to apply `Foo` when the parser encounters a `foo`
directives.register_directive('foo', Foo)
register_generic_role('issue', AnetIssue)

# create a `Writer` and set phasers to `AnetHTMLTranslator`
AnetHtmlWriter = Writer()
AnetHtmlWriter.translator_class = AnetHTMLTranslator
