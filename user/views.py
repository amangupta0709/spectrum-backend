from knox.models import AuthToken
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
import random
import string
from user.serializers import UserDetailsSerializer, UserRoundsSerializer
from user.models import UserDetails, UserRounds


class LoginAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    # serializer_class = OAuthSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = "".join(random.choices(string.ascii_lowercase, k=8))
        data = {}
        if not email:
            return Response(
                {"message": "Invalid Email"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = User.objects.get(username=email)
        except User.DoesNotExist:
            user = User.objects.create_user(username=email, password=password)

        data["token"] = AuthToken.objects.create(user)[1]
        rounds_obj, _ = UserRounds.objects.get_or_create(user=user)
        serializer = UserRoundsSerializer(rounds_obj)
        data["user_rounds"] = serializer.data

        return Response(
            data,
            status=status.HTTP_200_OK,
        )


class UserDetailsAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserDetailsSerializer

    def post(self, request, *args, **kwargs):
        user_details_obj, _ = UserDetails.objects.get_or_create(user=request.user)
        serializer = self.get_serializer(user_details_obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        data = {}
        rounds_data = {
            "registered_round_one": True,
        }
        rounds_obj = request.user.rounds
        rounds_serializer = UserRoundsSerializer(
            rounds_obj, data=rounds_data, partial=True
        )
        rounds_serializer.is_valid(raise_exception=True)
        rounds_serializer.save()
        data["user_rounds"] = rounds_serializer.data

        return Response(
            data,
            status=status.HTTP_201_CREATED,
        )


class UserRoundsAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserRoundsSerializer

    def get(self, request, *args, **kwargs):
        try:
            rounds_obj = UserRounds.objects.get(user=request.user)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(rounds_obj)
        data = {}
        data["user_rounds"] = serializer.data

        return Response(data, status=status.HTTP_200_OK)
