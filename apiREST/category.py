from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from pullgerReflection.org__bbb import models

from .general import CustomPaginator
from pullgerReflection.org__bbb__REST import serializers

from pullgerInternalControl.pullgerReflection.REST.logging import logger


class CategoryAL(generics.GenericAPIView,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPaginator
    queryset = models.Category.objects.get_all()

    def get(self, request, *args, **kwargs):
        content = {
            'status': '',
            'message': None,
            'data': None,
        }

        self.serializer_class = serializers.CategoryListSerializer
        try:
            returnResponse = self.list(request, *args, **kwargs)
        except BaseException as e:
            logger.critical(f"Error on executing request [{str(request)}] execute 'self.list': {str(e)}")

            content['status'] = 'error'
            content['message'] = 'Internal server error.'
            content['data'] = None
            statusResp = status.HTTP_500_INTERNAL_SERVER_ERROR

            returnResponse = Response(self.content, status=statusResp)

        return returnResponse

    def post(self, request, *args, **kwargs):
        content = {
            'status': '',
            'message': None,
            'data': None,
        }
        self.serializer_class = serializers.CategoryListSerializer
        try:
            # request.data.get("")
            result = models.Category.add(**request.data)
            # returnResponse = self.create(request, *args, **kwargs)
        except BaseException as e:
            logger.critical(f"Error on executing request [{str(request)}] execute 'self.list': {str(e)}")

            content['status'] = 'error'
            content['message'] = 'Internal server error.'
            content['data'] = None
            status_response = status.HTTP_500_INTERNAL_SERVER_ERROR
        else:
            content['status'] = 'success'
            content['message'] = ''
            status_response = status.HTTP_201_CREATED

        return Response(content, status=status_response)
