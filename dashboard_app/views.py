from django.shortcuts import render, redirect, reverse, HttpResponse
from core.models import Order
from core.auth import interactive_login, renew_token
from OrdersDashboard.settings import CLIENT_SECRET
from msal.oauth2cli.oidc import decode_id_token
import json, jwt

# Create your views here.
def index(request):
    context = Order.objects.all()
    return render(request, 'dashboard_app/index.html', context={'orders': context})

def view_order(request, order_id):
    context = Order.objects.get(id=order_id)
    return render(request, 'dashboard_app/order.html', context={'order': context})

def login(request):
    token = interactive_login()
    print(token)

    print(decode_id_token(token)['exp'])

    if token:
        return redirect('dashboard')
    else:
        return HttpResponse(status=405)
    
def refresh_token(request):
    token = renew_token()
    
    if token:
        next = request.POST['next']
        return redirect(next)
    else:
        # Change this with an error page later
        return HttpResponse(status=404)