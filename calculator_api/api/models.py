from django.db import models


# Model to log each file upload request
class RequestLog(models.Model):
    user = models.CharField(max_length=100)  # Placeholder for user identification
    name = models.CharField(max_length=255)  # Name of the uploaded file
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set timestamp on creation

    def __str__(self):
        return f"Request by {self.user} for file '{self.name}'"


# Model to store calculation results related to a RequestLog
class CalculationResult(models.Model):
    request = models.ForeignKey(RequestLog, on_delete=models.CASCADE)  # Link to RequestLog
    result = models.FloatField()  # Calculation result
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when result is stored

    def __str__(self):
        return f"Result {self.result} for Request ID {self.request.id}"
