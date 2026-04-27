from django.db import models
from django.core.exceptions import ValidationError
from decimal import Decimal
from django.utils import timezone
from django.urls import reverse
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SingletonModel(models.Model):
    """
    Ensures only one record exists for configuration-style models.
    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class HomePageSetting(SingletonModel, TimeStampedModel):
    # General / SEO
    site_title = models.CharField(
        max_length=255,
        default="Muzadi Technologies - Innovate, Integrate, Inspire"
    )
    meta_keywords = models.TextField(
        blank=True,
        default="Muzadi Technologies, Uganda IT company, software development, web development, mobile apps, system development, Kampala tech company"
    )
    meta_description = models.TextField(
        blank=True,
        default="Muzadi Technologies is a leading IT company in Uganda offering software development, web design, mobile apps, and digital solutions to help businesses grow."
    )
    meta_author = models.CharField(max_length=255, blank=True, default="Muzadi Technologies")

    # Branding
    company_name = models.CharField(max_length=255, default="Muzadi Technologies")
    tagline = models.CharField(max_length=255, default="Innovate • Integrate • Inspire")
    logo = models.ImageField(upload_to="homepage/branding/", blank=True, null=True)
    favicon = models.ImageField(upload_to="homepage/branding/", blank=True, null=True)
    authorized_signature = models.ImageField(
        upload_to="homepage/branding/signatures/",
        blank=True,
        null=True
    )
    # Contact / Header / Footer
    phone_number = models.CharField(max_length=50, blank=True, default="+256784103296")
    whatsapp_number = models.CharField(max_length=50, blank=True, default="+256784103296")
    email = models.EmailField(blank=True, default="info@muzaditechnologies.com")
    website_url = models.URLField(blank=True, default="https://www.muzaditechnologies.com")
    address = models.CharField(max_length=255, blank=True, default="Kampala, Uganda")

    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    # Intro section
    intro_badge = models.CharField(max_length=120, default="Who We Are")
    intro_heading = models.CharField(
        max_length=255,
        default="Building smart digital solutions for modern businesses"
    )
    intro_text_1 = models.TextField(
        default="Muzadi Technologies is a Uganda-based technology company focused on building modern, scalable and secure digital solutions for organizations, startups, schools and growing enterprises."
    )
    intro_text_2 = models.TextField(
        default="We help businesses move from manual processes to intelligent systems through custom software development, mobile applications, websites, automation tools, branding and digital transformation services."
    )

    # Services section
    services_title = models.CharField(max_length=120, default="Our Services")
    services_subtitle = models.CharField(
        max_length=255,
        default="Premium technology services tailored for modern businesses"
    )

    # Products section
    products_title = models.CharField(max_length=120, default="Software Products")
    products_subtitle = models.CharField(
        max_length=255,
        default="Powerful solutions we build for businesses, schools and organizations"
    )

    # Features section
    features_title = models.CharField(max_length=120, default="Why Choose Us")
    features_subtitle = models.CharField(
        max_length=255,
        default="What makes Muzadi Technologies a strong technology partner"
    )
    features_image = models.ImageField(upload_to="homepage/features/", blank=True, null=True)

    # Pricing section
    pricing_title = models.CharField(max_length=120, default="Pricing")
    pricing_subtitle = models.CharField(
        max_length=255,
        default="Flexible packages for different business needs"
    )

    # Clients section
    clients_title = models.CharField(max_length=120, default="Our Clients")
    clients_subtitle = models.CharField(
        max_length=255,
        default="Trusted by growing businesses, schools and organizations"
    )
    clients_intro = models.TextField(
        blank=True,
        default="We partner with institutions and businesses across different sectors to build reliable digital solutions that improve efficiency, service delivery and growth."
    )
    clients_note = models.TextField(
        blank=True,
        default="From startups to established institutions, we deliver digital products that are practical, scalable and built for real operational impact."
    )

    # CTA section
    cta_badge = models.CharField(max_length=120, default="Let’s Build Something Great")
    cta_heading = models.CharField(
        max_length=255,
        default="Ready to transform your idea into a powerful digital solution?"
    )
    cta_text = models.TextField(
        default="Whether you need a website, mobile app, school system, business platform or custom software solution, Muzadi Technologies is ready to help."
    )
    cta_button_text = models.CharField(max_length=100, default="Start a Project")
    cta_button_url = models.CharField(max_length=255, default="#contact")
    cta_whatsapp_text = models.CharField(max_length=100, default="Chat on WhatsApp")

    # Footer
    footer_about = models.TextField(
        default="We build modern websites, business systems, mobile apps and digital solutions that help organizations work smarter and grow faster."
    )
    footer_copyright = models.CharField(
        max_length=255,
        default="© 2026 Muzadi Technologies. All Rights Reserved."
    )

    def __str__(self):
        return "Homepage Settings"


class HeroSlide(TimeStampedModel):
    title = models.CharField(max_length=255)
    subtitle_badge = models.CharField(max_length=120, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="homepage/hero/")
    primary_button_text = models.CharField(max_length=100, blank=True)
    primary_button_url = models.CharField(max_length=255, blank=True, default="#")
    secondary_button_text = models.CharField(max_length=100, blank=True)
    secondary_button_url = models.CharField(max_length=255, blank=True, default="#")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class IntroPoint(TimeStampedModel):
    text = models.CharField(max_length=255)
    icon = models.CharField(max_length=80, default="bi bi-check-circle-fill")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.text


class IntroStatCard(TimeStampedModel):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class Service(TimeStampedModel):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to="homepage/services/")
    icon = models.CharField(max_length=80, default="bi bi-window-stack")
    item_1 = models.CharField(max_length=150, blank=True)
    item_2 = models.CharField(max_length=150, blank=True)
    item_3 = models.CharField(max_length=150, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class SoftwareProduct(TimeStampedModel):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to="homepage/products/")
    icon = models.CharField(max_length=80, default="bi bi-box")
    tag = models.CharField(max_length=120, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class FeatureItem(TimeStampedModel):
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.CharField(max_length=80, default="bi bi-check2-square")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class PricingPlan(TimeStampedModel):
    title = models.CharField(max_length=120)
    price_prefix = models.CharField(max_length=50, blank=True, default="From")
    currency = models.CharField(max_length=20, blank=True, default="UGX")
    price_text = models.CharField(max_length=100, default="800K+")
    icon = models.CharField(max_length=80, default="bi bi-rocket-takeoff")
    button_text = models.CharField(max_length=100, default="Request Package")
    button_url = models.CharField(max_length=255, default="#contact")
    featured_label = models.CharField(max_length=120, blank=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class PricingPlanFeature(TimeStampedModel):
    plan = models.ForeignKey(
        PricingPlan,
        on_delete=models.CASCADE,
        related_name="features"
    )
    text = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.plan.title} - {self.text}"


class ClientLogo(TimeStampedModel):
    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to="homepage/clients/")
    website_url = models.URLField(blank=True)
    row = models.PositiveSmallIntegerField(default=1, help_text="Use 1 or 2 for slider row.")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["row", "order", "id"]

    def clean(self):
        if self.row not in [1, 2]:
            raise ValidationError({"row": "Row must be either 1 or 2."})

    def __str__(self):
        return self.name


class FooterLinkGroup(TimeStampedModel):
    title = models.CharField(max_length=120)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class FooterLink(TimeStampedModel):
    group = models.ForeignKey(
        FooterLinkGroup,
        on_delete=models.CASCADE,
        related_name="links"
    )
    label = models.CharField(max_length=120)
    url = models.CharField(max_length=255, default="#")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.group.title} - {self.label}"
   

class Receipt(TimeStampedModel):
    STATUS_CHOICES = [
        ("ISSUED", "Issued"),
        ("VOID", "Void"),
    ]

    PAYMENT_METHOD_CHOICES = [
        ("CASH", "Cash"),
        ("BANK", "Bank Transfer"),
        ("MOBILE", "Mobile Money"),
        ("CHEQUE", "Cheque"),
        ("OTHER", "Other"),
    ]

    receipt_number = models.CharField(max_length=30, unique=True, blank=True)

    invoice = models.ForeignKey(
        "Invoice",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="receipts"
    )

    received_from = models.CharField(max_length=255)
    payer_email = models.EmailField(blank=True, null=True)
    payer_phone = models.CharField(max_length=50, blank=True)
    payer_address = models.CharField(max_length=255, blank=True)

    payment_date = models.DateField(default=timezone.now)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default="BANK")
    reference_number = models.CharField(max_length=120, blank=True)

    currency = models.CharField(max_length=10, default="UGX")
    amount_received = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal("0.00"))

    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ISSUED")

    class Meta:
        ordering = ["-created_at", "-id"]

    def __str__(self):
        return f"{self.receipt_number} - {self.received_from}"

    def save(self, *args, **kwargs):
        if not self.receipt_number:
            self.receipt_number = self.generate_receipt_number()
        super().save(*args, **kwargs)

    @classmethod
    def generate_receipt_number(cls):
        today = timezone.now().strftime("%Y%m%d")
        last_receipt = cls.objects.filter(
            receipt_number__startswith=f"RCT-{today}"
        ).order_by("-id").first()

        if last_receipt and last_receipt.receipt_number:
            try:
                last_number = int(last_receipt.receipt_number.split("-")[-1])
            except (ValueError, IndexError):
                last_number = 0
        else:
            last_number = 0

        return f"RCT-{today}-{last_number + 1:04d}"

    @property
    def invoice_total(self):
        if self.invoice:
            return self.invoice.total_amount
        return Decimal("0.00")

    @property
    def remaining_balance(self):
        if self.invoice:
            bal = self.invoice.total_amount - self.invoice.amount_paid
            return bal if bal > 0 else Decimal("0.00")
        return Decimal("0.00")

    def get_pdf_url(self):
        return reverse("admin_receipt_pdf", args=[self.pk])

    def clean(self):
        if self.amount_received < 0:
            raise ValidationError({"amount_received": "Amount received cannot be negative."})

        if self.invoice:
            if self.currency != self.invoice.currency:
                raise ValidationError({"currency": "Receipt currency must match the invoice currency."})


class ReceiptItem(TimeStampedModel):
    receipt = models.ForeignKey(
        Receipt,
        on_delete=models.CASCADE,
        related_name="items"
    )
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal("0.00"))

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.receipt.receipt_number} - {self.description}"

    def clean(self):
        if self.amount < 0:
            raise ValidationError({"amount": "Amount cannot be negative."})

class Invoice(TimeStampedModel):
    STATUS_CHOICES = [
        ("DRAFT", "Draft"),
        ("SENT", "Sent"),
        ("PARTIAL", "Partial"),
        ("PAID", "Paid"),
        ("OVERDUE", "Overdue"),
        ("CANCELLED", "Cancelled"),
    ]

    invoice_number = models.CharField(max_length=30, unique=True, blank=True)

    client_name = models.CharField(max_length=255)
    client_email = models.EmailField(blank=True, null=True)
    client_phone = models.CharField(max_length=50, blank=True)
    client_address = models.CharField(max_length=255, blank=True)

    issued_date = models.DateField(default=timezone.now)
    due_date = models.DateField(blank=True, null=True)

    notes = models.TextField(blank=True)
    terms = models.TextField(blank=True, default="Payment is due within the stated due date.")
    currency = models.CharField(max_length=10, default="UGX")

    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal("0.00"))
    discount_amount = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal("0.00"))
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal("0.00"))

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="DRAFT")

    class Meta:
        ordering = ["-created_at", "-id"]

    def __str__(self):
        return f"{self.invoice_number} - {self.client_name}"

    def save(self, *args, **kwargs):
        if not self.invoice_number:
            self.invoice_number = self.generate_invoice_number()
        super().save(*args, **kwargs)

    @classmethod
    def generate_invoice_number(cls):
        today = timezone.now().strftime("%Y%m%d")
        last_invoice = cls.objects.filter(
            invoice_number__startswith=f"INV-{today}"
        ).order_by("-id").first()

        if last_invoice and last_invoice.invoice_number:
            try:
                last_number = int(last_invoice.invoice_number.split("-")[-1])
            except (ValueError, IndexError):
                last_number = 0
        else:
            last_number = 0

        return f"INV-{today}-{last_number + 1:04d}"

    @property
    def subtotal(self):
        return sum((item.line_total for item in self.items.all()), Decimal("0.00"))

    @property
    def tax_amount(self):
        return (self.subtotal * self.tax_percentage) / Decimal("100.00")

    @property
    def total_amount(self):
        total = self.subtotal + self.tax_amount - self.discount_amount
        return total if total > 0 else Decimal("0.00")

    @property
    def balance(self):
        bal = self.total_amount - self.amount_paid
        return bal if bal > 0 else Decimal("0.00")

    def get_pdf_url(self):
        return reverse("admin_invoice_pdf", args=[self.pk])

    def clean(self):
        if self.discount_amount < 0:
            raise ValidationError({"discount_amount": "Discount cannot be negative."})
        if self.amount_paid < 0:
            raise ValidationError({"amount_paid": "Amount paid cannot be negative."})


class InvoiceItem(TimeStampedModel):
    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE,
        related_name="items"
    )
    description = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("1.00"))
    unit_price = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal("0.00"))

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.invoice.invoice_number} - {self.description}"

    @property
    def line_total(self):
        return self.quantity * self.unit_price

    def clean(self):
        if self.quantity <= 0:
            raise ValidationError({"quantity": "Quantity must be greater than zero."})
        if self.unit_price < 0:
            raise ValidationError({"unit_price": "Unit price cannot be negative."})
        



def update_invoice_payment_status(invoice):
    total_received = invoice.receipts.filter(status="ISSUED").aggregate(
        total=models.Sum("amount_received")
    )["total"] or Decimal("0.00")

    invoice.amount_paid = total_received

    if invoice.amount_paid <= 0:
        if invoice.status == "PAID":
            invoice.status = "SENT"
    elif invoice.amount_paid >= invoice.total_amount:
        invoice.status = "PAID"
    else:
        invoice.status = "PARTIAL"

    invoice.save(update_fields=["amount_paid", "status"])


@receiver(post_save, sender=Receipt)
def receipt_post_save(sender, instance, **kwargs):
    if instance.invoice:
        update_invoice_payment_status(instance.invoice)


@receiver(post_delete, sender=Receipt)
def receipt_post_delete(sender, instance, **kwargs):
    if instance.invoice:
        update_invoice_payment_status(instance.invoice)