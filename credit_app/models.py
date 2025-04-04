from django.db import models

class UserCredit(models.Model):
    user_id = models.CharField(max_length=20, unique=True)
    credit_limit = models.FloatField(default=0.00, null=True)
    account_balance = models.FloatField(default=0.00, null=True)

    def __str__(self):
        return self.user_id