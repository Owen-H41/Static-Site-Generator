from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict | None=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("No Tag")
        if not self.children:
            raise ValueError("No Children")
        html_string = f'<{self.tag}{self.props_to_html()}>'
        for child in self.children:
            html_string = html_string + child.to_html()
        return html_string + f'</{self.tag}>'