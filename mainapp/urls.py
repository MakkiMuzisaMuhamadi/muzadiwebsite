from django.urls import path

from mainapp.views import *

urlpatterns = [
    path('', home, name='home'),
    path('muzadi-tech/about-us', about, name='about'),
    path('muzadi-tech/services', services, name='services'),
    path('muzadi-tech/contact-us', contact, name='contact'),
    path('muzadi-tech/blog', blog, name='blog'),
    path("receipts/<int:pk>/pdf/", receipt_pdf_view, name="admin_receipt_pdf"),
    path("invoices/<int:pk>/pdf/", invoice_pdf_view, name="admin_invoice_pdf"),
]