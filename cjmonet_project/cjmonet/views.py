from django.shortcuts import render
from .models import Artist, Painting, Sticker
from rest_framework import generics
from .serializers import ArtistSerializer, PaintingSerializer, StickerSerializer

# Create your views here.

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class PaintingList(generics.ListCreateAPIView):
    queryset = Painting.objects.all()
    serializer_class = PaintingSerializer

class PaintingDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Painting.objects.all()
    serializer_class = PaintingSerializer

class StickerList(generics.ListCreateAPIView):
    queryset = Sticker.objects.all()
    serializer_class = StickerSerializer

class StickerDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Sticker.objects.all()
    serializer_class = StickerSerializer
