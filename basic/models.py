from django.db import models

# Create your models here.
class AVItem(models.Model):
    #ids
    uid = models.CharField(max_length=15, unique=True, default = None)
    original_id = models.CharField(max_length=15, unique=False, default = '')
    collection_id = models.CharField(max_length=15, unique=False, default = '')

    # titles
    item_title = models.CharField(max_length=100, unique=False, default = '')
    series_title = models.CharField(max_length=100, unique=False,default = '')
    episode_title = models.CharField(max_length=100, unique=False,default = '')

    # numbers
    can_number = models.CharField(max_length=100, unique=False,default = '')
    original_can_number = models.CharField(max_length=100, unique=False,default = '')
    call_number = models.CharField(max_length=100, unique=False, default = '')

    # citation
    date_created = models.CharField(max_length=100, unique=False,default = '')
    credits = models.CharField(max_length=100, unique=False,default = '')

    # description
    description = models.CharField(max_length=100, unique=False,default = '')
    location = models.CharField(max_length=100, unique=False,default = '')

    class Meta:
        ordering=('item_title',)

    def __str__(self):
        return self.item_title
