from django.apps import AppConfig


class FinalProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_fp'

    def ready(self):
        import django_fp.signals

