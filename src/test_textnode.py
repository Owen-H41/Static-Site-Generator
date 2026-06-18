import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("this is a text node", TextType.TEXT)
        node2 = TextNode("this is a different text node", TextType.TEXT)
        self.assertNotEqual(node, node2)
    
    def test_same_url(self):
        node = TextNode("This is a URL node", TextType.LINK, "www.test_website.com")
        node2 = TextNode("This is a URL node", TextType.LINK, "www.test_website.com")
        self.assertEqual(node, node2)
    
    def test_not_same_url(self):
        node = TextNode("This is a URL node", TextType.LINK, "www.test_website.com")
        node2 = TextNode("This is a URL node", TextType.LINK, "www.bad_test_website.com")
        self.assertNotEqual(node, node2)
    
    def test_same_texttype(self):
        node = TextNode("this is a text node", TextType.TEXT)
        node2 = TextNode("this is a different text node", TextType.TEXT)
        self.assertEqual(node.text_type, node2.text_type)

    def test_not_same_texttype(self):
        node = TextNode("this is a text node", TextType.TEXT)
        node2 = TextNode("this is a different text node", TextType.BOLD)
        self.assertNotEqual(node.text_type, node2.text_type)
    
    def test_text_to_leafnode(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold_to_leafnode(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
    
    def test_italic_to_leafnode(self):
        node = TextNode("This is a italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic node")

    def test_code_to_leafnode(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")
    
    def test_link_to_leafnode(self):
        node = TextNode("This is a link node", TextType.LINK, "https://google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"herf": "https://google.com"})

    def test_image_to_leafnode(self):
        node = TextNode("This is a image node", TextType.IMAGE, "https://google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://google.com", "alt": "This is a image node"})

if __name__ == "__main__":
    unittest.main()