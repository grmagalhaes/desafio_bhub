from django.urls import path

from .views import ClientViewSet, DadosBancariosViewSet

create = ClientViewSet.as_view({"post": "create"})
get = ClientViewSet.as_view({"get": "get"})
update = ClientViewSet.as_view({"put": "update"})
delete = ClientViewSet.as_view({"delete": "delete"})
list = ClientViewSet.as_view({"get": "list"})

add_account = DadosBancariosViewSet.as_view({"post": "add_account"})
remove_account = DadosBancariosViewSet.as_view({"delete": "remove_account"})

urlpatterns = [
    path("create", create, name="create"),
    path("get", get, name="get"),
    path("update", update, name="update"),
    path("delete", delete, name="delete"),
    path("list", list, name="list"),

    path("add_account", add_account, name="add_account"),
    path("remove_account", remove_account, name="remove_account"),
]

# if settings.DEBUG:
#    urlpatterns += static(r'/favicon.ico', document_root='static/favicon.ico')
