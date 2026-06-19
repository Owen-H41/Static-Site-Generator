import unittest
from split_node_delimiter import split_node_delimiter
from textnode import TextNode, TextType

class TestSplitNodeDelimiter(unittest.TestCase):
    def test_no_inline_text(self):
        list_of_TextNodes = [
            TextNode("this text is just plain and contains no inline delimiters", TextType.TEXT)
        ]
        delimited_nodes = split_node_delimiter(list_of_TextNodes, "**", TextType.BOLD)
        self.assertEqual(
            delimited_nodes,
            [TextNode("this text is just plain and contains no inline delimiters", TextType.TEXT)]
        )
    
    def test_bold_inline_text(self):
        list_of_TextNodes = [
            TextNode("this text contains a **Bold** piece of text in it.", TextType.TEXT)
        ]
        delimited_nodes = split_node_delimiter(list_of_TextNodes, "**", TextType.BOLD)
        self.assertEqual(
            delimited_nodes,
            [
                TextNode("this text contains a ", TextType.TEXT),
                TextNode("Bold", TextType.BOLD),
                TextNode(" piece of text in it.", TextType.TEXT)
            ]
        )
    
    def test_2_bold_inline_text(self):
        list_of_TextNodes = [
            TextNode("this text contains two **Bold** pieces of **Bold** text in it.", TextType.TEXT)
        ]
        delimited_nodes = split_node_delimiter(list_of_TextNodes, "**", TextType.BOLD)
        self.assertEqual(
            delimited_nodes,
            [
                TextNode("this text contains two ", TextType.TEXT),
                TextNode("Bold", TextType.BOLD),
                TextNode(" pieces of ", TextType.TEXT),
                TextNode("Bold", TextType.BOLD),
                TextNode(" text in it.", TextType.TEXT)
            ]
        )
    
    def test_italic_inline_text(self):
        list_of_TextNodes = [
            TextNode("this text contains an _italic_ piece of text in it.", TextType.TEXT)
        ]
        delimited_nodes = split_node_delimiter(list_of_TextNodes, "_", TextType.ITALIC)
        self.assertEqual(
            delimited_nodes,
            [
                TextNode("this text contains an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" piece of text in it.", TextType.TEXT)
            ]
        )

    def test_2_italic_inline_text(self):
        list_of_TextNodes = [
            TextNode("this text contains two _italic_ pieces of _italic_ text in it.", TextType.TEXT)
        ]
        delimited_nodes = split_node_delimiter(list_of_TextNodes, "_", TextType.ITALIC)
        self.assertEqual(
            delimited_nodes,
            [
                TextNode("this text contains two ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" pieces of ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text in it.", TextType.TEXT)
            ]
        )

    def test_code_inline_text(self):
        list_of_TextNodes = [
            TextNode("this text contains a `code` piece of text in it.", TextType.TEXT)
        ]
        delimited_nodes = split_node_delimiter(list_of_TextNodes, "`", TextType.CODE)
        self.assertEqual(
            delimited_nodes,
            [
                TextNode("this text contains a ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" piece of text in it.", TextType.TEXT)
            ]
        )

    def test_2_code_inline_text(self):
        list_of_TextNodes = [
            TextNode("this text contains two `code` pieces of `code` text in it.", TextType.TEXT)
        ]
        delimited_nodes = split_node_delimiter(list_of_TextNodes, "`", TextType.CODE)
        self.assertEqual(
            delimited_nodes,
            [
                TextNode("this text contains two ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" pieces of ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" text in it.", TextType.TEXT)
            ]
        )

    def test_multi_delimter_inline_text(self):
        list_of_textnodes = [
            TextNode("this text conatins both a **Bold** and an _italic_ section of text.", TextType.TEXT),
            TextNode("this text conatins both a **Bold** and a `code` section of text.", TextType.TEXT),
            TextNode("this text conatins both a `code` and an _italic_ section of text.", TextType.TEXT),
            TextNode("this text conatins a **Bold**, a `code` and an _italic_ section of text.", TextType.TEXT)
        ]
        delimited_nodes = split_node_delimiter(split_node_delimiter(split_node_delimiter(list_of_textnodes, "**", TextType.BOLD), "_", TextType.ITALIC), "`", TextType.CODE)
        self.assertEqual(
            delimited_nodes,
            [
                TextNode("this text conatins both a ", TextType.TEXT),
                TextNode("Bold", TextType.BOLD),
                TextNode(" and an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" section of text.", TextType.TEXT),
                TextNode("this text conatins both a ", TextType.TEXT),
                TextNode("Bold", TextType.BOLD),
                TextNode(" and a ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" section of text.", TextType.TEXT),
                TextNode("this text conatins both a ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" section of text.", TextType.TEXT),
                TextNode("this text conatins a ", TextType.TEXT),
                TextNode("Bold", TextType.BOLD),
                TextNode(", a ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" section of text.", TextType.TEXT)
            ]
        )

    def test_inline_delimiters_at_start_or_end_of_textnode(self):
        list_of_textnodes = [
            TextNode("**Bold** at the start", TextType.TEXT),
            TextNode("_italic_ at the start", TextType.TEXT),
            TextNode("`code` at the start", TextType.TEXT),
            TextNode("ends with **Bold**", TextType.TEXT),
            TextNode("ends with _italic_", TextType.TEXT),
            TextNode("ends with `code`", TextType.TEXT)
        ]
        delimted_nodes = split_node_delimiter(split_node_delimiter(split_node_delimiter(list_of_textnodes, "**", TextType.BOLD), "_", TextType.ITALIC), "`", TextType.CODE)
        self.assertEqual(
            delimted_nodes,
            [
                TextNode("Bold", TextType.BOLD),
                TextNode(" at the start", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" at the start", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" at the start", TextType.TEXT),
                TextNode("ends with ", TextType.TEXT),
                TextNode("Bold", TextType.BOLD),
                TextNode("ends with ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode("ends with ", TextType.TEXT),
                TextNode("code", TextType.CODE),
            ]
        )

if __name__ == "__main__":
    unittest.main()