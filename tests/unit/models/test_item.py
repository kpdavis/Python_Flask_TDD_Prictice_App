from unittest import TestCase

from models.item import ItemModel


class ItemTest(TestCase):
    def test_init_item(self):
        item = ItemModel('Test Item', 5.55)

        self.assertEqual(item.name,
                         'Test Item', 'Name of item not equal to constructor argument')
        self.assertEqual(item.price, 5.55,
                         'Price not equal to constructor argument')


    def test_json(self):
        item = ItemModel('Test Item', 5.55)
        expected = {
            'name': 'Test Item',
            'price': 5.55
        }

        self.assertEqual(item.json(), expected,
                         'The JSON export is Incorredt. Receiced {}, '
                         'expected {} '.format(item.json(), expected))

