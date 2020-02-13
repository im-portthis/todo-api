from django.contrib.auth import get_user_model
from django.db import migrations


def create_test_user(apps, schema_editor):
    User = get_user_model()
    user = User.objects.create(username='test')
    user.set_password('test')
    user.is_staff = True
    user.is_superuser = True
    user.save()


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_test_user),
    ]
