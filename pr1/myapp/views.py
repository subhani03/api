from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET'])
def Apioverview(r):
    api_urls={
        'all_items':'/all/',
        'search by category':'?category=category_name',
        'search by subcategory':'/?subcategory=category_name',
        'Add':'/create',
        'update':'/update/pk',
        'delete':'/item/pk/delete'
    }
    return Response(api_urls)
@api_view(['POST'])
def add_items(r):
    if r.method=='GET':
      items=Item.objects.all()
      serializer=ItemSerializers(items,many=True)
      return Response(serializer.data)
    if r.method=='POST':
        serializer=ItemSerializers(data=r.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)
    """ item=ItemSerializers(data=r.data)
    if item.objects.filter(**ritems.data).exists():
        raise serializers.ValidationError('This data already exists')
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND) """
@api_view(['GET'])
def view_items(r):
    items=Item.objects.all()
    serializer=ItemSerializers(items,many=True)
    return Response(serializer.data)


    """ if r.Query_params:
        items=Item.objects.filter(**r.Query_params.dict())
    else:
        items=Item.objects.all()
    if items:
        serializer=ItemSerializers(items,many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
 """    
@api_view(['POST'])
def update_items(r,pk):
    try:
        item=Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    seriaalizer=ItemSerializers(item,data=r.data)
    if seriaalizer.is_valid():
        seriaalizer.save()
        return Response(seriaalizer.data)
    return Response(seriaalizer.errors,status=status.HTTP_400_BAD_REQUEST)

    """ item=Item.objects.get(pk=pk)
    data=ItemSerializers(instance=item,data=r.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)"""
@api_view(['GET'])
def delete_item(r,pk):
    item=Item.objects.get(pk=pk)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


{
        "category":"New Item",
        "subcategory":"products",
        "name":"nabati",
        "amount":10
    }







