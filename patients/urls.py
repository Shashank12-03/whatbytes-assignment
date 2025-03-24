from django.urls import path
from .views import AddPatientView, ListPatientView, GetPatientByIdView, UpdatePatientView, DeletePatientView

urlpatterns = [
    path('', AddPatientView.as_view(), name='add_patient'),
    path('get', ListPatientView.as_view(), name='list_patient'),
    path('<int:pk>/', GetPatientByIdView.as_view(), name='get_patient'),
    path('put/<int:pk>', UpdatePatientView.as_view(), name='update_patient'),
    path('<int:pk>', DeletePatientView.as_view(), name='delete_patient'),
]
