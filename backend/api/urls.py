from django.urls import path
from .views import HelloWorldView, OddNumbersView

urlpatterns = [
    path('hello-world/', HelloWorldView.as_view(), name='hello-world'),
    path('odd-numbers/', OddNumbersView.as_view(), name='odd-numbers'),
]
