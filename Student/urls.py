from django.urls import path
from Student import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add_student', views.add_student, name='add_student'),
    path('delete/<int:id>/', views.delete_data, name='deletedata'),
    path('<int:id>/', views.update_data, name='updatedata'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogout'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('search', views.search, name='search'),
    path('change_password', views.change_password, name='change_password'),
    path('student_acadmics', views.student_acadmics, name='student_acadmics'),
    path('Student_Academics_update_data/<int:id>/', views.Student_Academics_update_data, name='Student_Academics_update_data'),






    

]