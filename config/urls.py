from django.contrib import admin
from django.urls import path

from app.views import hey, how_old, good_burger

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hey/<name>/", hey),
    path("age-in/<int:end>/<int:birthyear>/", how_old),
    path("order-total/<int:burgers>/<int:fries>/<int:drinks>/", good_burger),
]