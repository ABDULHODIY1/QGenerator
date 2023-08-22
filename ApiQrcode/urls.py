from django.urls import path
from .views import QRCodeUpdateAPIView, QRCodeDeleteAPIView,QRCodeGenerateAPIView

urlpatterns = [
    # ...
    path('generate-qr/', QRCodeGenerateAPIView.as_view(), name='generate-qr'),
    path('update-qr/<int:pk>/', QRCodeUpdateAPIView.as_view(), name='update-qr'),
    path('delete-qr/<int:pk>/', QRCodeDeleteAPIView.as_view(), name='delete-qr'),
    # ...
]
