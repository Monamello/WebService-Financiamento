from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import Consulta
from .serializers import ConsultaSerializer
from rest_framework import status
from rest_framework.response import Response



class ConsultaCreateAPIView(CreateAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            consulta = Consulta(serializer.validated_data)
            return Response(consulta.lista_parcelas)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
