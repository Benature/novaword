from django import template

from users.models import UserGroup, UserProfile

register = template.Library()


@register.filter(name="is_teacher")
def is_teacher(value):
    user_id = value
    if UserProfile.objects.filter(id=user_id, is_staff=True).count():
        return True
    if UserGroup.objects.filter(user_id=user_id, role__gt=1).count():
        return True
    return False

