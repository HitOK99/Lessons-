from django.shortcuts import render

def sing_up_in(request):
    return render(request, 'sing_up_in/sing_up_in.html')

def sing_in(request):
    return render(request, 'sing_up_in/sing_in.html')

def main_work_window(request):
    return render(request, 'main_work_window/main_work_window.html')