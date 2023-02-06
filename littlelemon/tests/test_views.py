from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(title="Ice Cream", price=5.00, inventory=10)
        Menu.objects.create(title="Cheese Cake", price=10.00, inventory=10)
        Menu.objects.create(title="Cup Cake", price=2.00, inventory=10)

    def test_getall(self):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        response = self.client.get('/menu/')

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)
