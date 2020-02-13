from rest_framework.routers import DefaultRouter

from apps.api.v1.views import AccountViewSetV1, TaskViewSetV1

router = DefaultRouter()
router.register('accounts', AccountViewSetV1)
router.register('tasks', TaskViewSetV1)
