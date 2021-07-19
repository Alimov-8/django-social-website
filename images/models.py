from django.db import models
from django.conf import settings 
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                related_name='images_created',
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='users/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True,
                                db_index=True)

    # The ManyToManyField fields provide a many-to-many manager that allows you to
    # retrieve related objects, such as image.users_like.all(), or get them from
    # a user object, such as user.images_liked.all().
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                            related_name='images_liked',
                                            blank=True)

    def __str__(self):
        return self.title

    # In the preceding code, the slugify() function provided by Django to
    # automatically generate the image slug for the given title when no slug is provided.
    # Then, save the object. By generating slugs automatically, users don't have
    # to manually enter a slug for each image.
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])  
    
