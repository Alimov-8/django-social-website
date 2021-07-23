from django.db import models

# Create your models here.
class Action(models.Model):
    user = models.ForeignKey('auth.User',
                            related_name='actions',
                            db_index=True,
                            on_delete=models.CASCADE,)
    verb = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True,
                                db_index=True)
    class Meta:
        ordering = ('-created',)