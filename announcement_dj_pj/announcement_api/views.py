from django.shortcuts import render
from rest_framework import viewsets, filters, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import Ad, AdPicture
from .serializers import AdSerializer, AdListSerializer, AllFieldsListSerializer

class AdViewSetPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_number'
    max_page_size = 10

class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdViewSetPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price', 'created_at']


    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({'id': serializer.instance.id, 'status': 'success'}, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            return Response({'status': 'failure', 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            request_parameter = self.request.query_params.get('fields', None)
            if request_parameter:
                return AllFieldsListSerializer
            return AdListSerializer
        return AdSerializer