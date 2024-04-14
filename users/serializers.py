from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'fullname', 'email', 'password', 'onboardingpass', 'articles', 'roadmap']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    

class UserArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['articles', 'onboardingpass']  # Only the articles field is exposed for update

    def update(self, instance, validated_data):
        instance.articles = validated_data.get('articles', instance.articles)
        instance.onboardingpass = True
        instance.save()
        return instance


class UserRoadmapSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['roadmap']

    def update(self, instance, validated_data):
        instance.roadmap = validated_data.get('roadmap', instance.roadmap)
        instance.save()
        return instance
