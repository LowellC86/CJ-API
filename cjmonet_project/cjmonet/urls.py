from django.urls import path 
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('artists/', views.ArtistList.as_view(), name='artist_list'),
    path('paintings/', views.PaintingList.as_view(), name='painting_list'),
    path('sticker/', views.StickerList.as_view(), name='sticker_list'),
    path('artists/<int:pk>/', views.ArtistDetail.as_view(), name='artist_detail'),
    path('paintings/<int:pk>/', views.PaintingDetail.as_view(), name='painting_detail'),
    path('sticker/<int:pk>/', views.StickerDetail.as_view(), name='sticker_detail') 
]
