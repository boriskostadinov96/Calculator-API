from django.db import models


class RequestLog(models.Model):
    user = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class CalculationResult(models.Model):
    request = models.ForeignKey(RequestLog, on_delete=models.CASCADE)
    result = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
