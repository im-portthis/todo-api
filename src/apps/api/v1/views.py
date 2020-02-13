from rest_framework import viewsets

from apps.todo.models import Account, Task
from .serializers import (
    AccountSerializerV1,
    AccountListSerializerV1,
    TaskSerializerV1,
    TaskListSerializerV1,
)


class AccountViewSetV1(viewsets.ModelViewSet):
    queryset = Account.objects.all().order_by('-id')
    serializer_class = AccountSerializerV1

    def get_serializer_class(self):
        if self.action == 'list':
            return AccountListSerializerV1
        return super().get_serializer_class()


class TaskViewSetV1(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializerV1

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskListSerializerV1
        return super().get_serializer_class()
