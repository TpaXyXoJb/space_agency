from django.db import models
from filer.fields.image import FilerImageField


class Picture(models.Model):
    name = models.CharField(max_length=255)
    custom_ordering = models.PositiveIntegerField(default=0, null=False, blank=False)
    image = FilerImageField(blank=True, null=True, on_delete=models.CASCADE, related_name='picture_image')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['custom_ordering']
