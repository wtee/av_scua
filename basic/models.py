from django.db import models

# Create your models here.
class AVItem(models.Model):
    '''
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| Variable Name           | Notes                                                                          | Original Field Name     |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| uid                     | Unique                                                                         | UID                     |
|                         |   Identifier; AV#;Text                                                         |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| original_id             | Original Unique ID, Text                                                       | Original ID             |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| collection_id           | Collection I.D., Text                                                          | Collection ID           |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| item_title              | Title of object, Text                                                          | Title                   |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| series_title            | Name of Series, Text                                                           | Series Title            |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| episode_title           | Name of Episode, Text                                                          | Episode Title           |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| can_number              | Number on Film Can, Text                                                       | Can Number              |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| original_can_number     | Original Number on Can, Text                                                   | Original Can Number     |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| call_number             | Catalog Call Number, Text                                                      | Call Number             |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| date_created            | Orginal Creation Date, Text                                                    | Date Created            |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| creadits                | These are the Credits, Text                                                    | Credits                 |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| description             | Description of Content, Text                                                   | Description             |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| location                | Location of physical item,                                                     | Location                |
|                         |   Text                                                                         |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| format_duration         | enter                                                                          | Format duration         |
|                         |   duration of film formatted as h:mm:ss                                        |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| media_type              | Following List: Film, Video,                                                   | Media Type              |
|                         |   Audio                                                                        |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| copies                  | Yes, No                                                                        | Copies                  |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| other_notes             | Enter                                                                          | Other Notes             |
|                         |   notes or details about the film, Text                                        |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| digital_preservation    | Yes, No                                                                        | Digital Preservation    |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| lto_number              | Enter LTO number, Text                                                         | LTO Number              |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| status                  | Following List: on shelf,                                                      | Status                  |
|                         |   Conservation,Vendor, Loan                                                    |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| copyright               | Following List: Open,                                                          | Copyright               |
|                         |   Restricted                                                                   |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| gauge                   | enter                                                                          | Gauge                   |
|                         |   gauge from the following list:                                               |                         |
|                         |     -8mm                                                                       |                         |
|                         |     -Super 8mm                                                                 |                         |
|                         |     -16mm                                                                      |                         |
|                         |     -Super 16mm                                                                |                         |
|                         |     -35mm                                                                      |                         |
|                         |     -35/32mm                                                                   |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| ???                     | enter                                                                          | Film generation         |
|                         |   either "Positive" and/or "Negative" then any relevant                        |                         |
|                         |   additional categories from the following list separated by a comma and a     |                         |
|                         |   space:                                                                       |                         |
|                         |     -Projection print                                                          |                         |
|                         |     -A roll                                                                    |                         |
|                         |     -B roll                                                                    |                         |
|                         |     -C roll                                                                    |                         |
|                         |     -D roll                                                                    |                         |
|                         |     -Answer print                                                              |                         |
|                         |     -Camera original                                                           |                         |
|                         |     -Composite                                                                 |                         |
|                         |     -Duplicate                                                                 |                         |
|                         |     -Edited                                                                    |                         |
|                         |     -Fine grain master                                                         |                         |
|                         |     -Intermediate                                                              |                         |
|                         |     -Kinescope                                                                 |                         |
|                         |     -Separate magnetic soundtrack                                              |                         |
|                         |     -Preservation master                                                       |                         |
|                         |     -Mezzanine                                                                 |                         |
|                         |     -Separate optical soundtrack                                               |                         |
|                         |     -Original                                                                  |                         |
|                         |     -Outs and trims                                                            |                         |
|                         |     -Reversal                                                                  |                         |
|                         |     -Work print                                                                |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| footage                 | enter                                                                          | Footage                 |
|                         |   footage                                                                      |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| ???                     | enter                                                                          | Base                    |
|                         |   film base from the following list separated by a comma and a space:          |                         |
|                         |     -Acetate                                                                   |                         |
|                         |     -Polyestar                                                                 |                         |
|                         |     -Mixed                                                                     |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| frame_rate              | enter                                                                          | Frame rate              |
|                         |   frame rate from the following list:                                          |                         |
|                         |     -16 fps                                                                    |                         |
|                         |     -18 fps                                                                    |                         |
|                         |     -24 fps                                                                    |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| color                   | enter                                                                          | Color                   |
|                         |   either "Color" and/or "Black and white" then any relevant                    |                         |
|                         |   additional categories from the following list separated by a comma and a     |                         |
|                         |   space:                                                                       |                         |
|                         |     -Toned                                                                     |                         |
|                         |     -Tinted                                                                    |                         |
|                         |     -Hand coloring                                                             |                         |
|                         |     -Stencil coloring                                                          |                         |
|                         |     -Ektachrome                                                                |                         |
|                         |     -Kodachrome                                                                |                         |
|                         |     -Technicolor                                                               |                         |
|                         |     -Anscochrome                                                               |                         |
|                         |     -Eco                                                                       |                         |
|                         |     -Eastman                                                                   |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| aspect_ratio            | enter                                                                          | Aspect ratio            |
|                         |   aspect ratio from the following list:                                        |                         |
|                         |     -1.18:1                                                                    |                         |
|                         |     -1.33:1                                                                    |                         |
|                         |     -1.37:1                                                                    |                         |
|                         |     -1.66:1                                                                    |                         |
|                         |     -1.85:1                                                                    |                         |
|                         |     -2.35:1                                                                    |                         |
|                         |     -2.39:1                                                                    |                         |
|                         |     -2.59:1                                                                    |                         |
|                         |     -2.66:1                                                                    |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| anamorphic              | enter                                                                          | Anamorphic              |
|                         |   either "Yes" or "No"                                                         |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| sound                   | enter                                                                          | Sound                   |
|                         |   either "Sound" or "Silent"                                                   |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| ???                     | enter                                                                          | Sound format type       |
|                         |   sound format types from the following list separated by a comma and a        |                         |
|                         |   space:                                                                       |                         |
|                         |     -Optical: Variable Area: Unilateral,                                       |                         |
|                         |     -Optical: Variable Area: Dual Unilateral                                   |                         |
|                         |     -Optical: Variable Area: Bilateral                                         |                         |
|                         |     -Optical: Variable Area: Dual Bilateral                                    |                         |
|                         |     -Optical: Variable Area: Multi-track (ie Maurer)                           |                         |
|                         |     -Optical: Variable Area: Duplex                                            |                         |
|                         |     -Optical: Variable Density                                                 |                         |
|                         |     -Optical: Variable Density: Multiple Density                               |                         |
|                         |     -Magnetic                                                                  |                         |
|                         |     -Sound on separate media                                                   |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| sound_content_type      | leave                                                                          | Sound content type      |
|                         |   blank if film is silent, enter "Composite track" if film is                  |                         |
|                         |   composite of audio and image, or enter sound content type from the following |                         |
|                         |   list if film is audio only:                                                  |                         |
|                         |     -Music track                                                               |                         |
|                         |     -Effects track                                                             |                         |
|                         |     -Dialog                                                                    |                         |
|                         |     -Outtakes                                                                  |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| sound_field             | leave                                                                          | Sound field             |
|                         |   blank if silent, or enter sound field from the following list:               |                         |
|                         |     -Mono                                                                      |                         |
|                         |     -Stereo                                                                    |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| clean                   | enter                                                                          | Clean                   |
|                         |   "Yes" if film should be fully cleaned either by ultrasonic cleaner           |                         |
|                         |   or velvet cloth, enter "No" if film should only be spot-cleaned              |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| resolution              | entire                                                                         | Resolution              |
|                         |   desired resolution from the following list:                                  |                         |
|                         |     -HD                                                                        |                         |
|                         |     -2k                                                                        |                         |
|                         |     -4k                                                                        |                         |
|                         |     -5k                                                                        |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| sample_encoding         | enter                                                                          | Sample Encoding         |
|                         |   either "Linear 10 bit" or "Linear 16 bit" if film is                         |                         |
|                         |   positive, enter "Logarithmic 10 bit" if film is negative                     |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| return_on_original_reel | enter                                                                          | Return on original reel |
|                         |   "Yes" if film should be wound back on to the reel on which it                |                         |
|                         |   arrived, enter "No" if original reel can be disposed of                      |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| mold                    | enter                                                                          | Mold                    |
|                         |   "Treated" if film has been treated for mold in the past, enter               |                         |
|                         |   "No" if film has no history of mold contamination                            |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| shrinkage               | enter                                                                          | Shrinkage               |
|                         |   shrinkage value to two decimal places, preface with a minus sign (-) if the  |                         |
|                         |   value is for stretch rather than shrinkage                                   |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| ad_strip                | leave                                                                          | AD strip                |
|                         |   blank if no AD strip test data available, or enter AD strip test result from |                         |
|                         |   the following list:                                                          |                         |
|                         |     -0                                                                         |                         |
|                         |     -0.5                                                                       |                         |
|                         |     -1                                                                         |                         |
|                         |     -1.5                                                                       |                         |
|                         |     -2                                                                         |                         |
|                         |     -2.5                                                                       |                         |
|                         |     -3                                                                         |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| track_count             | enter                                                                          | Track count             |
|                         |   "0" if film is silent, enter "1" if film is mono, or                         |                         |
|                         |   enter "2" if film is stereo                                                  |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
| stock                   | enter                                                                          | Stock                   |
|                         |   film stock from the following list:                                          |                         |
|                         |     -Agfa                                                                      |                         |
|                         |     -Ansco                                                                     |                         |
|                         |     -Dupont                                                                    |                         |
|                         |     -Orwo                                                                      |                         |
|                         |     -Fuji                                                                      |                         |
|                         |     -Gevaert                                                                   |                         |
|                         |     -Kodak                                                                     |                         |
|                         |     -Ferrania                                                                  |                         |
|                         |     -3M                                                                        |                         |
|                         |     -Agfa-Gevaert                                                              |                         |
|                         |     -Pathe                                                                     |                         |
|                         |     -unknown                                                                   |                         |
+-------------------------+--------------------------------------------------------------------------------+-------------------------+
Use Unicode symbols for table borders

    '''
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
