from . import views

urlpatterns =[
    path('', views.home_page, name='home'),
    path('', views.login_page, name='login'),
    path('', views.register_page, name='register'),
    path('', views.success_page, name='success'),
    path('', views.token_send_page, name='token_send'),
    path('', views.error, name='error'),
]