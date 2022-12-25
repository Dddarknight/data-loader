from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse_lazy
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status

from data_loader.utils import get_picture
from data_loader.test_container import TestContainer
from data_loader.resources.models import UploadedImage


test_container = TestContainer()


class UserCreationTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = test_container.create_user('user1')
        cls.image = SimpleUploadedFile(
            name='test_picture.jpeg',
            content=get_picture('test_picture.jpeg'))

    def test_image(self):
        image = UploadedImage.objects.create(
            image=self.image,
            owner=self.user
        )
        id = image.id
        self.user.subscribe_plan = 'Basic'
        self.user.save()
        c = APIClient()
        c.force_authenticate(user=self.user)
        response = c.get(reverse_lazy('thumbnail200', args=[id]))
        self.assertTrue(status.is_success(response.status_code))
        response = c.get(reverse_lazy('thumbnail400', args=[id]))
        self.assertFalse(status.is_success(response.status_code))
        response = c.get(reverse_lazy('original', args=[id]))
        self.assertFalse(status.is_success(response.status_code))

        self.user.subscribe_plan = 'Premium'
        self.user.save()
        c.force_authenticate(user=self.user)
        response = c.get(reverse_lazy('thumbnail200', args=[id]))
        self.assertTrue(status.is_success(response.status_code))
        response = c.get(reverse_lazy('thumbnail400', args=[id]))
        self.assertTrue(status.is_success(response.status_code))
        response = c.get(reverse_lazy('original', args=[id]))
        self.assertTrue(status.is_success(response.status_code))

        self.user.subscribe_plan = 'Enterprise'
        self.user.save()
        c.force_authenticate(user=self.user)
        response = c.get(reverse_lazy('thumbnail200', args=[id]))
        self.assertTrue(status.is_success(response.status_code))
        response = c.get(reverse_lazy('thumbnail400', args=[id]))
        self.assertTrue(status.is_success(response.status_code))
        response = c.get(reverse_lazy('original', args=[id]))
        self.assertTrue(status.is_success(response.status_code))
