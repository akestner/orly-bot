import logging

from pprint import pformat
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

logger = logging.getLogger('testlogger')

class Orly(APIView):
  """
  View to handle Slack POST requests for the /orly slash command
  """

  def post(self, request, format=None):
    logger.info('Orly.post() request:')
    logger.info(pformat(request))
    return Response(None, status=status.HTTP_200_OK)
