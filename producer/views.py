from django.shortcuts import render


def create_producer(request):
    if request.method == "POST":
        pass
    return render(request, 'Producer/CreateProducer.html')