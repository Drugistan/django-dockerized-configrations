# orders/views.py
import os

from django.http import FileResponse
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core import settings
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from account.permissions import IsClient
from .tasks import generate_user_credentials



class OrderCreateListView(APIView):
    permission_classes = [IsAuthenticated, IsClient]

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            order = serializer.save()
            generate_user_credentials.delay(order.id, request.user.username, request.user.email)
            download_url = reverse('order-credential-download', args=[order.id])
            message = {
                "data": serializer.data,
                "file": download_url
            }
            return Response(message, status=201)
        return Response(serializer.errors, status=400)

class OrderCredentialDownloadView(APIView):
    permission_classes = [IsAuthenticated, IsClient]

    def get(self, request, pk):
        file_path = os.path.join(settings.MEDIA_ROOT, f"order_credentials_{pk}.csv")
        return FileResponse(open(file_path, "rb"), as_attachment=True, filename=f"order_{pk}_credentials.csv")