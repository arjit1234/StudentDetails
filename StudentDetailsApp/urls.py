from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('add_student/',views.add_student_view),
    path('create',views.save_student_data),
    path('edit/<id>',views.edit_view),
    path('update/<id>',views.update_view),
    path('delete/<id>',views.delete_view)
]