from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from .models import Movie, Director, Review
from .serializers import (MovieSerializer, MovieValidateSerializer,
                          DirectorSerializer, DirectorValidateSerializer,
                          ReviewSerializer, ReviewValidateSerializer)

@api_view(['GET', 'POST'])
def movie_list_api_view(request):
    print(request.user)
    if request.method == 'GET':
        movies = (Movie.objects.select_related('director').prefetch_related('reviews').all())
        list_ = MovieSerializer(instance=movies, many=True).data
        return Response(data=list_)
    elif request.method == 'POST':
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)

        print(serializer.validated_data)
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        print(title, description, duration)
        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        return Response(data={'movie_id': movie.id}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_api_view(request, id):
    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = MovieSerializer(movies, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movies.title = serializer.validated_data.get('title')
        movies.description = serializer.validated_data.get('description')
        movies.duration = serializer.validated_data.get('duration')
        movies.director_id = serializer.validated_data.get('director_id')
        movies.save()
        return Response(data=MovieSerializer(movies).data,
                        status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def director_list_api_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        list_ = DirectorSerializer(instance=directors, many=True).data
        return Response(data=list_)
    elif request.method == 'POST':
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        print(serializer.validated_data)
        name = request.data.get('name')
        print(name)
        director = Director.objects.create(name=name)
        return Response(data={'director_id': director.id}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_api_view(request, id):
    try:
        directors = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = DirectorSerializer(directors, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        directors.name = serializer.validated_data.get('name')
        directors.save()
        return Response(data=DirectorSerializer(directors).data,
                        status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        directors.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        list_ = ReviewSerializer(instance=reviews, many=True).data
        return Response(data=list_)
    elif request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        print(serializer.validated_data)
        movie_id = request.data.get('movie_id')
        text = request.data.get('text')
        star = request.data.get('star')
        print(text, star)
        review = Review.objects.create(text=text, star=star, movie_id=movie_id)
        return Response(data={'review_id': review.id}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_api_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ReviewSerializer(reviews, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        reviews.movie_id = serializer.validated_data.get('movie_id')
        reviews.text = serializer.validated_data.get('text')
        reviews.star = serializer.validated_data.get('star')
        reviews.save()
        return Response(data=ReviewSerializer(reviews).data,
                        status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        reviews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


