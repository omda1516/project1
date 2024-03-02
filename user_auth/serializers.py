from rest_framework import serializers
from . import models


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})


class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password_confirmation = serializers.CharField(
        write_only=True, required=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    gender = serializers.ChoiceField(
        choices=models.HospitalUser.GENDERS, required=True)

    class Meta:
        model = models.HospitalUser
        fields = ['username', 'email', 'password',
                  'password_confirmation', 'first_name', 'last_name', 'gender']

    def validate(self, data):
        if data.get('password') != data.get('password_confirmation'):
            raise serializers.ValidationError("Passwords do not match.")
        return super().validate(data)

    def create(self, validated_data):
        user = models.HospitalUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            gender=validated_data['gender']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user
