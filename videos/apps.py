from django.apps import AppConfig


class VideoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'videos'
    
    def ready(self):
        import videos.signals
        
        
    
    
        
    
