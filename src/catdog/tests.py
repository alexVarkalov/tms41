from unittest import mock

from django.test import TestCase


class HomeTest(TestCase):
    def test_home(self):
        result = self.client.get('/home/')
        self.assertEqual(result.status_code, 200)

    def test_home_post(self):
        data = {
            'button': 'I love cats!',
        }
        with mock.patch('catdog.views.get_cat_url', return_value='Google.com'):
            result = self.client.post('/catdog/get_image/', data=data)
        animal_image_data = self.client.session['animal_image_data']
        self.assertEqual(result.status_code, 200)
        self.assertEqual(animal_image_data['species'], 'Cat')
