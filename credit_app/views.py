from django.shortcuts import render
from django.http import JsonResponse
from .models import UserCredit

def get_credit_info(request):
    
        # user = UserCredit.objects.get(user_id=user_id)
        # data = {
        #     'credit_limit': str(user.credit_limit),
        #     'account_balance': str(user.account_balance),
        # }
        return render(request, "credit_app/index.html")
    