import csv
import io
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import RequestLog, CalculationResult

AUTH_PASSPHRASE = "Jf8s!j9L2fS0K"


@csrf_exempt
def upload_file(request):
    auth_header = request.headers.get("Authorization")

    # Authorization check
    if auth_header != AUTH_PASSPHRASE:
        return JsonResponse({"error": "Unauthorized"}, status=401)

    # Check for POST request and ensure file is uploaded
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']

        # Ensure the file is a CSV
        if not uploaded_file.name.endswith('.csv'):
            return JsonResponse({"error": "Invalid file format. Please upload a CSV file."}, status=400)

        try:
            # Decode file contents and read the CSV
            file_data = uploaded_file.read().decode('utf-8')
            io_string = io.StringIO(file_data)
            reader = csv.reader(io_string, delimiter=',')

            total_sum = 0  # Initialize total for summing up calculations
            header = True  # To skip the header if necessary

            for row in reader:
                # Skip header row, if present
                if header:
                    header = False
                    continue

                # Skip rows that do not have 3 columns
                if len(row) != 3:
                    continue

                # Parse values from CSV
                try:
                    left_operand = float(row[0].strip())
                    operator = row[1].strip()
                    right_operand = float(row[2].strip())
                except ValueError:
                    return JsonResponse({"error": "Invalid data format in the CSV."}, status=400)

                # Perform calculations
                if operator == '+':
                    total_sum += left_operand + right_operand
                elif operator == '-':
                    total_sum += left_operand - right_operand
                elif operator == '*':
                    total_sum += left_operand * right_operand
                elif operator == '/':
                    if right_operand == 0:
                        return JsonResponse({"error": "Division by zero is not allowed."}, status=400)
                    total_sum += left_operand / right_operand
                else:
                    continue  # Skip if the operator is unrecognized

            # Save request log and result to the database
            request_log = RequestLog.objects.create(user="example_user", name=uploaded_file.name)
            CalculationResult.objects.create(request=request_log, result=total_sum)

            # Return success response with the result
            return JsonResponse({
                "message": "File processed successfully",
                "result": total_sum  # Include the final result in the response
            }, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    # Invalid request
    return JsonResponse({"error": "Invalid request"}, status=400)


def admin_ui(request):
    # Fetch all request logs and calculation results
    request_logs = RequestLog.objects.all()
    calculation_results = CalculationResult.objects.all()

    return render(request, 'admin_ui.html', {
        'request_logs': request_logs,
        'calculation_results': calculation_results,
    })
