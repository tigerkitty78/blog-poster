from django.shortcuts import render
from django.core.paginator import Paginator
from .forms import SearchForm
from .models import Post
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})



def post_list(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 5)  # Show 5 posts per page.
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'posts': posts})

def search(request):
    form = SearchForm(request.GET or None)
    query = request.GET.get('query')
    results = []
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    return render(request, 'search_results.html', {
        'form': form,
        'results': results,
        'query': query
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


# Create your views here.
