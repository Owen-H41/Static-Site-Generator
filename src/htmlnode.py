class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        props_list = []
        for prop in self.props:
            props_list.append(f' {prop}="{self.props[prop]}"')
        prop_string = "".join(props_list)
        return prop_string

    def __repr__(self):
        return f"HTMLNode(Tag={self.tag}, Value={self.value}, Children={self.children}, Props={self.props_to_html()})"
