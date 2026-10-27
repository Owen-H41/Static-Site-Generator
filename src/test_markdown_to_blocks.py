import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkDownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_with_leading_whitespace(self):
        md = """
    This is **bolded** paragraph

  This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

 - This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_with_trailing_whitespace(self):
        md = """
This is **bolded** paragraph            

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line    

- This is a list
- with items   
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_with_excessive_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line


- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_whitespace_and_newlines_only(self):
        md = """
     


   
 
   
   
 
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            []
        )

    def test_single_block(self):
        md = """
this is text within the only block of this test
the only one
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "this is text within the only block of this test\nthe only one"
            ]
        )