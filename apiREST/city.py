from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from pullgerReflection.org__bbb import models

from .general import CustomPaginator
from pullgerReflection.org__bbb__REST import serializers

from pullgerInternalControl import pIC_pR
from pullgerInternalControl.pullgerReflection.REST.logging import logger


class CityAL(generics.GenericAPIView,
             mixins.ListModelMixin,
             mixins.CreateModelMixin):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPaginator
    queryset = models.City.objects.get_all()

    def get(self, request, *args, **kwargs):
        content = {
            'status': '',
            'message': None,
            'data': None,
        }

        self.serializer_class = serializers.CityListSerializer
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
        self.serializer_class = serializers.CityListSerializer
        try:
            param_force = str(request.query_params.get("force")).lower() in ('true', 1)

            prop_id_iso_country = request.data.get("id_iso_country")
            prop_id_iso_state = request.data.get("id_iso_state")

            prop_id_name = request.data.get("id_name")
            prop_id_name_city = request.data.get("id_name_city")
            if prop_id_name_city is not None:
                prop_id_name_issue = prop_id_name_city
            else:
                prop_id_name_issue = prop_id_name

            prop_description = request.data.get("description")

            country = models.Country.objects.get_by_keys(id_iso_country=prop_id_iso_country, force=param_force)
            state = models.State.objects.get_by_keys(id_iso_state=prop_id_iso_state, country=country, force=param_force)

            result = models.City.add(
                id_name_city=prop_id_name_issue,
                description=prop_description,
                country=country,
                state=state
            )

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
