from django.urls import path
from . import views

name = 'products'
urlpatterns = [
    path("", views.home, name="home"),
    path("category/bathroom/", views.bathroom, name="bathroom"),
    path("category/kitchen/", views.kitchen, name="kitchen"),
    path("category/commercial/", views.commercial, name="commercial"),
    path("category/hardware/", views.hardware, name="hardware"),

    path("category/<str:main_category>/brand/<str:brand_name>", views.brands, name="brands"),
    path("brand/<str:brand_name>/", views.brand, name="brand"),
    path("category/<str:main_category>/subcategory/<str:subcategory_name>", views.sub_category, name="sub_category"),

    path("category/<str:main_category>/addcategory/<str:addcategory_name>/", views.add_category, name="add_category"),
    path("category/<str:main_category>/addcategory/<str:addcategory_name>/supcategory/<str:supcategory_name>",
         views.add_sup_category, name="add_sup_category"),
    path("category/<str:main_category>/addcategory/<str:addcategory_name>/brand/<str:brand_name>",
         views.add_sup_brand, name="add_sup_brand"),

    path("closets/", views.closets, name="closets"),
    path("enclosure/", views.enclosure, name="enclosure"),
    path("no-search/", views.noSearch, name="no_search"),
    path("search/", views.search, name="search"),
    path("category/<str:main_category>/<str:sku>", views.singleProduct, name="single_product"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

    path("cart/", views.cart, name="cart"),
    path("add-to-cart/", views.add_to_cart, name="add_to_cart"),
    path("update-cart/", views.update_cart, name="update_cart"),
    path("remove-cart/<int:id>", views.remove_cart, name="remove_cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("payment/", views.payment, name="payment"),
]
