from django.contrib import admin
from .models import UserDetail, Borrower, BorrowedBy

admin.site.register(UserDetail)
admin.site.register(Borrower)
admin.site.register(BorrowedBy)

# Register your models here.
