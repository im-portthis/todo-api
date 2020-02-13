import django_filters

from apps.todo.models import Account, Task


class AccountFilterV1(django_filters.FilterSet):
    class Meta:
        model = Account
        fields = {
            'position': ['exact'],
        }


class TaskFilterV1(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = {
            'name': ['exact'],
        }
