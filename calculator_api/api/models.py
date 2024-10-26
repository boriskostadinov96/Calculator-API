from django.db import models


class RequestLog(models.Model):
    user = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request by {self.user} for file '{self.name}'"


class CalculationResult(models.Model):
    request = models.ForeignKey(RequestLog, on_delete=models.CASCADE)
    result = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result {self.result} for Request ID {self.request.id}"
