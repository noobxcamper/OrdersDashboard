from django.shortcuts import HttpResponse
from enum import IntEnum
import json

class ErrorCodes(IntEnum):
    ORDER_EXISTS = 1001

def order_exists_error(id):
    dict = {
        "error": {
                "error_code": ErrorCodes.ORDER_EXISTS,
                "error_message": "Order already exists"
        },
        "order": {
                "order_id": int(id)
        }
    }

    return HttpResponse(json.dumps(dict), status=200, content_type="application/json")