from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama_aplikasi' : 'FootyBall Shop',
        'nama': 'Sean Marcello Maheron',
        'kelas': 'PBP F'
    }

    return render(request, "main.html", context)