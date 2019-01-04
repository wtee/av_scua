
AV_SCUA
========

AV_SCUA is a Django-based API and interface for searching and editing Iowa State University's audio-visual catalog. 

Getting Started
----------------

``` {.sourceCode .console}
$ git clone https://github.com/wryan14/av_scua.git
$ cd av_scua
$ conda create -n "av_scua_env" python=3.7
$ pip install requirements.txt
```

With the environment created, run the django development
server in the typical fashion.

``` {.sourceCode .console}
$ python manage.py runserver
```

Changing Filters
-----------------

To change the filterable fields, navigate to 'templates/basic/dtable.html' and modify the javascript generated table data:


> ``` {.sourceCode .javascript}
> '<td align="right" width="150">UID:</td>'+
> '<td>'+d.uid+'</td>'+
> ```
