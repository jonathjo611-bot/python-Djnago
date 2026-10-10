import datetime
from django.shortcuts import render


def artist_detail(request):
    # A list of dictionaries sent to the template (sample data made up for practice)
    artists = [
        {
            "name": "luna ray",
            "bio": "Indie pop singer who writes dreamy songs about late night drives and city lights",
            "songs": ["Neon Rain", "Paper Moon", "Static Hearts"],
            "release_date": datetime.date(2024, 3, 15),
        },
        {
            "name": "the midnight bloom",
            "bio": "",                                   # empty on purpose, to show |default
            "songs": ["Velvet Hour", "Glass Garden"],
            "release_date": datetime.date(2023, 11, 2),
        },
        {
            "name": "DJ KAVI",
            "bio": "Chennai based producer",
            "songs": ["Marina Beat", "Sunday Bass", "Chai Break", "Rooftop Lights"],
            "release_date": datetime.date(2025, 7, 21),
        },
    ]
    return render(request, "artist/artist_detail.html", {"artists": artists})
