from django.db import models
from django.utils.translation import ugettext_lazy as _


class Account(models.Model):

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    name = models.CharField(_('Имя'), max_length=255)
    position = models.CharField(_('Должность'), max_length=255)
    city = models.CharField(_('Город'), max_length=255)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Task(models.Model):

    class Meta:
        verbose_name = _('Задача')
        verbose_name_plural = _('Задачи')

    name = models.CharField(_('Название'), max_length=255)
    description = models.TextField(_('Описание'))
    performer_mtm = models.ManyToManyField(
        Account,
        through='AccountTask',
        through_fields=('task', 'performer'),
        related_name='tasks',
    )
    reviewer_mtm = models.ManyToManyField(
        Account,
        through='AccountTask',
        through_fields=('task', 'reviewer'),
        related_name='verifiable',
    )

    def __str__(self):
        return self.name


class AccountTask(models.Model):
    class Meta:
        unique_together = (('performer', 'task'), )

    performer = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='performer',
        verbose_name=_('Исполняющий'),
    )
    reviewer = models.ForeignKey(
        Account,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reviewers',
        verbose_name=_('Ответственный'),
    )
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f'<AccountTask task:{self.task_id} performer:{self.performer_id}>'
