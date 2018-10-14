from rest_framework import serializers
from appointment_book.models import Appointment


class AppointmentSerializer (serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ('id', 'name', 'date', 'notes', 'age')