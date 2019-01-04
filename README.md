
AV_SCUA
========


AV_SCUA is a django based API and interface built to integrate with a
database containing Iowa State University audio visual materials. An
example of this code, can be found at
<https://rwolfsla.pythonanywhere.com/>.

Getting Started
===============

To run this code locally, you can clone the repository and create an
anaconda environment.

``` {.sourceCode .console}
$ git clone https://github.com/wryan14/av_scua.git
$ cd av_scua
$ conda create -n "av_scua_env" python=3.7
$ pip install requirements.txt
```

Once the environment is created, you can run the django development
server in the typical fashion.

``` {.sourceCode .console}
$ python manage.py runserver
```

Changing Filters
================

To modify which fields are being filtered, go to
'templates/basic/dtable.html' and modify the table data to reflect the
desired name, and to target the desired API field.

> ``` {.sourceCode .javascript}
> '<td align="right" width="150">UID:</td>'+
> '<td>'+d.uid+'</td>'+
> ```
