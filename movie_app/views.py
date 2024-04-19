from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from .models import Movie, Director, Review
from .serializers import (MovieSerializer, MovieDetailSerializer,
                          DirectorSerializer, DirectorDetailSerializer,
                          ReviewSerializer, ReviewDetailSerializer)

@api_view(['GET'])
def movie_list_api_view(request):
    movies = Movie.objects.all()
    list_ = MovieSerializer(movies, many=True).data
    return Response(data=list_)


@api_view(['GET'])
def movie_api_view(request, id):
    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = MovieDetailSerializer(movies, many=False).data
    return Response(data=data)

@api_view(['GET'])
def director_list_api_view(request):
    directors = Director.objects.all()
    list_ = DirectorSerializer(directors, many=True).data
    return Response(data=list_)


@api_view(['GET'])
def director_api_view(request, id):
    try:
        directors = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = DirectorDetailSerializer(directors, many=False).data
    return Response(data=data)


@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    list_ = ReviewSerializer(reviews, many=True).data
    return Response(data=list_)


@api_view(['GET'])
def review_api_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ReviewDetailSerializer(reviews, many=False).data
    return Response(data=data)


