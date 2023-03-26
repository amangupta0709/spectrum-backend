from rest_framework import serializers
from user.models import UserDetails, UserRounds


class UserDetailsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    age = serializers.IntegerField(required=True)
    mobile = serializers.CharField(required=True)
    college = serializers.CharField(required=True)
    roll_number = serializers.CharField(required=True)
    tricity_resident = serializers.BooleanField(required=True)
    need_stay = serializers.BooleanField(required=True)
    image_url = serializers.URLField(required=True)

    class Meta:
        model = UserDetails
        fields = (
            "name",
            "age",
            "mobile",
            "college",
            "roll_number",
            "tricity_resident",
            "need_stay",
            "image_url",
        )


class UserRoundsSerializer(serializers.ModelSerializer):
    registered_round_one = serializers.BooleanField()
    selected_round_two = serializers.BooleanField()
    registered_round_two = serializers.BooleanField()
    selected_round_three = serializers.BooleanField()
    registered_round_three = serializers.BooleanField()

    class Meta:
        model = UserRounds
        fields = (
            "registered_round_one",
            "selected_round_two",
            "registered_round_two",
            "selected_round_three",
            "registered_round_three",
        )
