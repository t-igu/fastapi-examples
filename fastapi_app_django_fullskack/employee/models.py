from django.db import models
from django.urls import reverse

class TDepartment(models.Model):
    name = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        managed = False
        db_table = 't_department'

    def __str__(self):
        return self.name

class TEmployee(models.Model):
    name = models.CharField(max_length=64, blank=False, null=True)
    birthday = models.DateField(blank=False, null=True)
    department = models.ForeignKey(TDepartment, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        managed = False
        db_table = 't_employee'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        更処理完了時の戻り先URL
        """
        return reverse('employee:index')
