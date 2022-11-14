from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from pullgerReflection.org__bbb import models
from pullgerReflection.org__bbb import apiR
from pullgerReflection.org__bbb__REST import serializers

from .general import CustomPaginator


from pullgerInternalControl.pullgerReflection.REST.logging import logger


class AccordanceSearchRequestsP(generics.GenericAPIView,
                                mixins.ListModelMixin,
                                mixins.CreateModelMixin):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPaginator
    http_method_names = ('post',)
    # queryset = models.People.objects.get_all_persons()

    def post(self, request, *args, **kwargs):
        content = {
            'status': '',
            'message': None,
            'data': None,
        }
        # self.serializer_class = serializers.PeopleModifySerializer
        try:
            return_response = apiR.accordance_search_requests()
            # returnResponse = self.create(request, *args, **kwargs)
        except BaseException as e:
            logger.critical(f"Error on executing request [{str(request)}] execute 'self.list': {str(e)}")

            content['status'] = "error"
            content['message'] = "Internal server error."
            content['data'] = None
            status_response = status.HTTP_500_INTERNAL_SERVER_ERROR
        else:
            content['status'] = "success"
            content['message'] = f"Processed elements [{str(return_response)}]"
            status_response = status.HTTP_201_CREATED

        return Response(content, status=status_response)
