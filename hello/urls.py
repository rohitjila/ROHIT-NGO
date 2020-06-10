from django.urls import path
from . import views

urlpatterns=[
    path('help',views.help, name='help'),
    path('warriors',views.warriors, name='warriors'),
    path('create',views.create, name='create'),
    path('<int:product_id>',views.detail, name='detail'),
    path('<int:product_id>/upvote',views.upvote, name='upvote'),
    
]    