from django.urls import path

from .views import ClientViewSet

create = ClientViewSet.as_view({"post": "create"})

urlpatterns = [
    path("create", create, name="create"),
]

# if settings.DEBUG:
#    urlpatterns += static(r'/favicon.ico', document_root='static/favicon.ico')
