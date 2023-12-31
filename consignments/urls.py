from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_consignment, name='new_consignment'),
    path('manage/', views.manage_consignments, name='manage_consignments'),
    path('edit/<int:consignment_id>/', views.edit_consignment,
         name='edit_consignment'),
    path('delete/<int:consignment_id>/', views.delete_consignment,
         name='delete_consignment'),
    path('confirm/<int:consignment_id>/', views.confirm_consignment,
         name='confirm_consignment'),
]
