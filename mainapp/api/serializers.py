from rest_framework import serializers
from ..models import Location,Event,Map,NPC
import json
class EventSerializer(serializers.ModelSerializer):

    # def to_representation(self, instance):
    #     rep = super(TramStopSerializer, self).to_representation(instance)
    #     rep['nameno'] = str(instance)
    #     rep['longitude'] = float(instance.longitude)
    #     rep['latitude'] = float(instance.latitude)
    #     return rep
    # nameno = serializers.CharField(source='tramstop.name', read_only=True)

    class Meta:
        model = Event
        fields = ['id',
'type',
'text',
'warpto',
'warpx',
'warpy',
'warpor'

                  ]
        # read_only_fields = ['id']

class NPCSerializer(serializers.ModelSerializer):
    topleft = serializers.CharField(read_only = True)
    poxy = serializers.CharField(read_only = True)
    def to_representation(self, instance):
        rep = super(NPCSerializer, self).to_representation(instance)
        rep['topleft'] = [instance.starttop,instance.startleft]
        rep['poxy'] = [instance.startposx,instance.startposy]
        return rep

    class Meta:
        model = NPC
        fields = [
        'name',
        'dialog',
        'type',
        'topleft',
        'poxy',
        'startposex']
class LocationSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True, read_only=True)
    npcs = NPCSerializer(many=True)
    def to_representation(self, instance):
        rep = super(LocationSerializer, self).to_representation(instance)
        rep['tileorder'] = json.loads(instance.tileorder)
        return rep
    # nameno = serializers.CharField(source='tramstop.name', read_only=True)
    class Meta:
        model = Location
        fields = ['id',
                'name',
                'tileorder',
                'events',
                'npcs'
                  ]

class MapSerializer(serializers.ModelSerializer):
    locations= LocationSerializer(many=True)

    # def to_representation(self, instance):
    #     rep = super(LocationSerializer, self).to_representation(instance)
    #     rep['tileorder'] = json.loads(instance.tileorder)
    #     return rep
    # nameno = serializers.CharField(source='tramstop.name', read_only=True)
    class Meta:
        model = Map
        fields = ['id',
                'name',
                'locations',

                  ]
