import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("test", "dummy", props={"key1":"value1", "key2":"value2", "key3":"value3"})
        self.assertEqual(node.props_to_html(), ' key1="value1" key2="value2" key3="value3"')
    
    def test_empty_props_to_html(self):
        node = HTMLNode("test", "dummy")
        self.assertEqual(node.props_to_html(), "")
    
    def test_empty_children(self):
        node = HTMLNode("test", "dummy")
        self.assertEqual(node.children, None)

    def test_empty_props(self):
        node = HTMLNode("test", "dummy")
        self.assertEqual(node.props, None)
    
    def test___repr__(self):
        node = HTMLNode("test", "dummy", props={"key1":"value1", "key2":"value2", "key3":"value3"})
        self.assertEqual(node.__repr__(), 'HTMLNode(Tag=test, Value=dummy, Children=None, Props= key1="value1" key2="value2" key3="value3")')

if __name__ == "__main__":
    unittest.main()