import unittest

from htmlnode import (
    HTMLNode,
    LeafNode,
    ParentNode
)

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode("a", "hello mom", None,{"href":"https://www.boot.dev"})

        self.assertEqual(
            " href=\"https://www.boot.dev\"",
            node.props_to_html()
        )

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "Test to_html method")
        self.assertEqual(
            "<p>Test to_html method</p>",
            node.to_html()
        )
    
    def test_to_html2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            '<a href="https://www.google.com">Click me!</a>',
            node.to_html()
        )

    def test_to_html_no_tag(self):
        node = LeafNode(None,"Hello world!")
        self.assertEqual(
            node.to_html(),
            "Hello world!"
        )
    
class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div",[child_node])
        self.assertEqual(parent_node.to_html(),"<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b","grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None,"Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None,"Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>"
        )


if __name__ == "__main__":
    unittest.main()