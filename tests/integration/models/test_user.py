from models.user import UserModel
from tests.base_test import BaseTest


class UserTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            user = UserModel('test', 'password')

            self.assertIsNone(UserModel.find_by_username('test'),
                              'Found user with username test, expected none.')
            self.assertIsNone(UserModel.find_by_id(1),
                              'Found user with user_id 1, expected none')
            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_username('test'),
                                 'Did not find a user with username test, after writing to db')
            self.assertIsNotNone(UserModel.find_by_id(1),
                                 'Did not find a user with user_id 1, after writing to db')
