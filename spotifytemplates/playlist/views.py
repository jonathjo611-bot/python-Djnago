from django.shortcuts import render

PLAYLIST = [
    {'title': 'BbY WOW', 'plays': 33059939, 'album': 'NO ME ARREPIENTO DE SENTIR TANTO'},
    {'title': 'Beauty And A Beat', 'plays': 23060351, 'album': 'Believe'},
    {'title': 'Earrings', 'plays': 22481881, 'album': 'Sweet Boy'},
    {'title': 'Loser', 'plays': 22170033, 'album': 'Deadbeat'},
    {'title': 'The One That Got Away', 'plays': 22169158, 'album': 'Teenage Dream'},
    {'title': 'Dai Dai', 'plays': 21507155, 'album': 'Dai Dai'},
    {'title': 'Self Aware', 'plays': 20891173, 'album': 'Self Aware'},
    {'title': 'the cure', 'plays': 19826357, 'album': 'you seem pretty sad for a girl so in love'},
    {'title': 'Babydoll', 'plays': 19450905, 'album': "Don't Forget About Me, Demos"},
    {'title': 'back to friends', 'plays': 19424543, 'album': 'I Barely Know Her'},
    {'title': 'Billie Jean', 'plays': 19044517, 'album': 'Thriller'},
]


def playlist_detail(request):
    # To test the {% empty %} message, open  /playlist/?empty=1  (or temporarily pass [] below)
    songs = [] if request.GET.get("empty") == "1" else PLAYLIST
    return render(request, "playlist/playlist_detail.html", {"playlist": songs})
