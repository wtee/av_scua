from django.db import models

# Create your models here.
class AVItem(models.Model):
    #ids
    uid = models.CharField(max_length=15, unique=True, default = None)
    original_id = models.CharField(max_length=15, unique=False, blank = True)
    collection_id = models.CharField(max_length=15, unique=False, blank = True)

    # titles
    item_title = models.CharField(max_length=100, unique=False, blank = True)
    series_title = models.CharField(max_length=100, unique=False,blank = True)
    episode_title = models.CharField(max_length=100, unique=False,blank = True)

    # numbers
    can_number = models.CharField(max_length=100, unique=False,blank = True)
    original_can_number = models.CharField(max_length=100, unique=False,blank = True)
    call_number = models.CharField(max_length=100, unique=False, blank = True)

    # citation
    date_created = models.CharField(max_length=100, unique=False,blank = True)
    credits = models.CharField(max_length=100, unique=False,blank = True)

    # description
    description = models.CharField(max_length=100, unique=False,blank = True)
    location = models.CharField(max_length=100, unique=False,blank = True)

    class Meta:
        ordering=('item_title',
                  'uid',
                  'original_id',
                  'collection_id',
                  )

    def __str__(self):
        return self.item_title
