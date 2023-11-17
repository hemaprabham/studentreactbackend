from rest_framework import serializers
from students.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name',
            'admno',
            'rollno',
            'college'
        )
            