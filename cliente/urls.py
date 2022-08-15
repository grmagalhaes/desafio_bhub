from django.urls import path

from .views import Status

status = Status.as_view({"get": "get"})

urlpatterns = [
    path("criar/", status, name="status"),
    path("status", Status.as_view({"get": "get"}), name="status"),
]

# if settings.DEBUG:
#    urlpatterns += static(r'/favicon.ico', document_root='static/favicon.ico')
