from django.apps import AppConfig


class TwitappConfig(AppConfig):
    name = 'twitapp'

    def ready(self):
        import twitapp.signals
