from django.contrib.contenttypes.models import ContentType
from .models import Action

# The create_action() function allows you to create actions that optionally include
# a target object. You can use this function anywhere in your code as a shortcut to
# add new actions to the activity stream.
def create_action(user, verb, target=None):
    action = Action(user=user, verb=verb, target=target)
    action.save()