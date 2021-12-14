from django.shortcuts import render

from rest_framework import viewsets, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Element
from api.serializers import ElementSerializer, RegisterSerializer, MeSerializer


class ElementViewSet(viewsets.ModelViewSet):
    serializer_class = ElementSerializer
    queryset = Element.objects.all()


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def me(request):
    print(request.user)
    print(MeSerializer(request.user).data)
    userinfo = MeSerializer(request.user).data
    userinfo.update({ 'password' : "----" })
    return Response(userinfo, 200)
