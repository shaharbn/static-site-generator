from htmlnode import *

class LeafNode(HTMLNode):
    """
    A LeafNode is a type of HTMLNode that represents a single HTML tag with no children. For example, a simple <p> tag with some text inside of it

    ...

    Attributes
    ----------
    tag
    value
    props (default to None)

    Methods
    -------
    to_html()
        convert the leaf to html tag
    """
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Invalid HTML: no value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
