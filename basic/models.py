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
    format_duration = models.TimeField(default="00:00:00")

    # choices
    MEDIA_CHOICES = (
        ('film', 'Film'),
        ('video', 'Video'),
        ('audio', 'Audio'),
    )
    media_type = models.CharField(max_length=7,
                                  choices=MEDIA_CHOICES,
                                  default='')

    STATUS_CHOICES = (
        ('on shelf', 'On Shelf'),
        ('conservation', 'Conservation'),
        ('vendor', 'Vendor'),
        ('loan', 'Loan'),
    )
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='')

    COPYRIGHT_CHOICES = (
        ('open', 'OPEN'),
        ('restricted', 'RESTRICTED'),
    )
    copyright = models.CharField(max_length=15, choices=COPYRIGHT_CHOICES, default='')

    GAUGE_CHOICES = (
        ('8mm', '8mm'),
        ('super 8mm', 'Super 8mm'),
        ('16mm', '16mm'),
        ('35mm', '35mm'),
        ('35/32mm', '35/32mm'),
    )
    gauge = models.CharField(max_length=15, choices=GAUGE_CHOICES, default='')

    FRAMERATE_CHOICES = (
        ('16 fps', '16 fps'),
        ('18 fps', '18 fps'),
        ('24 fps', '24 fps'),
    )
    frame_rate = models.CharField(max_length=15,
                                  choices = FRAMERATE_CHOICES,
                                  default='')

    COLOR_CHOICES = (
        ('color', 'COLOR'),
        ('black and white', 'BLACK AND WHITE'),
    )
    ADV_COLOR_CHOICES = (
        ('ektachrome', 'Ektachrome'),
        ('kodachrome', 'Kodachrome'),
        ('technicolor', 'Technicolor'),
        ('anscochrome', 'Anscochrome'),
        ('eco', 'Eco'),
        ('eastman', 'Eastman')
    )

    color = models.CharField(max_length=15,
                             choices = COLOR_CHOICES,
                             default='')
    adv_color = models.CharField(max_length=15,
                                 choices=ADV_COLOR_CHOICES,
                                 default='')

    copies = models.BooleanField(default=False)
    digital_preservation = models.BooleanField(default=False)
    anamorphic = models.BooleanField(default=False)
    clean = models.BooleanField(default=False)
    return_on_original_reel = models.BooleanField(default=False)
    mold = models.BooleanField(default=False)



    other_notes = models.CharField(max_length=200, unique=False, blank=True)
    lto_number = models.CharField(max_length=100, unique=False, blank=True)

    footage = models.CharField(max_length=100, unique=False, blank=True)

    ASPECT_RATIO_CHOICES = (
        ('1.18:1', '1.18:1'),
        ('1.33:1', '1.33:1'),
        ('1.37:1', '1.37:1'),
        ('1.66:1', '1.66:1'),
        ('1.85:1', '1.85:1'),
        ('2.35:1', '2.35:1'),
        ('2.39:1', '2.39:1'),
        ('2.59:1', '2.59:1'),
        ('2.66:1', '2.66:1'),
    )
    aspect_ratio = models.CharField(max_length=15,
                                    choices=ASPECT_RATIO_CHOICES,
                                    default='')

    SOUND_CHOICES = (
        ('sound', 'SOUND'),
        ('silent', 'SILENT'),
    )
    sound = models.CharField(max_length=15,
                             choices = SOUND_CHOICES,
                             default='')

    SOUND_CONTENT_CHOICES = (
        ('composite track', 'COMPOSITE TRACK'),
        ('sound content', 'SOUND CONTENT'),
    )
    sound_content_type = models.CharField(max_length = 25,
                                          choices = SOUND_CONTENT_CHOICES,
                                          default = '')

    SOUND_FIELD_CHOICES = (
        ('mono', 'MONO'),
        ('stero', 'STEREO'),
    )
    sound_field = models.CharField(max_length=7,
                                   choices = SOUND_FIELD_CHOICES,
                                   default='')

    RESOLUTION_CHOICES = (
        ('hd', 'HD'),
        ('2k', '2k'),
        ('4k', '4k'),
        ('5k', '5k'),
    )
    resolution = models.CharField(max_length=7,
                                  choices =  RESOLUTION_CHOICES,
                                  default = '')

    SAMPLE_ENCODING_CHOICES = (
        ('linear 10 bit', 'Linear 10 bit'),
        ('linear 16 bit', 'Linear 16 bit'),
        ('logarithmic 10 bit', 'Logarithmic 10 bit'),
    )
    sample_encoding = models.CharField(max_length=25,
                                       choices = SAMPLE_ENCODING_CHOICES,
                                       default = '')

    AD_STRIP_CHOICES = (
        ('0','0'),
        ('0.5','0.5'),
        ('1', '1'),
        ('1.5', '1.5'),
        ('2','2'),
        ('2,5', '2,5'),
        ('3', '3'),
    )
    ad_strip = models.CharField(max_length=7,
                                choices = AD_STRIP_CHOICES,
                                default = '')

    TRACK_COUNT_CHOICES = (
        ('0','0'),
        ('1', '1'),
        ('2', '2'),
    )
    track_count = models.CharField(max_length=7,
                                   choices = TRACK_COUNT_CHOICES,
                                   default = '')

    STOCK_CHOICES = (
        ('Kodak', 'Kodak'),
        ('Ferrania','Ferrania'),
        ('3M', '3M'),
        ('Agfa-Gevaert', 'Agfa-Gevaert'),
        ('Pathe', 'Pathe'),
        ('unknown', 'unknown'),
    )
    stock = models.CharField(max_length=25,
                             choices = STOCK_CHOICES,
                             default = '')


    shrinkage = models.IntegerField(default = '0')



    def __str__(self):
        return self.item_title
