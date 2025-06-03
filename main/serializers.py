from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Dog
from rest_framework_simplejwt.tokens import RefreshToken

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        exclude = ['owner']

class SignupSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=6)
    marketing_opt_in = serializers.BooleanField()
    dog = DogSerializer()

    def create(self, validated_data):
        dog_data = validated_data.pop('dog')
        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Dog.objects.create(owner=user, **dog_data)
        refresh = RefreshToken.for_user(user)
        return {
            "user": {
                "id": user.id,
                "email": user.email
            },
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }




from rest_framework import serializers
from .models import Order
from django.contrib.auth.models import User

class OrderSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Order
        exclude = ['created_at', 'is_paid', 'user']  # we'll inject user manually

    def create(self, validated_data):
        email = validated_data.pop('email')
        user = User.objects.filter(email=email).first()
        if not user:
            raise serializers.ValidationError({"user": ["No user found with this email."]})
        validated_data['user'] = user
        return Order.objects.create(**validated_data)



from rest_framework import serializers
from .models import User, Dog

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']  # add any extra fields as needed
        extra_kwargs = {'email': {'read_only': True}}


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        exclude = ['owner']  # or use fields explicitly




# class OrderBoxHistorySerializer(serializers.ModelSerializer):
#     box_name = serializers.CharField(source='monthly_box.name', read_only=True)
#     box_theme = serializers.CharField(source='monthly_box.name', read_only=True)  # assuming theme = name
#     box_image = serializers.ImageField(source='monthly_box.image', read_only=True)
#     rating = serializers.FloatField(source='monthly_box.rating', read_only=True)
#     month = serializers.SerializerMethodField()
#     year = serializers.SerializerMethodField()

#     class Meta:
#         model = Order
#         fields = ['id', 'box_name', 'box_theme', 'box_image', 'month', 'year', 'status', 'rating']

#     def get_month(self, obj):
#         return obj.monthly_box.month if obj.monthly_box else None

#     def get_year(self, obj):
#         return obj.monthly_box.year if obj.monthly_box else None

# serializers.py
class OrderBoxHistorySerializer(serializers.ModelSerializer):
    box_name = serializers.CharField(source='monthly_box.name', read_only=True)
    box_theme = serializers.CharField(source='monthly_box.name', read_only=True)
    box_image = serializers.ImageField(source='monthly_box.image', read_only=True)
    month = serializers.SerializerMethodField()
    year = serializers.SerializerMethodField()
    rating = serializers.IntegerField(read_only=True)  # ✅ ensure this line exists

    class Meta:
        model = Order
        fields = ['id', 'box_name', 'box_theme', 'box_image', 'month', 'year', 'status', 'rating']

    def get_month(self, obj):
        return obj.monthly_box.month if obj.monthly_box else None

    def get_year(self, obj):
        return obj.monthly_box.year if obj.monthly_box else None



class OrderRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['rating']
