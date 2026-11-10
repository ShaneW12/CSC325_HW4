from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status


class InventoryTests(APITestCase):

    def test_inventory_endpoint_returns_200(self):
        response = self.client.get('/api/inventory/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_inventory_endpoint_returns_items(self):
        response = self.client.get('/api/inventory/')

        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'Keyboard')


