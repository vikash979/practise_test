from django.db import models
from django.conf import settings

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
#from users.models import CustomUser
from django.conf import settings

class UserDetail(models.Model):
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name =  models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Borrower(models.Model):
	borrower_user = models.ForeignKey(UserDetail,related_name='borrowers',  on_delete=models.CASCADE)
	owes_to = models.ForeignKey(UserDetail,related_name='owes',  on_delete=models.CASCADE)
	amount = models.FloatField(blank=True, null=True)

	def __str__(self):
		return self.owes_to.name


class BorrowedBy(models.Model):
	borrower_user = models.ForeignKey(UserDetail,related_name='borrows',  on_delete=models.CASCADE)
	owes_by = models.ForeignKey(UserDetail,related_name='owes_by',  on_delete=models.CASCADE)
	amount = models.FloatField(blank=True, null=True)
