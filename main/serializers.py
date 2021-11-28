from rest_framework import serializers

from .models import *


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    added = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', read_only=True)

    class Meta:
        model = Movie
        exclude = ('author', )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = instance.author.email
        representation['images'] = MovieImageSerializer(instance.images.all(), many=True, context=self.context).data
        representation['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        return representation

    def create(self, validated_data):
        request = self.context.get('request')
        user_id = request.user.id
        validated_data['author_id'] = user_id
        movie = Movie.objects.create(**validated_data)
        return movie


class MovieImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieImage
        fields = '__all__'

    def _get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            url = obj.image.url
            return 'http://localhost:5000' + url
        return ''

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        reply = Comment.objects.create(author=request.user, **validated_data)
        return reply
