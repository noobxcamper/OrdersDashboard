from core import models

def does_order_exist(id):
    return models.Orders.objects.filter(id=id).exists()

def create_new_order(json_data):
    order = models.Orders()
    order.status = json_data['status']
    order.responder = json_data['responder']
    order.submission_date = json_data['submission_date']
    order.department = json_data['department']
    order.items = json_data['items']
    order.price = json_data['price']
    order.quantity = json_data['quantity']
    order.ship_to = json_data['ship_to']
    order.hyperlink = json_data['hyperlink']

    order.save()