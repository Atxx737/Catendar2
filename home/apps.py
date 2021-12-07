from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
    
    def ready(self):
        import home.signals
    
class UsersConfig(AppConfig):
    name = 'users'

    # add this function
    def ready(self):
        from . import signals
        from . import receivers

# users/__init__.py 
default_app_config = 'users.apps.UsersConfig'
