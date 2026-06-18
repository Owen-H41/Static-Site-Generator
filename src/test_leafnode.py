import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf___repr__(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.__repr__(), 'LeafNode(Tag=p, Value=Hello, world!, Props=)')
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click Me!", {"herf": "https://google.com"})
        self.assertEqual(node.to_html(), '<a herf="https://google.com">Click Me!</a>')

    def test_lead_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

if __name__ == "__main__":
    unittest.main()