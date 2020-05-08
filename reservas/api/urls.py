"""tennisconcierge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (
    ReservasListAPIView,
    ReservaAPIView,
    ReservasCreateAPIView
)

def method_dispatch(**table):
    def invalid_method(request, *args, **kwargs):
        logger.warning('Method Not Allowed (%s): %s', request.method, request.path,
            extra={
                'status_code': 405,
                'request': request
            }
        )
        return HttpResponseNotAllowed(table.keys())

    def d(request, *args, **kwargs):
        handler = table.get(request.method, invalid_method)
        return handler(request, *args, **kwargs)
    return d

urlpatterns = [
    # path('',  ReservasListAPIView.as_view(), name='list'),
    # path('/<int:id>',  ReservasRetrieveAPIView.as_view(), name='retrieve'),
    # path('/<int:id>/update',  ReservasUpdateAPIView.as_view(), name='update'),
    # path('/<int:id>/destroy',  ReservasDestroyAPIView.as_view(), name='destroy'),
    # path('/create',  ReservasCreateAPIView.as_view(), name='create'),
    path('', method_dispatch(
            GET = ReservasListAPIView.as_view(),
            POST = ReservasCreateAPIView.as_view()
        ),
        name='/reserva'),
    path('/<int:id>',  method_dispatch(
            GET = ReservaAPIView.as_view(),
            PUT = ReservaAPIView.as_view(),
            DELETE = ReservaAPIView.as_view()
        ), name='/reserva/id')
]
