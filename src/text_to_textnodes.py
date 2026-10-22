from split_node_delimiter import split_node_delimiter
from split_nodes_links import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

def text_to_textnodes(text: str) -> list[TextNode]:
    delimiters = [("**", TextType.BOLD), ("_", TextType.ITALIC), ("`", TextType.CODE)]
    new_nodes = [TextNode(f"{text}", TextType.TEXT)]
    for delimiter in delimiters:
        new_nodes = split_node_delimiter(new_nodes, delimiter[0], delimiter[1])
    new_nodes = split_nodes_link(split_nodes_image(new_nodes))
    return new_nodes