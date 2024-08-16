from django.urls import path
from .views import HelloWorldView, OddNumbersView, PrimeNumberView

urlpatterns = [
    path('hello-world/', HelloWorldView.as_view(), name='hello-world'),
    path('odd-numbers/', OddNumbersView.as_view(), name='odd-numbers'),
    path('prime-number/', PrimeNumberView.as_view(), name='prime-number'),
]
