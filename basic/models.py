from django.db import models

# Create your models here.
class AVItem(models.Model):
    item_title = models.CharField(max_length=100, unique=False)

    class Meta:
        ordering=('item_title',)

    def __str__(self):
        return self.item_title
