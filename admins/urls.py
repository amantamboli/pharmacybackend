from django.urls import path
from . import views

urlpatterns = [
    # path('',views.admininfo),
    # path('<int:pk>',views.userAdminDetailAPIView.as_view()),
    # path('create/',views.userAdminCreateAPIView.as_view())

    path('create/', views.UserAdminCreateView.as_view()),
    path('all/', views.UserAdminListView.as_view(), name='useradmin-list-all'),
    path('destroy/<str:user_id>/', views.UserAdminDestroyView.as_view(), name='useradmin-delete'),
    path('update/<str:user_id>/', views.UserAdminUpdateView.as_view(), name='useradmin-update'),

]
