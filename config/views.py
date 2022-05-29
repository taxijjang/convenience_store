from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def api_gate_way_response(request):
    return Response({"message": "OK"})
