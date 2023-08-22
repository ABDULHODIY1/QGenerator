from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import QRCode
from .serializers import QRCodeSerializer
import qrcode
from io import BytesIO
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
class QRCodeGenerateAPIView(APIView):
    def get(self, request):
        content = request.query_params.get('content')  # Ma'lumotni olish
        if content:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(content)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            response = HttpResponse(content_type="image/png")
            img.save(response, "PNG")
            return response
        return Response({"error": "Content parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
class QRCodeUpdateAPIView(APIView):
    def put(self, request, pk):
        try:
            qr_code = QRCode.objects.get(pk=pk)  # Ma'lumotni olish
        except QRCode.DoesNotExist:
            return Response({"error": "QR code not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = QRCodeSerializer(qr_code, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QRCodeDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            qr_code = QRCode.objects.get(pk=pk)  # Ma'lumotni olish
        except QRCode.DoesNotExist:
            return Response({"error": "QR code not found"}, status=status.HTTP_404_NOT_FOUND)

        qr_code.delete()  # Ma'lumotni o'chirish
        return Response(status=status.HTTP_204_NO_CONTENT)
