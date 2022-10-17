from django.shortcuts import redirect
from django.http import HttpResponse


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


# def allowed_users(allowed_roles=[]):
#     def decorator(view_function):
#         def wrapper_func(request, *args, **kwargs):
#             group = None
#             if request.user.groups.exists():
#                 group = request.user.groups.all()[0].name
#             if group in allowed_roles:
#                 return view_function(request, *args, **kwargs)
#             else:
#                 return HttpResponse('Vous n\'etez pas autorisée a visiter cette page !')
#         return wrapper_func
#
#     return decorator
