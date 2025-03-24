from django.urls import path
from .views import AddDoctorView, ListDoctorView, GetDoctorByIdView, UpdateDoctorView, DeleteDoctorView

urlpatterns = [
    path('', AddDoctorView.as_view(), name='add_patient'),
    path('get', ListDoctorView.as_view(), name='list_patient'),
    path('<int:pk>', GetDoctorByIdView.as_view(), name='get_patient'),
    path('update/<int:pk>', UpdateDoctorView.as_view(), name='update_patient'),
    path('delete/<int:pk>', DeleteDoctorView.as_view(), name='delete_patient'),
]
