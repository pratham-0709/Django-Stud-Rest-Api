from .models import StudentDetails
from rest_framework import serializers 

class SerializeStudent(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentDetails
        fields = ('id', 'name', 'mark1', 'mark2', 'mark3', 'total')

