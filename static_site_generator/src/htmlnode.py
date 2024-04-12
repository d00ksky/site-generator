class HTMLnode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        return " ".join([f'{key}="{value}"' for key, value in self.props.items()])
        
    def __repr__(self):
        return f"Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props}"
    
    
class LeafNode(HTMLnode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props=props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf nodes must have a value")
        if self.tag is None:
            return self.value
        props_html = self.props_to_html()
        space_if_props = " " if props_html else ""
        return f"<{self.tag}{space_if_props}{props_html}>{self.value}</{self.tag}>"
    
    
class ParentNode(HTMLnode):
    def __init__(self, children, tag=None, props=None):
        super().__init__(tag, children=children, props=props)
        
    def to_html(self):
        children_html = ""
        if self.tag is None:
            raise ValueError("Parent nodes must have a tag")
        if self.children is None:
            raise ValueError("Parent nodes must have children")
        else:
            for child in self.children:
                children_html += child.to_html()
                
        props_html = self.props_to_html()
        space_if_props = " " if props_html else ""
        return f"<{self.tag}{space_if_props}{props_html}>{children_html}</{self.tag}>"
    
        
        
        