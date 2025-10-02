def user_data(request):
    return {
        'username': request.session.get('username'),
        'profile_pic': request.session.get('profile_pic')
    }
