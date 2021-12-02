from django.urls import path
from . import views

urlpatterns = [
    path('', views.training_home, name='training_home'),
    path('update', views.update, name='update'),
    path('<int:pk>', views.TrainingDetailView.as_view(), name='training-detail'),
    path('<int:pk>/upgrade', views.TrainingUpgradeView.as_view(), name='training-upgrade'),
]
