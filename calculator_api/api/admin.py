from django.contrib import admin
from .models import RequestLog, CalculationResult

admin.site.register(RequestLog)
admin.site.register(CalculationResult)