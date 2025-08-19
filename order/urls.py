
from django.urls import path

from order.views import OrderCreateListView, OrderCredentialDownloadView

urlpatterns = [
    path('create_list_order', OrderCreateListView.as_view(), name='create_view'),
    path('orders/<int:pk>/download_credentials/', OrderCredentialDownloadView.as_view(),
         name='order-credential-download'),

]
