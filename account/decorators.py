from django.shortcuts import redirect


def user_not_authenticated(function=None, redirect_url='user:user_home'):
    """

    :param function:
    :param redirect_url:
    :return:
    """
    def decorator(view_function):
        def wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_url)
            return view_function(request, *args, **kwargs)
        return wrapped_view

    if function:
        return decorator(function)

    return decorator

