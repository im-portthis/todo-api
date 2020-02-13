from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.todo.models import Account, Task, AccountTask


class AccountSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id',
            'name',
            'position',
            'city',
            'is_admin',
        )


class AccountListSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'name', )


class TaskSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', )


class TaskListSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', )


class TaskExtraSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'reviewers', )

    reviewers = AccountListSerializerV1(source='reviewer_mtm', many=True)


class TaskPerformerSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'performers', )

    performers = AccountListSerializerV1(source='performer_mtm', many=True)


class AssignTaskSerializerV1(serializers.Serializer):
    task_id = serializers.IntegerField()

    def validate(self, attrs):
        try:
            Task.objects.get(id=attrs['task_id'])
        except Task.DoesNotExist:
            raise ValidationError('Задача с указанным id не найдена')
        return attrs


class AssignReviewerSerializerV1(serializers.Serializer):
    performer_id = serializers.IntegerField()
    task_id = serializers.IntegerField()
    reviewer_id = serializers.IntegerField()

    def validate(self, attrs):
        try:
            AccountTask.objects.get(
                performer_id=attrs['performer_id'],
                task_id=attrs['task_id'],
                reviewer_id=attrs['reviewer_id'],
            )
        except AccountTask.DoesNotExist:
            pass
        else:
            raise ValidationError('Ответственный уже назначен')


class AccountExtraSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'name', 'position', 'city', 'is_admin', 'tasks', )

    tasks = TaskExtraSerializerV1(many=True)
