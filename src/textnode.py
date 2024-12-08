from enum import Enum
from leafnode import *

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    """
    A class used to represent an text that part of bigger text

    ...

    Attributes
    ----------
    text: str
        The text content of the node
    text_type: TextType enum
        The type of text this node contains, which is a member of the TextType enum.
    url: str
        The URL of the link or image, if the text is a link. Default to None if nothing is passed in.


    Methods
    -------
    __eq__(other)
        compare 2 TextNode objects attributes.
    __repr__(self)
        return string that represent the TextNode object: TextNode(TEXT, TEXT_TYPE, URL)
    """
    def __init__(self, text, text_type, url=None):
        """
        Parameters
        ----------
        text: str
            The text content of the node
        text_type: TextType enum
            The type of text this node contains, which is a member of the TextType enum.
        url: str
            The URL of the link or image, if the text is a link. Default to None if nothing is passed in.
        """
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        """
        compare between 2 TextNode objects.
        If all of the properties equals return True other wise return False.

        Parameters
        ----------
        other: TextNode object
            second TextNode object to compere
        """
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False

    def __repr__(self):
        """
        return the string that represent of the TextNode object:
        TextNode(TEXT, TEXT_TYPE, URL)
        """
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    """
    the function take TextNode object and convert it to LeafNode
    """
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Invalid text type: {text_node.text_type}")