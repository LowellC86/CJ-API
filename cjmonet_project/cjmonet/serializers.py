from rest_framework import serializers
from .models import Artist, Painting, Sticker

class PaintingSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedRelatedField(
        view_name='artist_detail',
        read_only=True
    )

    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(),
        source='artist'
    )

    class Meta:
        model = Painting
        fields = ('id', 'artist_id', 'artist', 'title', 'preview_url', 'description')


class StickerSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedRelatedField(
        view_name='artist_detail',
        read_only=True
    )

    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(),
        source='artist'
    )

    class Meta:
        model = Sticker
        fields = ('id', 'artist_id', 'artist', 'title', 'image_url', 'description')
        
class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    paintings = PaintingSerializer(
        many=True,
        read_only=True
    )

    artist_url = serializers.ModelSerializer.serializer_url_field(
        view_name='artist_detail'
    )
    
    class Meta:
        model = Artist
        fields = ('id', 'artist_url', 'name', 'photo_url', 'description', 'paintings')