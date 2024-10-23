# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration
    path('register/', views.registration, name='register'),  # Updated this line to point to the registration view

    # path for login
    path(route='login', view=views.login_user, name='login'),

     # Path for logout
    path(route='logout/', view=views.logout_request, name='logout'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
