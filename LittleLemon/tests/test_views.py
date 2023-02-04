from django.test import TestCase, RequestFactory
from restaurant.models import Menu
from restaurant.views import MenuItemView
from restaurant.serializers import MenuSerializer

items = [
    {
        'title' : 'Sushi',
        'price' : 7.25,
        'inventory' : 5,
    },
    {
        'title' : 'Gyoza',
        'price' : 4.95,
        'inventory' : 3,
    },
    {
        'title' : 'Edamame',
        'price' : 3.95,
        'inventory' : 4,
    },
]

class MenuViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        for item in items:
            Menu.objects.create(
                title=item.title,
                price=item.price,
                inventory=item.inventory
            )

    def test_getall(self):
        menuitems = Menu.objects.all()
        serialized_menuitems = MenuSerializer(menuitems, many=True)
        request = self.factory.get('restaurant/menu/')
        response = MenuItemView.as_view()(request)

        self.assertEqual(response.data, serialized_menuitems.data)