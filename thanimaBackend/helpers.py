from rest_framework.response import Response

def GenericResponse(response, data, status = 200):
    return Response({
    "message": response,
    "data": data,
    "status": status }, status=status)