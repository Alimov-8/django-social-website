from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Image

@receiver(m2m_changed, sender=Image.users_like.through)
def users_like_changed(sender, instance, **kwargs):
    instance.total_likes = instance.users_like.count()
    instance.save()

    # Consider the following query to get images ordered according to their likes count:
    # from django.db.models import Count
    # (*) images_by_popularity = Image.objects.annotate(likes=Count('users_like')).order_by('-likes')
    # The preceding query can now be written as follows:
    # (* optimized) images_by_popularity = Image.objects.order_by('-total_likes')