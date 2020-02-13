from rest_framework import serializers

from apps.todo.models import Account, Task


class AccountSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class AccountListSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'name', )


class TaskSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskListSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', )
