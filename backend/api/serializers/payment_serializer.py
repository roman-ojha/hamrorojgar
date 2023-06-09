from rest_framework import serializers
# from api.models.payment import Payment
# from api.models.job_application import JobApplication
# from api.models.citizen import User
# from api.models.payment_gateway import PaymentGateway
from api.models import payment, job_application, user, payment_gateway


class PaymentSerializer(serializers.ModelSerializer):
    by = user.User()
    payment_using = payment_gateway.PaymentGateway()
    for_application = job_application.JobApplication()

    class Meta:
        model = payment.Payment
        fields = ['amount', 'payment_using', 'from_acc', 'status',
                  'payment_id', 'transaction_id', 'by', 'for_application']
