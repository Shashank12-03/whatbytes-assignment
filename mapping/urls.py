from django.urls import path
from .views import CreateMappingView, ListMappingsView, GetMappingsByPatientView, DeleteMappingView

urlpatterns = [
    path('', CreateMappingView.as_view(), name='create_mapping'),
    path('get', ListMappingsView.as_view(), name='list_mappings'),
    path('<int:patient_id>/', GetMappingsByPatientView.as_view(), name='get_mappings_by_patient'),
    path('<int:id>', DeleteMappingView.as_view(), name='delete_mapping'),
]