from django.urls import path
from django.contrib.auth.views import LogoutView
from App1 import views

urlpatterns = [
   
    path("", views.inicio, name="Inicio"),
    path("users/", views.UsersList.as_view(), name="Users"),
    path("games/", views.GamesList.as_view(), name="Games"),
    path("creators/", views.CreatorsList.as_view(), name="Creators"),
    path('browsingGames/', views.browsingGames, name='BrowsingGames'),
    path('search/', views.search),
    path("searchCreators/",views.searchCreators),
    path("searchUsers/",views.searchUsers),
    path('games/list', views.GamesList.as_view(), name='ListGames'),
    path(r'^detailsgames(?P<pk>\d+)$', views.GamesDetail.as_view(), name='DetailGames'),
    path(r'^newgames$', views.GamesCreation.as_view(), name='NewGames'),
    path(r'^editgames/(?P<pk>\d+)$', views.GamesUpdate.as_view(), name='EditGames'),
    path(r'^deletegames/(?P<pk>\d+)$', views.GamesDelete.as_view(), name='DeleteGames'),
    path('creators/list', views.CreatorsList.as_view(), name='ListCreators'),
    path(r'^detailscreators(?P<pk>\d+)$', views.CreatorsDetail.as_view(), name='DetailCreators'),
    path(r'^newcreators$', views.CreatorsCreation.as_view(), name='NewCreators'),
    path(r'^editcreators/(?P<pk>\d+)$', views.CreatorsUpdate.as_view(), name='EditCreators'),
    path(r'^deletecreators/(?P<pk>\d+)$', views.CreatorsDelete.as_view(), name='DeleteCreators'),
    path('users/list', views.UsersList.as_view(), name='ListUsers'),
    path(r'^detailsusers(?P<pk>\d+)$', views.UsersDetail.as_view(), name='DetailUsers'),
    path(r'^newusers$', views.UsersCreation.as_view(), name='NewUsers'),
    path(r'^editusers/(?P<pk>\d+)$', views.UsersUpdate.as_view(), name='EditUsers'),
    path(r'^deleteusers/(?P<pk>\d+)$', views.UsersDelete.as_view(), name='DeleteUsers'),
    path('login', views.login_request, name = 'Login'),
    path('register', views.register, name = 'Register'),
    path('logout', LogoutView.as_view(template_name='App1/logout.html'), name='Logout'),
    path('about/',views.about,name='About'),
    path('community/',views.community,name="Community"),
    path('editUser/',views.editUser,name='editUser'),

]