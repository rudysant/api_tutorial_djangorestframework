from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from app_api_tutorial.models import Tutorial
from app_api_tutorial.serializers import TutorialSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
    
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Tutorial.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
        
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    if request.method == 'GET':
        tutorial = Tutorial.objects.get(pk=pk)
        tutorials_serializer = TutorialSerializer(tutorial, many=False)
        return JsonResponse(tutorials_serializer.data, safe=False)
    
    elif request.method == 'PUT': 
        tutorial = Tutorial.objects.get(pk=pk)
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
       
    elif request.method == 'DELETE': 
        tutorial = Tutorial.objects.get(pk=pk)
        tutorial.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def tutorial_list_published(request):
    tutorials = Tutorial.objects.filter(published=True)
        
    if request.method == 'GET': 
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)