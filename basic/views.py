from django.shortcuts import render
from rest_framework import generics
from rest_framework.reverse import reverse
from basic.models import AVItem
from basic.serializers import AVItemSerializer

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
