from django.shortcuts import render, get_object_or_404
from .models import Publicacion


# Create your views here.
def index(request):
    publicaciones = Publicacion.objects.all().order_by('-fecha').values()
    context = {
        'publicaciones': publicaciones
    }
    return render(request, 'index.html', context)


def blog(request):
    publicaciones = Publicacion.objects.all().order_by('-fecha')
    ultima_publicacion = publicaciones.first()
    context = {
        'publicaciones': publicaciones,
        'ultima_publicacion': ultima_publicacion
    }
    return render(request, 'index.html', context)

def detalle_publicacion(request, publicacion_id):
    publicacion = get_object_or_404(Publicacion, pk=publicacion_id)
    return render(request, 'detalle_publicacion.html', {'publicacion': publicacion})