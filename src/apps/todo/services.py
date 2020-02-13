from apps.todo.exceptions import TaskAlreadyAssigned, AccountTaskDoesNotExist
from apps.todo.models import AccountTask


class AccountService:

    @classmethod
    def _get_account_task_object(cls, **kwargs) -> AccountTask:
        try:
            obj = AccountTask.objects.get(**kwargs)
        except AccountTask.DoesNotExist:
            raise AccountTaskDoesNotExist
        return obj

    @classmethod
    def _update_object(cls, obj: AccountTask, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(obj, k, v)
        obj.save()

    @classmethod
    def assign_task(cls, task_id: int, user_id: int) -> None:
        try:
            cls._get_account_task_object(task_id=task_id, performer_id=user_id)
        except AccountTaskDoesNotExist:
            obj = AccountTask()
            cls._update_object(obj=obj, task_id=task_id, performer_id=user_id)
        else:
            raise TaskAlreadyAssigned

    @classmethod
    def assign_reviewer(cls, task_id: int, performer_id: int, reviewer_id: int):
        obj = cls._get_account_task_object(performer_id=performer_id, task_id=task_id)
        cls._update_object(obj, reviewer_id=reviewer_id)
