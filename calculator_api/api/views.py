from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_file(request):
    AUTH_PASSPHRASE = "Jf8s!j9L2fS0K"
    auth_header = request.headers.get("Authorization")

    if auth_header != AUTH_PASSPHRASE:
        return JsonResponse({"error": "Unauthorized"}, status=401)

    return JsonResponse({"message": "File received"}, status=200)
