from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Director, Review, Movie
from .serializers import DirectorSerializers, MovieSerializers, ReviewSerializers



@api_view(['GET'])
def director_api_view(request):
    categories = Director.objects.all()
    serializer = DirectorSerializers(categories, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def director_detail_api_view(request, id):
    try:
        category = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data="ERROR! Такой страницы не существует")
    serializer = DirectorSerializers(category)
    return Response(data=serializer.data)


@api_view(['GET'])
def movies_api_view(request):
    movie = Movie.objects.all()
    serializer = MovieSerializers(movie, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data="ERROR! Такой страницы не существует")
    serializer = MovieSerializers(movie)
    return Response(data=serializer.data)


@api_view(['GET'])
def reviews_api_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializers(reviews, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data="ERROR! Такой страницы не существует")
    serializer = ReviewSerializers(review)
    return Response(data=serializer.data)