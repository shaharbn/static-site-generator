class HTMLNode():
    """
    The HTMLNode class will represent a "node" in an HTML document tree
    (like a <p> tag and its contents, or an <a> tag and its contents)
    and is purpose-built to render itself as HTML.

    ...

    Attributes
    ----------
    tag: str
        A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        An HTMLNode without a tag will just render as raw text
    value: str
        A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        An HTMLNode without a value will be assumed to have children
    children: list
        A list of HTMLNode objects representing the children of this node
        An HTMLNode without children will be assumed to have a value
    props: dictionary(key = attrubute name, value = the value of the attribute)
        A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
        An HTMLNode without props simply won't have any attributes


    Methods
    -------
    to_html()
        child class need to override
    props_to_html()
        return the attributes and their values as string
    __repr__(self):
        return the string that represent of the TextNode object:
        HtmlNode(tag, value, children, props)
    """
    def __init__(self, tag = None, value = None, children = None, props = None):
        """
        Parameters
        ----------
        tag: str
            A string representing the HTML tag name (e.g. "p", "a", "h1", etc.), default to None.
            An HTMLNode without a tag will just render as raw text
        value: str
            A string representing the value of the HTML tag (e.g. the text inside a paragraph), default to None.
            An HTMLNode without a value will be assumed to have children
        children: list
            A list of HTMLNode objects representing the children of this node, default to None.
            An HTMLNode without children will be assumed to have a value
        props: dictionary(key = attrubute name, value = the value of the attribute)
            A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}, default to None.
            An HTMLNode without props simply won't have any attributes
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        """
        child class need to override
        """
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        """
        return the attributes and their values as string
        """
        result = ""
        for key in self.props:
            result += f' {key}="{self.props[key]}"'
        return result

    def __repr__(self):
        """
        return the string that represent of the TextNode object:
        HtmlNode(tag, value, children, props)
        """
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"