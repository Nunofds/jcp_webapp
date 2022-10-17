from django.shortcuts import redirect


def user_not_authenticated(function=None):
    """

    :param function:
    :return:
    """

    def decorator(view_function):
        def wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect('user:user_home', request.user.id)
            else:
                return view_function(request, *args, **kwargs)

        return wrapped_view

    if function:
        return decorator(function)

    return decorator


def allowed_users(allowed_roles=[]):
    def decorator(view_function):
        def wrapper_func(request, *args, **kwargs):
            return view_function(request, *args, **kwargs)

        return wrapper_func

    return decorator
