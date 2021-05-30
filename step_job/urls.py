from django.urls import path


from .views import custom_handler400,custom_handler500,custom_handler403,custom_handler404

handler400 = custom_handler400
handler403 = custom_handler403
handler404 = custom_handler404
handler500 = custom_handler500

# urlpatterns = [
#     path('', views.main_view, name="main"),
#
#     path('departure/<str:name>/', views.__, name="departure"),
#     path('tour/<int:name>/', views.__, name="tour"),
# ]