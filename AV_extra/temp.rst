=======================
Temporary Instructions
=======================

-------------
Overview
-------------
This file will document how I build SUCA's AV Database. I will be using a
2NF database, js datatables, django admin, bootstrap. This also needs the ability
to search and export a csv file.

.. code:: shell

  django-admin startproject AV_SCUA
  cd AV_SCUA
  django-admin startapp basic

1. Add TEMPLATES_DIR and add app to settings.py
2. set up first test
3. first test passes by adding templates/basic/home.html, basic/urls.py, urls.py,
and creating a simple view in basic/views.py

#################
Functional Tests
#################

Functional test boots up a live server and checks if layout is correct.
This makes use of selenium.

.. code:: shell

  pip install selenium

To run all tests, use

.. code:: shell

  python manage.py test


######################
Django Tests
######################
1. Test if home page template is used
2. Test if data is being correctly modeled

#####################
Create Super User
#####################
.. code:: shell

  python manage.py makemigrations
  python manage.py migrate

Creating superuser with name and password

.. code:: shell

  python manage.py createsuperuser

#####################
Word about the Model
#####################

There does not appear to be much benefit in putting the model into 3NF. If
this changes, we can easily start to break apart items.

################
Word about CRUD
################

We can roll out the database with datatables, without having all of the CRUD
operations available through the tables. For now these items are editable through
Django's admin.  The Django API is certainly worth looking into for this.


#####################
Datatables
#####################

The first thing to know is that you need to code a second serializer to
account for datatables

views.py

.. code-block:: python

  @csrf_exampt
  def av_list(request):
      if request.method == 'GET':
          avitems = AVItem.objects.all()


serializers.py

.. code-block:: python

  class ToyAVSerializer(serializers.ModelSerializer):
      class Meta:
          model = AVItem
          fields = ('uid',
                    'item_title',
                    'series_title',
                    'episode_title')


##################
Follow up needed
##################

1. Don't understand Film generation instructions
2. Need to figure out how to do multiple selection for Base field
3. Similar issue with sound format type

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
