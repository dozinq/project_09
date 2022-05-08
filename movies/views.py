from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.views.decorators.http import require_safe
from django.core.paginator import Paginator

from rest_framework.decorators import api_view
from rest_framework.response import Response

from movies.serializers import MovieSerialzier

from .models import Movie

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.order_by('-popularity')
    paginator = Paginator(movies, 10)
    page_number = request.GET.get('page')
    # queryset
    page_obj = paginator.get_page(page_number)
    
    context = {
        'movies': page_obj,
    }
    return render(request, 'movies/index.html', context)

@api_view(['GET'])
def ajax(request):
    movies = Movie.objects.order_by('-popularity')
    paginator = Paginator(movies, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    serializer = MovieSerialzier(page_obj, many=True)
    
    return Response(serializer.data)

@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    if request.user.is_authenticated:
        movies = Movie.objects.order_by('-vote_average')[:10]
        context = {
            'movies': movies,
        }
        return render(request, 'movies/recommended.html', context)
    return redirect('accounts:login')
