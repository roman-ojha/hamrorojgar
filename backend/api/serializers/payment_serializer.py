from rest_framework import serializers
from api.models.payment import Payment
from api.models.job_application import JobApplication
from api.models.citizen import User
from api.models.payment_gateway import PaymentGateway


class PaymentSerializer(serializers.ModelSerializer):
    by = User
    payment_using = PaymentGateway()
    for_application = JobApplication()

    class Meta:
        model = Payment
        fields = ['amount', 'payment_using', 'from_acc', 'status',
                  'payment_id', 'transaction_id', 'by', 'for_application']
