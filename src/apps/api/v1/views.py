from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from apps.todo.exceptions import Error
from apps.todo.models import Account, Task
from apps.todo.services import AccountService
from .filters import AccountFilterV1, TaskFilterV1
from .serializers import (
    AccountSerializerV1,
    AccountListSerializerV1,
    TaskSerializerV1,
    TaskListSerializerV1,
    AssignTaskSerializerV1,
    AssignReviewerSerializerV1,
    AccountExtraSerializerV1,
    TaskPerformerSerializerV1,
)


class AccountViewSetV1(viewsets.ModelViewSet):
    queryset = Account.objects.all().order_by('-id')
    serializer_class = AccountSerializerV1
    filter_backends = (
        filters.SearchFilter,
        DjangoFilterBackend
    )
    search_fields = ('^position', )
    filter_class = AccountFilterV1

    def get_serializer_class(self):
        if self.action == 'list':
            return AccountListSerializerV1
        if self.action == 'retrieve' and self.request.query_params.get('extra', False):
            return AccountExtraSerializerV1
        return super().get_serializer_class()

    @action(detail=True, methods=['post'], url_path='assign-task')
    def assign_task(self, request, pk):
        serializer = AssignTaskSerializerV1(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            AccountService.assign_task(
                user_id=pk,
                task_id=serializer.validated_data['task_id'],
            )
        except Error as err:
            raise ValidationError(err.message)
        return Response({'operation': 'success'})

    @action(detail=True, methods=['post'], url_path='assign-reviewer')
    def assign_reviewer(self, request, pk):
        serializer = AssignReviewerSerializerV1(data={**request.data, 'reviewer_id': pk})
        serializer.is_valid(raise_exception=True)
        try:
            AccountService.assign_reviewer(
                reviewer_id=pk,
                performer_id=serializer.validated_data['performer_id'],
                task_id=serializer.validated_data['task_id'],
            )
        except Error as err:
            raise ValidationError(err.message)
        return Response({'operation': 'success'})


class TaskViewSetV1(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializerV1
    filter_backends = (
        filters.SearchFilter,
        DjangoFilterBackend
    )
    filter_class = TaskFilterV1
    search_fields = ('^name',)

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskListSerializerV1
        if self.action == 'retrieve' and self.request.query_params.get('extra', False):
            return TaskPerformerSerializerV1
        return super().get_serializer_class()
