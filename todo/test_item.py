from todo.item import Item

import unittest

class ItemTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_item_creation(self):
        item = Item()
        self.assertEqual(item.title, None)
        self.assertEqual(item.order, None)
        self.assertEqual(item.completed, False)

    def test_item_creation_with_title(self):
        item = Item("Title")
        self.assertEqual(item.title, "Title")
        self.assertEqual(item.order, None)
        self.assertEqual(item.completed, False)

    def test_item_creation_with_title_and_order(self):
        item = Item("Title", 1)
        self.assertEqual(item.title, "Title")
        self.assertEqual(item.order, 1)
        self.assertEqual(item.completed, False)

    def test_item_creation_with_title_and_order_and_completed(self):
        item = Item("Title", 1, True)
        self.assertEqual(item.title, "Title")
        self.assertEqual(item.order, 1)
        self.assertEqual(item.completed, True)

    def test_item_toString(self):
        item = Item("Title", 1, True)
        self.assertEqual(str(item), "Item(title=Title, order=1, completed=True)")

if __name__ == '__main__':
    unittest.main()
