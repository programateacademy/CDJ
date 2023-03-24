from django.urls import path
from . import views

app_name= 'login'

urlpatterns = [
    path("panel/", views.panel_admin, name="panel_admin"),
    path("create_post/", views.create_post, name="create_post"),
    path("delete_post/<int:post_id>", views.delete_post, name="delete_post"),
    path("update_post/<int:post_id>", views.update_post, name="update_post"),
    path("create_document/", views.create_document, name="create_document"),
    path("delete_document/<int:documents_id>", views.delete_document, name="delete_document"),
    path("create_banner/", views.create_banner, name="create_banner"),
    path("delete_banner/<int:banner_id>", views.delete_banner, name="delete_banner"),
    path("create_about/", views.create_about, name="create_about"),
    path("update_about/<int:aboutus_id>", views.update_about, name="update_about"),
    path("create_collaborator/", views.create_collaborator, name="create_collaborator"),
    path("delete_collaborator/<int:collaborators_id>", views.delete_collaborator, name="delete_collaborator"),
    path("update_collaborator/<int:collaborators_id>", views.update_collaborator, name="update_collaborator"),
    # =======================
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
]