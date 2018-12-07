from django.shortcuts import render
from rest_framework import generics
from rest_framework.reverse import reverse
from basic.models import AVItem
from basic.serializers import AVItemSerializer, ToyAVSerializer

# Create your views here.
def home_page(request):
    '''
        Home Page located in templates/basic/home.html
    '''
    return render(request, 'basic/dtable.html')

class AVItemList(generics.ListCreateAPIView):
    '''
        view for API
    '''
    queryset = AVItem.objects.all()
    serializer_class = AVItemSerializer
    name = 'avitem-list'
    filter_fields = (
        'uid',
        'item_title'
    )
    search_fields = (
        'uid',
        'item_title',
    )
    ordering_fields = (
        'uid',
        'item_title'
    )

class AVItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AVItem.objects.all()
    serializer_class = AVItemSerializer
    name = 'avitem-detail'


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# plain json views for datatables

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def av_list(request):
    if request.method == 'GET':
        avitems = AVItem.objects.all()
        avitem_serializer = ToyAVSerializer(avitems, many=True)
        return JSONResponse(avitem_serializer.data)
