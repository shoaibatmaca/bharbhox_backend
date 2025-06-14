"""
URL configuration for core project.

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
from django.urls import path
from main.views import * 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/signup/', SignupWithDogView.as_view(), name='signup-with-dog'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/checkout/', OrderCheckoutView.as_view(), name='checkout'),
    path('api/user/profile/', UserProfileView.as_view(), name='user-profile'),
    path('api/dog/profile/', DogProfileView.as_view(), name='dog-profile'),
    path('api/send-email/', SendEmailAPIView.as_view(), name='send-email'),
    path('api/box-history/', UserBoxHistoryView.as_view(), name='box-history'),
    path('api/skip-box/', SkipBoxView.as_view(), name='skip-box'),
    path('api/rate-box/<int:box_id>/', rate_box),
    path('api/current-subscription/', CurrentSubscriptionView.as_view()),


]

