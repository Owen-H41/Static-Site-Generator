from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str, props: dict | None=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("No Value")
        if self.tag == None:
            return self.value
        return "<" + self.tag + f'{self.props_to_html()}' + ">" + self.value + "</" + self.tag + ">"
    
    def __repr__(self):
        return f"LeafNode(Tag={self.tag}, Value={self.value}, Props={self.props_to_html()})"