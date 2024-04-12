import unittest
from htmlnode import HTMLnode

class TestHtmlNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLnode("p", "This is a paragraph")
        self.assertRaises(NotImplementedError, node.to_html)
    
    def test_props_to_html(self):
        node = HTMLnode("p", "This is a paragraph", props={"class": "paragraph"})
        self.assertEqual(node.props_to_html(), 'class="paragraph"')

    def test_leaf_node(self):
        from htmlnode import LeafNode
        node = LeafNode("p", "This is a paragraph", props={"class": "paragraph"})
        # Capture the output of the method
        actual_output = node.to_html()
        # Optionally, print the output for debugging or inspection purposes
        print(f'Actual output: {actual_output}')
        # Perform the assertion using the captured output
        self.assertEqual(actual_output, '<p class="paragraph">This is a paragraph</p>')

    def test_leaf_node_no_tag(self):
        from htmlnode import LeafNode
        node = LeafNode(value="This is a paragraph", props={"class": "paragraph"})
        actual_output = node.to_html()
        print(f'Actual output: {actual_output}')
        self.assertEqual(actual_output, 'This is a paragraph')
        
    def test_leaf_node_no_value(self):
        from htmlnode import LeafNode
        node = LeafNode("p", props={"class": "paragraph"})
        self.assertRaises(ValueError, node.to_html)
        
        
#   def test_parent_node(self):
#       from htmlnode import ParentNode, LeafNode
#       node = ParentNode("div", [LeafNode("p", "This is a paragraph"), LeafNode("p", "This is another paragraph")], props={"class": "container"})
#       actual_output = node.to_html()
#       print(f'Actual output: {actual_output}')
#       self.assertEqual(actual_output, '<div class="container"><p>This is a paragraph</p><p>This is another paragraph</p></div>')
        
    def test_parent_node_no_tag(self):
        from htmlnode import ParentNode, LeafNode
        node = ParentNode([LeafNode("p", "This is a paragraph"), LeafNode("p", "This is another paragraph")], props={"class": "container"})
        self.assertRaises(ValueError, node.to_html)
        
    def test_parent_node_no_children(self):
        from htmlnode import ParentNode
        node = ParentNode("div", props={"class": "container"})
        self.assertRaises(ValueError, node.to_html)
        
    def test_parent_node(self):
        from htmlnode import ParentNode, LeafNode
        # Initialize children correctly in a list with props
        children = [
            LeafNode("p", "This is a paragraph", props={"class": "paragraph"}),
            LeafNode("p", "This is another paragraph", props={"class": "paragraph"})
        ]
        # Create ParentNode with corrected children
        node = ParentNode(children, tag="div", props={"class": "container"})
        actual_output = node.to_html()
        print(f'Actual output: {actual_output}')
        self.assertEqual(actual_output, '<div class="container"><p class="paragraph">This is a paragraph</p><p class="paragraph">This is another paragraph</p></div>')

    def test_parent_node2(self):
        from htmlnode import ParentNode, LeafNode
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ]
        node = ParentNode(children, tag="p")
        actual_output = node.to_html()
        print(f'Actual output: {actual_output}')
        self.assertEqual(actual_output, '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')


if __name__ == "__main__":
    unittest.main(verbosity=2)