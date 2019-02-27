from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from jose import jwt
from .models import Usuario
from ingresousuarios.login_required import login_required

def index(request):

    context = {
        'errores': []
    }

    redirectProfile = redirect('profile')

    if request.method == 'POST':
        try:
            form = request.POST

            usuario = Usuario.objects.get(correo_electronico=form['email'])
            if check_password(form['pass'], usuario.contrasena):
                access_token = jwt.encode({'auth_user': usuario.pk}, 'secret123', algorithm='HS256')
                redirectProfile.set_cookie('accessToken', access_token)
                return redirectProfile

        except Usuario.DoesNotExist:
            context['errores'].append('Usuario no existe')
        except Exception as e:
            raise Exception(str(e))

    return render(request, 'index.html', context)

def registro(request):
    context = {
        'errores': []
    }

    redirectProfile = redirect('profile')

    if request.method == 'POST':
        try:
            form = request.POST

            usuario = Usuario.objects.create(nombre=form['name'], correo_electronico=form['email'],
                                             contrasena=make_password(form['pass']))
            access_token = jwt.encode({'auth_user': usuario.pk}, 'secret123', algorithm='HS256')
            redirectProfile.set_cookie('accessToken', access_token)
            return redirectProfile

        except Exception as e:
            raise Exception(str(e))

    return render(request, 'registro.html', context)

@login_required
def profile(request):
    context = {}
    return render(request, 'profile.html', context)