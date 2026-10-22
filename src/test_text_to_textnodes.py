import unittest
from text_to_textnodes import text_to_textnodes
from split_node_delimiter import split_node_delimiter
from split_nodes_links import split_nodes_image, split_nodes_link
from textnode import TextType, TextNode

class TestTextToTextnode(unittest.TestCase):
    def test_all_delimiters(self):
        new_nodes = text_to_textnodes(
            "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
            )
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev")
            ],
            new_nodes
        )

    def test_all_delimiters_no_text(self):
        new_nodes = text_to_textnodes(
            "**text**_italic_`code block`![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)[link](https://boot.dev)"
            )
        self.assertListEqual(
            [
                TextNode("text", TextType.BOLD),
                TextNode("italic", TextType.ITALIC),
                TextNode("code block", TextType.CODE),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode("link", TextType.LINK, "https://boot.dev")
            ],
            new_nodes
        )

    def test_text_only(self):
        new_nodes = text_to_textnodes(
            "this is plain text with no special text"
        )
        self.assertListEqual(
            [
                TextNode("this is plain text with no special text", TextType.TEXT)
            ],
            new_nodes
        )