from django.test import TestCase

from apps.todo.models import Account, Task, AccountTask
from apps.todo.services import AccountService


class AccountServiceTest(TestCase):

    def test_assign_reviewer(self):
        account_obj = Account.objects.create(name='test', position='main', city='Moscow')
        task_obj = Task.objects.create(name='task', description='description')
        AccountTask.objects.create(task=task_obj, performer=account_obj)

        assert not account_obj.reviewers.exists()
        AccountService.assign_reviewer(task_id=task_obj.id, performer_id=account_obj.id, reviewer_id=account_obj.id)
        assert account_obj.reviewers.exists()
