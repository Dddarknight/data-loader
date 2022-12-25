from django.test import TestCase

from data_loader.users.models import User
from data_loader.utils import get_test_data


class TestContainer(TestCase):
    test_data_users = get_test_data('users.json')

    def create_user(self, user):
        return User.objects.create(
            first_name=self.test_data_users['users'][user]['first_name'],
            last_name=self.test_data_users['users'][user]['last_name'],
            username=self.test_data_users['users'][user]['username'],
            password=self.test_data_users['users'][user]['password'],
            email=self.test_data_users['users'][user]['email'])
