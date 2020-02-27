from rest_framework import serializers
from .models import Problem , Session 

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ['problem_no' , 'text','option_A','option_B','option_C','option_D','difficulty']

