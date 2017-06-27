from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index' ),
    #przepis/categori_id/
    url(r'^(?P<category_id>[0-9]+)/$',views.detail,name='detail'),
    #przepis/category_id/dish_id/
    url(r'^(?P<category_id>[0-9]+)/(?P<dish_id>[0-9]+)/$',views.receipe,name='receipe'),
    #przepis/add
    url(r'^add/$', views.DishCreate.as_view(), name="dish_add"),
    #przepis/category_add
    url(r'^add_category/$', views.CategoryCreate.as_view(), name="category_add"),


    #przepis/
    #url(r'^przepis/(?P<category_id>[0-9]+)/(?P<dish_id>[0-9]+)/$', views.DishUpdate.as_view(), name="category_update"),
    #delete
    #url(r'przepis/(?P<category_id>[0-9]+)/$', views.DishDelete.as_view(), name="dish_delete"),

    url(r'^register/$',views.UserFormView.as_view(),name='register'),


]