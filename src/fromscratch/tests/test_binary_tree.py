import unittest
from ..binary_tree import IntBinaryTree


class TestIntBinaryTree(unittest.TestCase):
    def setUp(self):
        """
        Set up before each test runs.
        """
        self.tree = IntBinaryTree(5)

    def test_key_string_raise_valueerror(self):
        with self.assertRaises(ValueError):
            self.tree.insert("")

    def test_init_tree(self):
        no_init_tree = IntBinaryTree()
        no_init_tree.insert(5)
        self.assertEqual(self.tree, no_init_tree)


if __name__ == '__main__':
    unittest.main()
