import json
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status, mixins, viewsets
from django.contrib.sessions.models import Session
from ..models import Location, Event, Map
from .serializers import EventSerializer, LocationSerializer, MapSerializer

from rest_framework import status
from django.http import JsonResponse

class EventAPIView(generics.ListAPIView):

    serializer_class = EventSerializer

    def get_queryset(self):

        # queryset = Event.objects.all()
        if self.request.GET.get('q') != None and self.request.GET.get('q') != '':
            query = self.request.GET.get('q')
            queryset = Location.objects.get(pk=query).events


        return queryset

class LocationAPIView(APIView):

    serializer_class = LocationSerializer




    def get(self, request, *args, **kwargs):

        # queryset = Event.objects.all()
        if self.request.GET.get('q') != None and self.request.GET.get('q') != '':
            query = self.request.GET.get('q')
            queryset = Location.objects.get(pk=query)
            serializer = LocationSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
            # serializer = self.get_serializer(queryset)
            # return queryset
class MapAPIView(APIView):

    serializer_class = MapSerializer




    def get(self, request, *args, **kwargs):

        # queryset = Event.objects.all()
        # if self.request.GET.get('q') != None and self.request.GET.get('q') != '':
            # query = self.request.GET.get('q')
        queryset = Map.objects.get(pk=1)
        serializer = MapSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
            # serializer = self.get_serializer(queryset)
            # return queryset
