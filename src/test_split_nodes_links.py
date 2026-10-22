import unittest
from split_nodes_links import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestSplitNodesLinks(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes
        )

    def test_split_link_then_image(self):
        node = TextNode(
            "This is text with a [link](https://link.test.com) and an ![image](https://image.test.com)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image(split_nodes_link([node]))
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://link.test.com"),
                TextNode(" and an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://image.test.com")
            ],
            new_nodes
        )

    def test_split_image_then_link(self):
        node = TextNode(
            "This is text with a [link](https://link.test.com) and an ![image](https://image.test.com)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link(split_nodes_image([node]))
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://link.test.com"),
                TextNode(" and an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://image.test.com")
            ],
            new_nodes
        )

    def test_image_at_start(self):
        node = TextNode(
            "![image](https://image.test.com) was at the start of this text",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://image.test.com"),
                TextNode(" was at the start of this text", TextType.TEXT)
            ],
            new_nodes
        )

    def test_link_at_start(self):
        node = TextNode(
            "[link](https://link.test.com) was at the start of this text",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://link.test.com"),
                TextNode(" was at the start of this text", TextType.TEXT)
            ],
            new_nodes
        )

    def test_image_at_end(self):
        node = TextNode(
            "This text ends with an ![image](https://image.test.com)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This text ends with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://image.test.com")
            ],
            new_nodes
        )

    def test_link_at_end(self):
        node = TextNode(
            "This text ends with an [link](https://link.test.com)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This text ends with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://link.test.com")
            ],
            new_nodes
        )

    def test_only_image(self):
        node = TextNode(
            "![image](https://image.test.com)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://image.test.com")
            ],
            new_nodes
        )

    def test_only_link(self):
        node = TextNode(
            "[link](https://link.test.com)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://link.test.com")
            ],
            new_nodes
        )

    def test_no_image(self):
        node = TextNode(
            "This is text with no image",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with no image", TextType.TEXT)
            ],
            new_nodes
        )

    def test_no_link(self):
        node = TextNode(
            "This is text with no link",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with no link", TextType.TEXT)
            ],
            new_nodes
        )

    def test_two_images_touching(self):
        node = TextNode(
            "this is text with these ![image1](https://image1.test.com)![image2](https://image2.test.com) touching in the middle",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("this is text with these ", TextType.TEXT),
                TextNode("image1", TextType.IMAGE, "https://image1.test.com"),
                TextNode("image2", TextType.IMAGE, "https://image2.test.com"),
                TextNode(" touching in the middle", TextType.TEXT)
            ],
            new_nodes
        )

    def test_two_links_touching(self):
        node = TextNode(
            "this is text with these [link1](https://link1.test.com)[link2](https://link2.test.com) touching in the middle",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("this is text with these ", TextType.TEXT),
                TextNode("link1", TextType.LINK, "https://link1.test.com"),
                TextNode("link2", TextType.LINK, "https://link2.test.com"),
                TextNode(" touching in the middle", TextType.TEXT)
            ],
            new_nodes
        )

    def test_image_and_link_touching(self):
        node = TextNode(
            "this is text with these ![image](https://image.test.com)[link](https://link.test.com) touching in the middle",
            TextType.TEXT
        )
        new_nodes = split_nodes_link(split_nodes_image([node]))
        self.assertListEqual(
            [
                TextNode("this is text with these ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://image.test.com"),
                TextNode("link", TextType.LINK, "https://link.test.com"),
                TextNode(" touching in the middle", TextType.TEXT)
            ],
            new_nodes
        )

    def test_link_and_image_touching(self):
        node = TextNode(
            "this is text with these [link](https://link.test.com)![image](https://image.test.com) touching in the middle",
            TextType.TEXT
        )
        new_nodes = split_nodes_link(split_nodes_image([node]))
        self.assertListEqual(
            [
                TextNode("this is text with these ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://link.test.com"),
                TextNode("image", TextType.IMAGE, "https://image.test.com"),
                TextNode(" touching in the middle", TextType.TEXT)
            ],
            new_nodes
        )