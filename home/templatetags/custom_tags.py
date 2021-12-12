from django import template
from home.models import Notificatiion

register= template.Library()

@register.inclusion_tag('show_notifications.html', takes_context=True)

def show_notifications(context):
    request_user= context['request'].user
    noti= Notificatiion.objects.filter(to_user=request_user).exclude(user_has_seen=True).order_by('-date')
    return {
        'noti':noti,
    }