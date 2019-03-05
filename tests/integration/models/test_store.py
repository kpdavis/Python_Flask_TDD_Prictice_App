from models.item import ItemModel
from models.store import StoreModel

from tests.base_test import BaseTest

class StoreTest(BaseTest):
    def test_create_store_items_empty(self):
        store = StoreModel('test')

        self.assertListEqual(store.items.all(), [],
                             'the store\'s items length was not 0 though no items were added')


    def test_crud(self):
        with self.app_context():
            store = StoreModel('test')

            self.assertIsNone(StoreModel.find_by_name('test'),
                              'Found an store with name test , but expected not to.')

            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name('test'),
                                 'Did not find a store with name test, after writing to db')

            store.delete_from_db()

            self.assertIsNone(StoreModel.find_by_name('test'),
                              'Found an store with name test, but expected not to after deletion')

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test_store')
            item = ItemModel('test_item', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'test_item')

    def test_store_json(self):
        store = StoreModel('test')
        expected = {
            'name': 'test',
            'items': []
        }

        self.assertDictEqual(store.json(), expected)

    def test_store_item_json(self):
        with self.app_context():
            store = StoreModel('test_store')
            item = ItemModel('test_item', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            expected = {
                'name': 'test_store',
                'items': [{
                    'name': 'test_item',
                    'price': 19.99
                }]
            }

            self.assertDictEqual(store.json(), expected)
