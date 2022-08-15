from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from cliente.utils import hardening_header
from desafio.healthcheck import HealthCheckMiddleware


class Status(ViewSet):
    authentication_classes = []

    def get(self, request):
        check = HealthCheckMiddleware(request)
        return Response(
                dict(
                    healthz=check.healthz(request).content,
                    readiness=check.readiness(request).content
                ),
                headers=hardening_header(),
        )