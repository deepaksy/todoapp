from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='shopHome'),
    path('about/',views.about,name='AboutUs'),
    path('contact/',views.contact,name='ContactUs'),
    path('tracker/',views.tracker,name='TrackingStatus'),
    path('search/',views.search,name='Search'),
    path('product/',views.prodview,name='ProductView'),
    path('checkout/',views.checkout,name='Checkout'),
    path('login/',views.login,name='Login'),
    path('test/',views.test,name='test'),
    path('cart/',views.cart,name='cart')
]
