from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import urllib.request
import re
from .serializer import WebAccessReadSerializer
from .models import WebAccessRead

# Create your views here.

@api_view(['GET'])
def index(request, *args, **kwargs):
    """Check link and word without recording it to DB

    Args:
       request link: web url
                word: desired word to count

    Returns:
        word: Total number the word mentioned
    """
    result = readThenCount(request.query_params)
    return Response(data=result, status=status.HTTP_200_OK)


@api_view(['POST'])
def addLink(request):
    """Count all word from link provided and Add them to DB

    Args:
        request link: web url
                word: desired word to count

    Returns:
        word: Total number the word mentioned
    """
    serializer = WebAccessReadSerializer(data=request.data)
    if serializer.is_valid():
        result = readThenCount(request.data)
        serializer.save(count=result[request.data["word"]])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getAll(request, id, *args, **kwargs):
    """Get a record from DB according to id given

    Args:
        id (integer): ID of the record

    Returns:
        [object|array]: details of the specific record
    """
    model = WebAccessRead.objects.get(pk=id)
    check = WebAccessReadSerializer(model)
    return Response(data=check.data, status=status.HTTP_200_OK)

def readThenCount(data):
    fp = urllib.request.urlopen(data["link"])
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    # split includes special characters
    split_word_no_special_character = re.split('\W+', mystr.lower()) 
    result = {w:split_word_no_special_character.count(w) for w in [data["word"].lower()]}

    return result
