from django.contrib import admin
from django.utils.html import format_html

from .models import (
    HomePageSetting,
    HeroSlide,
    IntroPoint,
    IntroStatCard,
    Service,
    SoftwareProduct,
    FeatureItem,
    PricingPlan,
    PricingPlanFeature,
    ClientLogo,
    FooterLinkGroup,
    FooterLink,

    # SHOP MODELS
    ShopInvoice,
    ShopInvoiceItem,
    ShopReceipt,
)


# =========================================================
# INLINE MODELS
# =========================================================

class PricingPlanFeatureInline(admin.TabularInline):
    model = PricingPlanFeature
    extra = 1


class FooterLinkInline(admin.TabularInline):
    model = FooterLink
    extra = 1


class ShopInvoiceItemInline(admin.TabularInline):
    model = ShopInvoiceItem
    extra = 1

    fields = (
        "category",
        "product_name",
        "description",
        "serial_number",
        "quantity",
        "unit_price",
        "warranty",
        "line_total_display",
    )

    readonly_fields = ("line_total_display",)

    def line_total_display(self, obj):
        if obj.pk:
            return f"{obj.line_total:,.0f}"
        return "0"
    line_total_display.short_description = "Amount"


# =========================================================
# GENERAL WEBSITE ADMIN
# =========================================================

@admin.register(HomePageSetting)
class HomePageSettingAdmin(admin.ModelAdmin):

    fieldsets = (

        ("Company Branding", {
            "fields": (
                "company_name",
                "tagline",
                "logo",
                "favicon",
            )
        }),

        ("Contact Information", {
            "fields": (
                "phone_number",
                "whatsapp_number",
                "email",
                "website_url",
                "address",
            )
        }),

        ("Social Media", {
            "fields": (
                "facebook_url",
                "instagram_url",
                "linkedin_url",
            )
        }),

        ("SEO", {
            "fields": (
                "site_title",
                "meta_keywords",
                "meta_description",
                "meta_author",
            )
        }),

        ("Homepage Intro", {
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

        ("Call To Action", {
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
    list_display = (
        "title",
        "tag",
        "order",
        "is_active"
    )

    list_editable = (
        "order",
        "is_active"
    )


@admin.register(FeatureItem)
class FeatureItemAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "order",
        "is_active"
    )

    list_editable = (
        "order",
        "is_active"
    )


@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "price_text",
        "is_featured",
        "order",
        "is_active"
    )

    list_editable = (
        "is_featured",
        "order",
        "is_active"
    )

    inlines = [PricingPlanFeatureInline]


@admin.register(ClientLogo)
class ClientLogoAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "row",
        "order",
        "is_active"
    )

    list_editable = (
        "row",
        "order",
        "is_active"
    )


@admin.register(FooterLinkGroup)
class FooterLinkGroupAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "order",
        "is_active"
    )

    list_editable = (
        "order",
        "is_active"
    )

    inlines = [FooterLinkInline]


# =========================================================
# SHOP INVOICE ADMIN
# =========================================================

@admin.register(ShopInvoice)
class ShopInvoiceAdmin(admin.ModelAdmin):

    list_display = (
        "invoice_number",
        "customer_name",
        "invoice_date",
        "total_display",
        "paid_display",
        "balance_display",
        "status_badge",
        "download_pdf",
    )

    list_filter = (
        "status",
        "invoice_date",
        "currency",
    )

    search_fields = (
        "invoice_number",
        "customer_name",
        "customer_phone",
        "customer_email",
    )

    readonly_fields = (
        "invoice_number",
        "subtotal_display",
        "tax_display",
        "total_display_readonly",
        "balance_display_readonly",
        "pdf_preview",
    )

    autocomplete_fields = []

    inlines = [ShopInvoiceItemInline]

    fieldsets = (

        ("Invoice Information", {
            "fields": (
                "invoice_number",
                "invoice_date",
                "status",
                "currency",
            )
        }),

        ("Customer Information", {
            "fields": (
                "customer_name",
                "customer_phone",
                "customer_email",
                "customer_address",
            )
        }),

        ("Payment Summary", {
            "fields": (
                "tax_percentage",
                "discount_amount",
                "amount_paid",
                "subtotal_display",
                "tax_display",
                "total_display_readonly",
                "balance_display_readonly",
            )
        }),

        ("Extra Information", {
            "fields": (
                "notes",
                "pdf_preview",
            )
        }),

    )

    # =======================================
    # DISPLAY METHODS
    # =======================================

    def total_display(self, obj):
        return f"{obj.currency} {obj.total_amount:,.0f}"
    total_display.short_description = "Total"

    def paid_display(self, obj):
        return f"{obj.currency} {obj.amount_paid:,.0f}"
    paid_display.short_description = "Paid"

    def balance_display(self, obj):
        return f"{obj.currency} {obj.balance:,.0f}"
    balance_display.short_description = "Balance"

    def subtotal_display(self, obj):
        return f"{obj.currency} {obj.subtotal:,.0f}"
    subtotal_display.short_description = "Subtotal"

    def tax_display(self, obj):
        return f"{obj.currency} {obj.tax_amount:,.0f}"
    tax_display.short_description = "Tax Amount"

    def total_display_readonly(self, obj):
        return f"{obj.currency} {obj.total_amount:,.0f}"
    total_display_readonly.short_description = "Grand Total"

    def balance_display_readonly(self, obj):
        return f"{obj.currency} {obj.balance:,.0f}"
    balance_display_readonly.short_description = "Remaining Balance"

    # =======================================
    # STATUS BADGES
    # =======================================

    def status_badge(self, obj):

        colors = {
            "PENDING": "#f59e0b",
            "PARTIAL": "#2563eb",
            "PAID": "#16a34a",
            "CANCELLED": "#dc2626",
        }

        return format_html(
            '''
            <span style="
                background:{};
                color:white;
                padding:4px 10px;
                border-radius:20px;
                font-size:11px;
                font-weight:bold;
            ">
                {}
            </span>
            ''',
            colors.get(obj.status, "#64748b"),
            obj.status
        )

    status_badge.short_description = "Status"

    # =======================================
    # PDF LINKS
    # =======================================

    def download_pdf(self, obj):

        if obj.pk:
            return format_html(
                '''
                <a class="button"
                   href="{}"
                   target="_blank">

                   Download PDF

                </a>
                ''',
                obj.get_pdf_url()
            )

        return "-"

    download_pdf.short_description = "PDF"

    def pdf_preview(self, obj):

        if obj.pk:
            return format_html(
                '''
                <a class="button"
                   href="{}"
                   target="_blank">

                   Open / Download Invoice PDF

                </a>
                ''',
                obj.get_pdf_url()
            )

        return "Save invoice first."

    pdf_preview.short_description = "Invoice PDF"


# =========================================================
# SHOP RECEIPT ADMIN
# =========================================================

@admin.register(ShopReceipt)
class ShopReceiptAdmin(admin.ModelAdmin):

    list_display = (
        "receipt_number",
        "customer_name",
        "invoice",
        "payment_date",
        "payment_method",
        "amount_display",
        "download_pdf",
    )

    list_filter = (
        "payment_method",
        "payment_date",
    )

    search_fields = (
        "receipt_number",
        "customer_name",
        "reference_number",
        "invoice__invoice_number",
    )

    autocomplete_fields = ("invoice",)

    readonly_fields = (
        "receipt_number",
        "pdf_preview",
    )

    fieldsets = (

        ("Receipt Information", {
            "fields": (
                "receipt_number",
                "invoice",
                "payment_date",
                "payment_method",
                "reference_number",
            )
        }),

        ("Customer Information", {
            "fields": (
                "customer_name",
            )
        }),

        ("Payment", {
            "fields": (
                "amount_received",
                "notes",
            )
        }),

        ("PDF", {
            "fields": (
                "pdf_preview",
            )
        }),

    )

    # =======================================
    # DISPLAY METHODS
    # =======================================

    def amount_display(self, obj):
        return f"UGX {obj.amount_received:,.0f}"
    amount_display.short_description = "Amount"

    # =======================================
    # PDF METHODS
    # =======================================

    def download_pdf(self, obj):

        if obj.pk:
            return format_html(
                '''
                <a class="button"
                   href="{}"
                   target="_blank">

                   Download PDF

                </a>
                ''',
                obj.get_pdf_url()
            )

        return "-"

    download_pdf.short_description = "PDF"

    def pdf_preview(self, obj):

        if obj.pk:
            return format_html(
                '''
                <a class="button"
                   href="{}"
                   target="_blank">

                   Open / Download Receipt PDF

                </a>
                ''',
                obj.get_pdf_url()
            )

        return "Save receipt first."

    pdf_preview.short_description = "Receipt PDF"