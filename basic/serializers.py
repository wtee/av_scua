from rest_framework import serializers
from basic.models import AVItem

class AVItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=AVItem
        view_name = 'avitem-detail'
        fields = ('pk',
                  'uid',
                  'original_id',
                  'collection_id',
                  'item_title',
                  'series_title',
                  'episode_title',
                  'can_number',
                  'original_can_number',
                  'call_number',
                  'date_created',
                  'credits',
                  'description',
                  'location',)

class ToyAVSerializer(serializers.ModelSerializer):
    class Meta:
        model = AVItem
        fields = ('pk',
                  'uid',
                  'item_title',
                  'series_title',
                  'episode_title')
