from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def user_profile(request):
    profile = request.user.profile
    favorites = profile.favorites.all()  # Избранные услуги
    return render(request, 'user/profile.html', {'profile': profile, 'favorites': favorites})
