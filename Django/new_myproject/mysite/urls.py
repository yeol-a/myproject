"""new_myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from polls import views 

#app_name='polls'

urlpatterns = [
    path('admin/', admin.site.urls),
    # polls 경로로 요청이 오면, views의 index를 불러옴. name은 별칭 
    path('polls/', views.index, name="index"),
    path('polls/<int:question_id>/', views.detail, name="detail"),
    path('polls/<int:question_id>/vote', views.vote, name="vote"),
    path('polls/<int:question_id>/results', views.results, name="result")
]
