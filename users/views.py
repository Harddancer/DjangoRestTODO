from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import Users
from .serializers import UserModelSerializer
from rest_framework.permissions import IsAuthenticated


class UserModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserModelSerializer
    queryset = Users.objects.all()


class UserModelLimitedViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, GenericViewSet
):
    serializer_class = UserModelSerializer
    queryset = Users.objects.all()
