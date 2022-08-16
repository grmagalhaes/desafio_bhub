from django.urls import path

from .views import ClientViewSet

create = ClientViewSet.as_view({"post": "create"})
get = ClientViewSet.as_view({"get": "get"})
delete = ClientViewSet.as_view({"delete": "delete"})

urlpatterns = [
    path("create", create, name="create"),
    path("get", get, name="get"),
    path("delete", delete, name="delete"),
]

# if settings.DEBUG:
#    urlpatterns += static(r'/favicon.ico', document_root='static/favicon.ico')
