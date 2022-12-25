from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status

from data_loader.utils import get_test_data
from data_loader.test_container import TestContainer


test_container = TestContainer()


class UserCreationTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user1_data = get_test_data('users.json')['users']['user1']
        cls.first_name = cls.user1_data['first_name']
        cls.last_name = cls.user1_data['last_name']
        cls.username = cls.user1_data['username']
        cls.password = cls.user1_data['password']
        cls.email = cls.user1_data['email']

    def test_create_user(self):
        c = APIClient()
        data = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'password2': self.password
        }
        c.post(reverse_lazy('sign-up'), data)
        user = get_user_model().objects.get(first_name=self.first_name)
        assert user.last_name == self.last_name
        assert user.username == self.username
        assert user.email == self.email

    def test_wrong_password(self):
        c = APIClient()
        data = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'password2': f'{self.password}%'
        }
        response = c.post(reverse_lazy('sign-up'), data)
        self.assertFalse(status.is_success(response.status_code))


class UserUpdateTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = test_container.create_user('user1')
        cls.user1_data = get_test_data('users.json')['users']['user1']
        cls.user2_data = get_test_data('users.json')['users']['user2']
        cls.first_name = cls.user1_data['first_name']
        cls.last_name = cls.user1_data['last_name']
        cls.username = cls.user2_data['username']
        cls.email = cls.user1_data['email']
        cls.password = cls.user1_data['password']
        cls.user3 = test_container.create_user('user3')

    def test_update_user(self):
        c = APIClient()
        c.force_authenticate(user=self.user)
        new_data = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'email': self.email,
            'subscribe_plan': 'Basic'
        }
        c.put(reverse_lazy('user', args=[self.user.id]), new_data)
        user = get_user_model().objects.get(first_name=self.first_name)
        assert user.last_name == self.last_name
        assert user.username == self.username
        assert user.email == self.email

        c.force_authenticate(user=self.user3)
        new_data.update({'username': 'username'})
        response = c.put(reverse_lazy('user', args=[self.user.id]), new_data)
        self.assertFalse(status.is_success(response.status_code))


class UserDeleteTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = test_container.create_user('user1')
        cls.user3 = test_container.create_user('user3')

    def test_delete_user(self):
        id = self.user.id
        c = APIClient()
        c.force_authenticate(user=self.user3)
        response = c.delete(reverse_lazy('user', args=[self.user.id]))
        self.assertFalse(status.is_success(response.status_code))

        c.force_authenticate(user=self.user)
        c.delete(reverse_lazy('user', args=[id]))
        assert not get_user_model().objects.filter(id=id).exists()


class UsersTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user1 = test_container.create_user('user1')
        cls.user2 = test_container.create_user('user2')

    def test_users(self):
        c = APIClient()
        c.force_authenticate(user=self.user1)
        response = c.get(reverse_lazy('users'))
        self.assertContains(response, self.user1.username)
        self.assertContains(response, self.user2.username)
