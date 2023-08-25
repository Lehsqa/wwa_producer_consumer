from rest_framework import serializers
from .models import Order, Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('position', 'probation',)


class OrderSerializer(serializers.ModelSerializer):
    employee = serializers.SerializerMethodField('get_employee')

    class Meta:
        model = Order
        fields = '__all__'

    def get_employee(self, obj):
        try:
            account = Account.objects.get(user=obj.employee)
            position = account.position
        except Account.DoesNotExist:
            position = 'Developer'
        return {
            'first_name': obj.employee.username,
            'position': position
        }
