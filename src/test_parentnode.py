import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_nested_children(self):
        node1_1 = LeafNode("b", "grandchild 1 of child 1")
        node1_2 = LeafNode("p", "grandchild 2 of child 1")
        node2_1 = LeafNode("b", "grandchild 1 of child 2")
        node2_2 = LeafNode("p", "grandchild 2 of child 2")
        node1 = ParentNode("span1", [node1_1, node1_2])
        node2 = ParentNode("span2", [node2_1, node2_2])
        Parent_node = ParentNode("div", [node1, node2])
        self.assertEqual(
            Parent_node.to_html(),
            "<div><span1><b>grandchild 1 of child 1</b><p>grandchild 2 of child 1</p></span1><span2><b>grandchild 1 of child 2</b><p>grandchild 2 of child 2</p></span2></div>"
        )
    
    def test_to_html_with_nested_link(self):
        node1_1 = LeafNode("a", "Click Me!", {"herf": "https://google.com"})
        node1_2 = LeafNode("p", "that was a link")
        node1 = ParentNode("span", [node1_1, node1_2])
        self.assertEqual(
            node1.to_html(),
            '<span><a herf="https://google.com">Click Me!</a><p>that was a link</p></span>'
        )
    
if __name__ == "__main__":
    unittest.main()