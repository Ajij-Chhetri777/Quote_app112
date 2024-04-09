from django.urls import path
from app.views import home, quote_view, post, login, register, ping, add_favourite, favourite_quotes, delete_favourite, edit_quote, delete_quote

urlpatterns = [
    path('',home,name= 'home' ),
    path('<int:id1>/',quote_view, name = 'quote_view'),
    path('post/', post ,name= 'post' ),
    path('login/', login , name = 'login'),
    path('register/', register, name = 'register'), 
    path('ping/<uuid:key>/',ping, name= 'ping'),
    path('<uuid:key>/',add_favourite, name = 'add_favourite'),
    path('favourite/',favourite_quotes,name= 'favourite_quotes'),
    path('favourite/<int:id>',delete_favourite , name = 'delete_favourite'),
    path('update/<uuid:key>/',edit_quote, name= 'edit_quote'),
    path('delete/<uuid:key>/',delete_quote,name = 'delete_quote'),

]
