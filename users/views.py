from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import Users
from .serializers import UserModelSerializer,UserModelSerializerV2
from rest_framework.permissions import IsAuthenticated


class UserModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserModelSerializer
    queryset = Users.objects.all()
    def get_serializer_class(self):
        if self.request.version == '2.0':
            return UserModelSerializerV2
        return UserModelSerializer


class UserModelLimitedViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, GenericViewSet
):
    serializer_class = UserModelSerializer
    queryset = Users.objects.all()
