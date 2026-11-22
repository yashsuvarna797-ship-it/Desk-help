from . import models

def get_notifications(request):
    if request.user.is_authenticated:
        notifications = models.Notification.objects.filter(recipient=request.user)
        return {'notifications':notifications[:10]}
    return {
        'notifications':[],
    }