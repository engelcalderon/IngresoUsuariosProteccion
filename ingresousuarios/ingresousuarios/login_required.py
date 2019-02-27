from functools import wraps
from django.http import HttpResponseForbidden, HttpResponseRedirect
from jose import jwt

def login_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if 'accessToken' in request.COOKIES:
            try:
                access_token = request.COOKIES['accessToken']

                request.user = jwt.decode(access_token, 'secret123', algorithms='HS256')

                return function(request, *args, **kwargs)

            except KeyError as k:
                # raise Exception('A valid token is required')
                return HttpResponseForbidden()
            except jwt.ExpiredSignatureError as es:
                # raise Exception('Token expired')
                return HttpResponseForbidden()
            except jwt.JWSError as je:
                # raise Exception('Invalid token')
                return HttpResponseForbidden()
            except jwt.JWTClaimsError as jce:
                # raise Exception('Invalid token')
                return HttpResponseForbidden()
            except jwt.JWTError as jwtE:
                return HttpResponseForbidden()
        else:
            return HttpResponseRedirect('/')
    return wrap