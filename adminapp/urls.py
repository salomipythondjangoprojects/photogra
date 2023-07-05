from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('topsongs',views.topsongfn,name='topsongfn'),
    path('detail/<int:music_id>/',views.detailfn,name='detailfn'),
    path('detailz/<int:musicz_id>/',views.detailfnz,name='detailfnz'),
    path('about',views.aboutfn,name='aboutfn'),
    path('contact',views.contactfn,name='contactfn'),
    path('premium',views.premiumfn,name='premiumfn')
]