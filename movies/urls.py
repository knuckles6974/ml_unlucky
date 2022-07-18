from django.urls import path
from .views import (
       MovieImageView,
       MovieInfoView, 
       MovieVideoView,
       InformationView,
       MovieRepairView
) 

urlpatterns = [
    path('/movieinfo', MovieInfoView.as_view()),
    path('/movieimage', MovieImageView.as_view()),
    path('/movievideo', MovieVideoView.as_view()),
    path('/movieinfo/<int:movieinfo_id>', InformationView.as_view()),
    path('/<int:movieinfo_id>', MovieRepairView.as_view())  
 ]
