import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

logger = logging.getLogger(__name__)

class Orly(APIView):
  """
  View to handle Slack POST requests for the /orly slash command
  """

  def post(self, request, format=None):
    logger.info(request.data)
    return Response(None, status=status.HTTP_200_OK)
