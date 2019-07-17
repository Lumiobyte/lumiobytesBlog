from django.shortcuts import render

from blog.models import BlogPost

from .models import SearchQuery

def search_view(request):
    searchQuery = request.GET.get('q', None)
    print(searchQuery)

    user = None
    if request.user.is_authenticated:
        user = request.user
    if searchQuery is not None: 
        SearchQuery.objects.create(user=user, query=searchQuery)
        qs = BlogPost.objects.all().search(query=searchQuery)

    return render(request, 'search/view.html', {'query': searchQuery, 'resultCount': len(qs), 'results': qs})
