from django.urls import path
from . import routes
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('search-rooms',csrf_exempt(routes.search_rooms), name="search_rooms")
]