from rest_framework.response import Response

def GenericResponse(response, data, status = 200):
    if(type(response) is str):
        return Response({
        "response": response,
        "data": data,
        "status": status }, status=status)
    else:
        return Response({ "response": response,
            "data": data,
            "status": status }, status=status)