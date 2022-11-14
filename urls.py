from django.urls import path
from . import apiREST

urlpatterns = [
    path('ping', apiREST.Ping.as_view()),
    path('category', apiREST.CategoryAL.as_view()),
    path('city', apiREST.CityAL.as_view()),
    # path('city/<str:pk>', apiREST.CityRGUD.as_view()),
    path('search-requests/rpc/accordance-search-requests', apiREST.AccordanceSearchRequestsP.as_view()),
    # path('search-requests', apiREST.SearchRequestsView.as_view()),
    # path('search-requests/<str:pk>', apiREST.SearchRequestsRGUD.as_view()),
]
