
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def inventory_list(request):
    inventory = [
        {
            "id": 1,
            "name": "Keyboard",
            "quantity": 15,
            "price": 49.99
        },
        {
            "id": 2,
            "name": "Mouse",
            "quantity": 25,
            "price": 19.99
        }
    ]

    return Response(inventory)
