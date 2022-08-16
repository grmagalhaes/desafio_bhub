from django.urls import path

from .views import ClientViewSet

create = ClientViewSet.as_view({"post": "create"})
read = ClientViewSet.as_view({"get": "read"})

urlpatterns = [
    path("create", create, name="create"),
    path("read", read, name="read"),
]

# if settings.DEBUG:
#    urlpatterns += static(r'/favicon.ico', document_root='static/favicon.ico')
