from textnode import TextType, TextNode

def split_node_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        potential_new_nodes = node.text.split(delimiter)
        formatted_nodes = []
        if len(potential_new_nodes) % 2 == 0:
            raise Exception("Invalid Markdown Syntax, No second delimiter")
        for i in range(len(potential_new_nodes)):
            if potential_new_nodes[i] == "":
                continue
            if i % 2 == 0:
                formatted_nodes.append(TextNode(potential_new_nodes[i], TextType.TEXT))
            else:
                formatted_nodes.append(TextNode(potential_new_nodes[i], text_type))
        new_nodes.extend(formatted_nodes)
    return new_nodes


