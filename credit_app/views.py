from django.shortcuts import render
from django.http import JsonResponse
from .models import UserCredit

def get_credit_info(request):
        if request.method == "POST":
                print(f"\n\n\n{request.POST.get("id_no")}\n\n\n")
        return render(request, "credit_app/index.html")
    