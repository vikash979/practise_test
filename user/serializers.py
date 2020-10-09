from rest_framework import serializers
from .models import UserDetail, Borrower, BorrowedBy
from django.db.models import Sum


class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = '__all__'

class UserDetailSerializer(serializers.ModelSerializer):
	owes = serializers.SerializerMethodField()
	owed_by = serializers.SerializerMethodField()

	# borrowers  = BorrowerSerializer(many=True)
	balance  = serializers.SerializerMethodField()
	class Meta:
		model = UserDetail
		fields = ['name','owes', 'owed_by','balance']

	def get_owes(self,obj):
		borr  =  Borrower.objects.filter(borrower_user_id=obj.id).values()
		user_obj  = []
		dicts = {}
		for x in borr:
			use  = UserDetail.objects.filter(id=x['owes_to_id']).values('name')
			users = {use[0]['name']: x['amount']}
			dicts = {**dicts, **users}
		user_obj.append(dicts)


		return (user_obj[0])

	def get_owed_by(self,obj):
		borr  =  BorrowedBy.objects.filter(borrower_user_id=obj.id).values()
		user_obj  = []
		dicts = {}
		for x in borr:
			use  = UserDetail.objects.filter(id=x['owes_by_id']).values('name')
			users = {use[0]['name']: x['amount']}
			dicts = {**dicts, **users}
		user_obj.append(dicts)
		return (user_obj[0])

	def total(self):
		return ("hello")
	def get_balance(self,obj):
		owed_to  =  Borrower.objects.filter(borrower_user_id=obj.id).aggregate(Sum('amount'))

		owed_by  =  BorrowedBy.objects.filter(borrower_user_id=obj.id).aggregate(Sum('amount'))
		ownedby = owed_by.get('amount__sum',0)
		ownedto = owed_to.get('amount__sum',0)

		if type(ownedby) == float:
			ownedby = ownedby
		else:
			ownedby = 0

		if type(ownedto) == float:
			ownedto = ownedto
		else:
			ownedto = 0
		total  = ownedby - ownedto

		return(total)
