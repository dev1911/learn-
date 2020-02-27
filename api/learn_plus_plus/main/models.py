from django.db import models

# Create your models here.

class Test(models.Model):
    test_id = models.AutoField(primary_key=True)

class Problem(models.Model):
    problem_id = models.AutoField(primary_key=True)
    problem_no = models.IntegerField(blank=False , null=False)
    option_A = models.CharField(max_length=100)
    option_B = models.CharField(max_length=100)
    option_C = models.CharField(max_length=100)
    option_D = models.CharField(max_length=100)
    answer = models.CharField(max_length=1)
    difficulty = models.IntegerField(blank=False , null=False)
    threshold = models.IntegerField(blank=False,null=False)
    text = models.CharField(max_length=500)
    test = models.ForeignKey(Test ,on_delete=models.CASCADE)

class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User , on_delete=models.CASCADE)
    test_id = models.ForeignKey(Test , on_delete=models.CASCADE)
    start_time = models.TimeField(auto_now=True)
    total_time_taken = models.IntegerField()
    log_file_path = models.CharField(max_length=100)

