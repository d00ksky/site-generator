import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        
    def test_url(self):
        node = TextNode("This is a text node", "bold", "https://www.google.com")
        self.assertEqual(node.url, "https://www.google.com")
    
    def test_repr(self):
        node = TextNode("This is a text node", "bold", "https://www.google.com")
        self.assertEqual(repr(node), "Text: This is a text node, Type: bold, URL: https://www.google.com")
        
    def test_eq_not_textnode(self):
        node = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, "This is a text node")


if __name__ == "__main__":
    unittest.main()
