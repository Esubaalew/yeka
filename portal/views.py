from django.shortcuts import render, get_object_or_404
from .models import Research, Author


# Home page view
def home(request):
    # Fetch recent research (for example, the 6 latest research items)
    recent_research = Research.objects.order_by('-id')[:6]  # Adjust the number as needed

    # Fetch featured authors (for simplicity, we'll just get a few random authors)
    featured_authors = Author.objects.all()[:4]  # Adjust the number as needed

    context = {
        'recent_research': recent_research,
        'featured_authors': featured_authors
    }

    return render(request, 'home.html', context)


# Authors page view
def authors(request):
    # Fetch all authors
    all_authors = Author.objects.all()

    context = {
        'all_authors': all_authors,
    }

    return render(request, 'authors.html', context)


# Author detail page view
def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)

    context = {
        'author': author,
    }

    return render(request, 'author_detail.html', context)


# Research page view
def research_list(request):
    # Fetch all research entries
    all_research = Research.objects.all()

    context = {
        'all_research': all_research,
    }

    return render(request, 'research_list.html', context)


# Research detail page view
def research_detail(request, research_id):
    research = get_object_or_404(Research, id=research_id)

    context = {
        'research': research,
    }

    return render(request, 'research_detail.html', context)
    
def view_404(request, exception):
    return render(request, '404.html', status=404)
