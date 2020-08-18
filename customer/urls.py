from django.urls import path
from .views import *

urlpatterns=[
    path('account/', Account, name='account'),
    path('reservation/', Reservation, name='reservation'),
    path('logout/', Logout, name='logout'),
    path('cart/', Cart, name='cart'),
    path('delete_order/<int:Oid>/', DeleteOrder, name='deleteOrder'),
]