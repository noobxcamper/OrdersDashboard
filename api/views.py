from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.models import Order
from .serializers import OrderSerializer

# Create
@api_view(['POST'])
def create_new_order(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)

    return Response(serializer.data)

# Read
@api_view(['GET'])
def get_all_orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_order_status(request, id):
    order = Order.objects.get(submission_id=id)
    serializer = OrderSerializer(order)

    return Response(serializer.data)

# Update
@api_view(['PUT'])
def update_order(request, id):
    order = Order.objects.get(id=id)
    serializer = OrderSerializer(order, data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)
    else:
        return Response(status=404)

# Delete
@api_view(['DELETE'])
def delete_order(request, id):
    order = Order.objects.get(id=id)
    order.delete()

    return Response(status=204)