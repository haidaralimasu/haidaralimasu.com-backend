from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView
from portfolio.models import Portfolio
from portfolio.serializers import PortfolioSerializer


class PortfolioListView(ListAPIView):
    queryset = Portfolio.objects.order_by('id')
    serializer_class = PortfolioSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )
