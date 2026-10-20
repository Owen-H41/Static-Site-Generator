import unittest
from extract_markdown_links import extract_markdown_links, extract_markdown_images

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.boot.dev)"
        )
        self.assertListEqual([("link", "https://www.boot.dev")], matches)

    def test_no_image(self):
        matches = extract_markdown_images(
            "This is text without an image"
        )
        self.assertListEqual([], matches)

    def test_no_link(self):
        matches = extract_markdown_links(
            "this is text without a link"
        )
        self.assertListEqual([], matches)

    def test_multiple_images(self):
        matches = extract_markdown_images(
            "this is text with multiple images, here's ![one](https://test.com/one) and here's ![two](https://test.com/two)"
        )
        self.assertListEqual([("one", "https://test.com/one"), ("two", "https://test.com/two")], matches)

    def test_multiple_links(self):
        matches = extract_markdown_links(
            "this is text with multiple Links, here's [one](https://test.com/one) and here's [two](https://test.com/two)"
        )
        self.assertListEqual([("one", "https://test.com/one"), ("two", "https://test.com/two")], matches)

    def test_both_link_and_image(self):
        text = "this is text with both an ![image](https://test.com/image) and a [link](https://test.com/link)"
        link_matches = extract_markdown_links(text)
        image_matches = extract_markdown_images(text)
        self.assertListEqual([("image", "https://test.com/image")], image_matches)
        self.assertListEqual([("link", "https://test.com/link")], link_matches)