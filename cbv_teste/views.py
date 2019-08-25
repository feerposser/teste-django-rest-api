from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CBVTeste(APIView):

    

    def get(self, request, format=None):
        l = {'t':[]}
        l['t'].append(request.query_params.get('teste', None))

        return Response(l, status=status.HTTP_200_OK)


