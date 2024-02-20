from curdapp import views
from django.urls import path

urlpatterns = [
    path("", views.add_data),
    path("home", views.home),
    path("add", views.add_data),
    path("del_data/<int:emp_id>", views.del_data),
    path("edit_data/<int:emp_id>", views.edit_data),
    path("do_edit_data/<int:emp_id>", views.do_edit_data),
]