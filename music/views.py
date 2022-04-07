from logging import raiseExceptions
from django.shortcuts import get_object_or_404
from http.client import FOUND
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Car
from .serializers import CarSerializer
from cars import serializers

# Create your views here.
