import unittest
from textnode import TextNode, TextType

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
        node = TextNode("This is a URL node", TextType.URL, "www.test_website.com")
        node2 = TextNode("This is a URL node", TextType.URL, "www.test_website.com")
        self.assertEqual(node, node2)
    
    def test_not_same_url(self):
        node = TextNode("This is a URL node", TextType.URL, "www.test_website.com")
        node2 = TextNode("This is a URL node", TextType.URL, "www.bad_test_website.com")
        self.assertNotEqual(node, node2)
    
    def test_same_texttype(self):
        node = TextNode("this is a text node", TextType.TEXT)
        node2 = TextNode("this is a different text node", TextType.TEXT)
        self.assertEqual(node.text_type, node2.text_type)

    def test_not_same_texttype(self):
        node = TextNode("this is a text node", TextType.TEXT)
        node2 = TextNode("this is a different text node", TextType.BOLD)
        self.assertNotEqual(node.text_type, node2.text_type)
    

if __name__ == "__main__":
    unittest.main()