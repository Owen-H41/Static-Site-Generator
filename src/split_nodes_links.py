from extract_markdown_links import extract_markdown_links, extract_markdown_images
from textnode import TextNode, TextType

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if links == []:
            new_nodes.append(node)
            continue
        sections = [node.text]
        potential_new_nodes = []
        for i in links:
            sections = sections[-1]
            sections = sections.split(f"[{i[0]}]({i[1]})", 1)
            potential_new_nodes.append(TextNode(sections[0], TextType.TEXT))
            potential_new_nodes.append(TextNode(i[0], TextType.LINK, i[1]))
        potential_new_nodes.append(TextNode(sections[-1], TextType.TEXT))
        for potential_node in potential_new_nodes:
            if (potential_node.text_type == TextType.TEXT) and (potential_node.text == ""):
                continue
            else:
                new_nodes.append(potential_node)
    return new_nodes


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if images == []:
            new_nodes.append(node)
            continue
        sections = [node.text]
        potential_new_nodes = []
        for i in images:
            sections = sections[-1]
            sections = sections.split(f"![{i[0]}]({i[1]})", 1)
            potential_new_nodes.append(TextNode(sections[0], TextType.TEXT))
            potential_new_nodes.append(TextNode(i[0], TextType.IMAGE, i[1]))
        potential_new_nodes.append(TextNode(sections[-1], TextType.TEXT))
        for potential_node in potential_new_nodes:
            if (potential_node.text_type == TextType.TEXT) and (potential_node.text == ""):
                continue
            else:
                new_nodes.append(potential_node)
    return new_nodes