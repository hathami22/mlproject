"""
URL configuration for mlprojet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from PublicpriveApp import views as public_views
from YassinApp import views as viewsyassin
from PerformanceApp import views as performance_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cantine/', include('CantineApp.urls')),
    path('formation/', include('FormationApp.urls')), 
    path('', public_views.home, name='home'),
    path('ml/', include('BoardinPlusIfRulesApp.urls')),
    path('ObjectiveYassin2/', viewsyassin.objective_yassin2, name='objective_yassin2'),
    path('ObjectiveYassin1/', viewsyassin.objective_yassin1, name='objective_yassin1'),
    
    path('api/extract_csv_data/', viewsyassin.extract_csv_data, name='extract_csv_data'),
    path('api/run_prediction/', viewsyassin.run_prediction, name='run_prediction'),
    path('api/extract_csv_data_yassin2/', viewsyassin.extract_csv_data_yassin2, name='extract_csv_data_yassin2'),
    path('api/run_prediction_yassin2/', viewsyassin.run_prediction_yassin2, name='run_prediction_yassin2'),
    path('temporal-trajectory-clustering/', performance_views.temporal_trajectory_clustering, name='temporal_trajectory_clustering'),
    path('school-ranking-by-score/', performance_views.school_ranking_by_score, name='school_ranking_by_score'),
]