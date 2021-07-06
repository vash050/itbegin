from django.apps import AppConfig


class GroupAppConfig(AppConfig):
    name = 'signals'

    def ready(self):
        import signals.signals