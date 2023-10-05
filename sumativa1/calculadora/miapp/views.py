from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    if request.method == "POST":
        numero1 = float(request.POST.get("numero1", 0))
        numero2 = float(request.POST.get("numero2", 0))
        operacion = request.POST.get("operacion")

        resultado = calcular_resultado(numero1, numero2, operacion)
        return render(request, "index.html", {"resultado": resultado})
    return render(request, "index.html")


def calculate(request):
    if request.method == "POST":
        numero1 = float(request.POST.get("numero1", 0))
        numero2 = float(request.POST.get("numero2", 0))
        operacion = request.POST.get("operacion")

        resultado = calcular_resultado(numero1, numero2, operacion)
        return render(request, "index.html", {"resultado": resultado})

    return HttpResponse("No se ha podido calcular")

def calcular_resultado(numero1, numero2, operacion):
    if operacion == "sumar":
        return numero1 + numero2
    elif operacion == "restar":
        return numero1 - numero2
    elif operacion == "multiplicar":
        return numero1 * numero2
    elif operacion == "dividir":
        if numero2 == 0:
            return "No se puede dividir por 0"
        return numero1 / numero2
