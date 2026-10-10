from django.shortcuts import render


def podcast_detail(request):
    podcasts = [
        {"title": "Code & Chai", "host": "Meera Nair", "category": "Technology", "episodes": 24},
        {"title": "Chemistry Cafe", "host": "Dr. Arun Rao", "category": "Science", "episodes": 18},
        {"title": "Startup Stories", "host": "Kavya Menon", "category": "Business", "episodes": 31},
    ]
    return render(request, "podcast/podcast_detail.html", {"podcasts": podcasts})
