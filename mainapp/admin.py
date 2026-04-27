from django.contrib import admin
from django.utils.html import format_html

from .models import (
    HomePageSetting,
    HeroSlide,
    IntroPoint,
    IntroStatCard,
    Invoice,
    InvoiceItem,
    Service,
    SoftwareProduct,
    FeatureItem,
    PricingPlan,
    PricingPlanFeature,
    ClientLogo,
    FooterLinkGroup,
    FooterLink,
    Receipt,
    ReceiptItem,
)


class PricingPlanFeatureInline(admin.TabularInline):
    model = PricingPlanFeature
    extra = 1


class FooterLinkInline(admin.TabularInline):
    model = FooterLink
    extra = 1


class ReceiptItemInline(admin.TabularInline):
    model = ReceiptItem
    extra = 1


@admin.register(HomePageSetting)
class HomePageSettingAdmin(admin.ModelAdmin):
    fieldsets = (
        ("SEO & Branding", {
            "fields": (
                "site_title",
                "meta_keywords",
                "meta_description",
                "meta_author",
                "company_name",
                "tagline",
                "logo",
                "favicon",
            )
        }),
        ("Contact", {
            "fields": (
                "phone_number",
                "whatsapp_number",
                "email",
                "website_url",
                "address",
                "facebook_url",
                "instagram_url",
                "linkedin_url",
            )
        }),
        ("Intro", {
            "fields": (
                "intro_badge",
                "intro_heading",
                "intro_text_1",
                "intro_text_2",
            )
        }),
        ("Services", {
            "fields": (
                "services_title",
                "services_subtitle",
            )
        }),
        ("Products", {
            "fields": (
                "products_title",
                "products_subtitle",
            )
        }),
        ("Features", {
            "fields": (
                "features_title",
                "features_subtitle",
                "features_image",
            )
        }),
        ("Pricing", {
            "fields": (
                "pricing_title",
                "pricing_subtitle",
            )
        }),
        ("Clients", {
            "fields": (
                "clients_title",
                "clients_subtitle",
                "clients_intro",
                "clients_note",
            )
        }),
        ("CTA", {
            "fields": (
                "cta_badge",
                "cta_heading",
                "cta_text",
                "cta_button_text",
                "cta_button_url",
                "cta_whatsapp_text",
            )
        }),
        ("Footer", {
            "fields": (
                "footer_about",
                "footer_copyright",
            )
        }),
    )


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(IntroPoint)
class IntroPointAdmin(admin.ModelAdmin):
    list_display = ("text", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(IntroStatCard)
class IntroStatCardAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(SoftwareProduct)
class SoftwareProductAdmin(admin.ModelAdmin):
    list_display = ("title", "tag", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(FeatureItem)
class FeatureItemAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ("title", "price_text", "is_featured", "order", "is_active")
    list_editable = ("is_featured", "order", "is_active")
    inlines = [PricingPlanFeatureInline]


@admin.register(ClientLogo)
class ClientLogoAdmin(admin.ModelAdmin):
    list_display = ("name", "row", "order", "is_active")
    list_editable = ("row", "order", "is_active")


@admin.register(FooterLinkGroup)
class FooterLinkGroupAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")
    inlines = [FooterLinkInline]


class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        "invoice_number",
        "client_name",
        "issued_date",
        "due_date",
        "total_amount_display",
        "amount_paid_display",
        "balance_display",
        "status",
        "download_pdf_link",
    )
    list_filter = ("status", "issued_date", "due_date", "currency")
    search_fields = ("invoice_number", "client_name", "client_email", "client_phone")
    inlines = [InvoiceItemInline]
    readonly_fields = ("invoice_number", "pdf_preview_link")

    fieldsets = (
        ("Invoice Info", {
            "fields": (
                "invoice_number",
                "status",
                "issued_date",
                "due_date",
                "currency",
            )
        }),
        ("Client Details", {
            "fields": (
                "client_name",
                "client_email",
                "client_phone",
                "client_address",
            )
        }),
        ("Payment Details", {
            "fields": (
                "tax_percentage",
                "discount_amount",
                "amount_paid",
            )
        }),
        ("Extra", {
            "fields": (
                "notes",
                "terms",
                "pdf_preview_link",
            )
        }),
    )

    def total_amount_display(self, obj):
        return f"{obj.currency} {obj.total_amount:,.2f}"
    total_amount_display.short_description = "Total"

    def amount_paid_display(self, obj):
        return f"{obj.currency} {obj.amount_paid:,.2f}"
    amount_paid_display.short_description = "Paid"

    def balance_display(self, obj):
        return f"{obj.currency} {obj.balance:,.2f}"
    balance_display.short_description = "Balance"

    def download_pdf_link(self, obj):
        if obj.pk:
            return format_html(
                '<a class="button" href="{}" target="_blank">Download PDF</a>',
                obj.get_pdf_url()
            )
        return "-"
    download_pdf_link.short_description = "PDF"

    def pdf_preview_link(self, obj):
        if obj.pk:
            return format_html(
                '<a class="button" href="{}" target="_blank">Open / Download Invoice PDF</a>',
                obj.get_pdf_url()
            )
        return "Save the invoice first to enable PDF download."
    pdf_preview_link.short_description = "Invoice PDF"



class ReceiptItemInline(admin.TabularInline):
    model = ReceiptItem
    extra = 1


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = (
        "receipt_number",
        "received_from",
        "invoice",
        "payment_date",
        "payment_method",
        "amount_received_display",
        "status",
        "download_pdf_link",
    )
    list_filter = ("status", "payment_date", "payment_method", "currency")
    search_fields = (
        "receipt_number",
        "received_from",
        "payer_email",
        "payer_phone",
        "reference_number",
        "invoice__invoice_number",
    )
    autocomplete_fields = ("invoice",)
    inlines = [ReceiptItemInline]
    readonly_fields = (
        "receipt_number",
        "invoice_total_display",
        "remaining_balance_display",
        "pdf_preview_link",
    )

    fieldsets = (
        ("Receipt Info", {
            "fields": (
                "receipt_number",
                "invoice",
                "status",
                "payment_date",
                "payment_method",
                "reference_number",
                "currency",
            )
        }),
        ("Received From", {
            "fields": (
                "received_from",
                "payer_email",
                "payer_phone",
                "payer_address",
            )
        }),
        ("Payment", {
            "fields": (
                "amount_received",
                "invoice_total_display",
                "remaining_balance_display",
            )
        }),
        ("Extra", {
            "fields": (
                "notes",
                "pdf_preview_link",
            )
        }),
    )

    def amount_received_display(self, obj):
        return f"{obj.currency} {obj.amount_received:,.2f}"
    amount_received_display.short_description = "Amount Received"

    def invoice_total_display(self, obj):
        return f"{obj.currency} {obj.invoice_total:,.2f}"
    invoice_total_display.short_description = "Invoice Total"

    def remaining_balance_display(self, obj):
        return f"{obj.currency} {obj.remaining_balance:,.2f}"
    remaining_balance_display.short_description = "Remaining Balance"

    def download_pdf_link(self, obj):
        if obj.pk:
            return format_html(
                '<a class="button" href="{}" target="_blank">Download PDF</a>',
                obj.get_pdf_url()
            )
        return "-"
    download_pdf_link.short_description = "PDF"

    def pdf_preview_link(self, obj):
        if obj.pk:
            return format_html(
                '<a class="button" href="{}" target="_blank">Open / Download Receipt PDF</a>',
                obj.get_pdf_url()
            )
        return "Save the receipt first to enable PDF download."
    pdf_preview_link.short_description = "Receipt PDF"