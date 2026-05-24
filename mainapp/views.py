from django.shortcuts import render

from django.shortcuts import render
from .models import (
    HomePageSetting,
    HeroSlide,
    IntroPoint,
    IntroStatCard,
    Invoice,
    Service,
    ShopInvoice,
    ShopReceipt,
    SoftwareProduct,
    FeatureItem,
    PricingPlan,
    ClientLogo,
    FooterLinkGroup,
)
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from weasyprint import HTML, CSS

from .models import Receipt, HomePageSetting


def home(request):
    homepage, _ = HomePageSetting.objects.get_or_create(pk=1)

    context = {
        "homepage": homepage,
        "hero_slides": HeroSlide.objects.filter(is_active=True).order_by("order", "id"),
        "intro_points": IntroPoint.objects.filter(is_active=True).order_by("order", "id"),
        "intro_stats": IntroStatCard.objects.filter(is_active=True).order_by("order", "id"),
        "services": Service.objects.filter(is_active=True).order_by("order", "id"),
        "products": SoftwareProduct.objects.filter(is_active=True).order_by("order", "id"),
        "feature_items": FeatureItem.objects.filter(is_active=True).order_by("order", "id"),
        "pricing_plans": PricingPlan.objects.filter(is_active=True).prefetch_related("features").order_by("order", "id"),
        "client_logos_row_1": ClientLogo.objects.filter(is_active=True, row=1).order_by("order", "id"),
        "client_logos_row_2": ClientLogo.objects.filter(is_active=True, row=2).order_by("order", "id"),
        "footer_groups": FooterLinkGroup.objects.filter(is_active=True).prefetch_related("links").order_by("order", "id"),
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def receipt_pdf_view(request, pk):
    receipt = get_object_or_404(
        Receipt.objects.select_related("invoice").prefetch_related("items"),
        pk=pk
    )
    company = HomePageSetting.load()

    html_string = render_to_string("receipts/receipt_pdf.html", {
        "receipt": receipt,
        "company": company,
        "request": request,
    })

    pdf_file = HTML(
        string=html_string,
        base_url=request.build_absolute_uri("/")
    ).write_pdf()

    response = HttpResponse(pdf_file, content_type="application/pdf")
    response["Content-Disposition"] = f'inline; filename="{receipt.receipt_number}.pdf"'
    return response



def invoice_pdf_view(request, pk):
    invoice = get_object_or_404(Invoice.objects.prefetch_related("items"), pk=pk)
    company = HomePageSetting.load()

    html_string = render_to_string("invoices/invoice_pdf.html", {
        "invoice": invoice,
        "company": company,
        "request": request,
    })

    pdf_file = HTML(
        string=html_string,
        base_url=request.build_absolute_uri("/")
    ).write_pdf()

    response = HttpResponse(pdf_file, content_type="application/pdf")
    response["Content-Disposition"] = f'inline; filename="{invoice.invoice_number}.pdf"'
    return response




def shop_invoice_pdf(request, pk):
    invoice = get_object_or_404(
        ShopInvoice.objects.prefetch_related("items"),
        pk=pk
    )

    html_string = render_to_string(
        "shop/invoice_pdf.html",
        {
            "invoice": invoice,
        }
    )

    pdf_file = HTML(
        string=html_string,
        base_url=request.build_absolute_uri("/")
    ).write_pdf()

    response = HttpResponse(
        pdf_file,
        content_type="application/pdf"
    )

    response["Content-Disposition"] = (
        f'inline; filename="{invoice.invoice_number}.pdf"'
    )

    return response


def shop_receipt_pdf(request, pk):
    receipt = get_object_or_404(
        ShopReceipt.objects.select_related("invoice"),
        pk=pk
    )

    html_string = render_to_string(
        "shop/receipt_pdf.html",
        {
            "receipt": receipt,
        }
    )

    pdf_file = HTML(
        string=html_string,
        base_url=request.build_absolute_uri("/")
    ).write_pdf()

    response = HttpResponse(
        pdf_file,
        content_type="application/pdf"
    )

    response["Content-Disposition"] = (
        f'inline; filename="{receipt.receipt_number}.pdf"'
    )

    return response