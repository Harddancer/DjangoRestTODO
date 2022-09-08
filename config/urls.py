"""config URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from todoapp.views import ProjectModelViewSet, TodoModelViewSet
from users.views import UserModelLimitedViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from graphene_django.views import GraphQLView




schema_view = get_schema_view(
    openapi.Info(
        title="TODO",
        default_version='0.1',
        description="Documentation to out project",
        contact=openapi.Contact(email="yamamotod@mail.ru"),
        license=openapi.License(name="MIT License"),
)
)

router = DefaultRouter()
# router.register("users", UserModelViewSet)
router.register("users", UserModelLimitedViewSet)
router.register("project", ProjectModelViewSet)
router.register("todo", TodoModelViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
    path("api-auth-token/", obtain_auth_token),
    path('swagger', schema_view.with_ui()),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
    re_path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui()),
]
