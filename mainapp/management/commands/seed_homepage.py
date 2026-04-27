from django.core.management.base import BaseCommand
from mainapp.models import (
    HomePageSetting,
    HeroSlide,
    IntroPoint,
    IntroStatCard,
    Service,
    SoftwareProduct,
    FeatureItem,
    PricingPlan,
    PricingPlanFeature,
    FooterLinkGroup,
    FooterLink,
)


class Command(BaseCommand):
    help = "Seed homepage content"

    def handle(self, *args, **options):
        homepage, _ = HomePageSetting.objects.get_or_create(pk=1)

        homepage.site_title = "Muzadi Technologies - Innovate, Integrate, Inspire"
        homepage.meta_keywords = (
            "Muzadi Technologies, Uganda IT company, software development, "
            "web development, mobile apps, system development, Kampala tech company"
        )
        homepage.meta_description = (
            "Muzadi Technologies is a leading IT company in Uganda offering software "
            "development, web design, mobile apps, and digital solutions to help businesses grow."
        )
        homepage.meta_author = "Muzadi Technologies"
        homepage.company_name = "Muzadi Technologies"
        homepage.tagline = "Innovate • Integrate • Inspire"
        homepage.phone_number = "+256784103296"
        homepage.whatsapp_number = "+256784103296"
        homepage.email = "info@muzaditechnologies.com"
        homepage.website_url = "https://www.muzaditechnologies.com"
        homepage.address = "Kampala, Uganda"

        homepage.intro_badge = "Who We Are"
        homepage.intro_heading = "Building smart digital solutions for modern businesses"
        homepage.intro_text_1 = (
            "Muzadi Technologies is a Uganda-based technology company focused on building "
            "modern, scalable and secure digital solutions for organizations, startups, "
            "schools and growing enterprises."
        )
        homepage.intro_text_2 = (
            "We help businesses move from manual processes to intelligent systems through "
            "custom software development, mobile applications, websites, automation tools, "
            "branding and digital transformation services."
        )

        homepage.services_title = "Our Services"
        homepage.services_subtitle = "Premium technology services tailored for modern businesses"

        homepage.products_title = "Software Products"
        homepage.products_subtitle = "Powerful solutions we build for businesses, schools and organizations"

        homepage.features_title = "Why Choose Us"
        homepage.features_subtitle = "What makes Muzadi Technologies a strong technology partner"

        homepage.pricing_title = "Pricing"
        homepage.pricing_subtitle = "Flexible packages for different business needs"

        homepage.clients_title = "Our Clients"
        homepage.clients_subtitle = "Trusted by growing businesses, schools and organizations"
        homepage.clients_intro = (
            "We partner with institutions and businesses across different sectors to build "
            "reliable digital solutions that improve efficiency, service delivery and growth."
        )
        homepage.clients_note = (
            "From startups to established institutions, we deliver digital products that are "
            "practical, scalable and built for real operational impact."
        )

        homepage.cta_badge = "Let’s Build Something Great"
        homepage.cta_heading = "Ready to transform your idea into a powerful digital solution?"
        homepage.cta_text = (
            "Whether you need a website, mobile app, school system, business platform or "
            "custom software solution, Muzadi Technologies is ready to help."
        )
        homepage.cta_button_text = "Start a Project"
        homepage.cta_button_url = "#contact"
        homepage.cta_whatsapp_text = "Chat on WhatsApp"

        homepage.footer_about = (
            "We build modern websites, business systems, mobile apps and digital solutions "
            "that help organizations work smarter and grow faster."
        )
        homepage.footer_copyright = "© 2026 Muzadi Technologies. All Rights Reserved."
        homepage.save()

        hero_slides = [
            {
                "title": "We Create Systems That Simplify How Businesses Work",
                "subtitle_badge": "Business Systems • Automation",
                "description": (
                    "From school systems to HR, inventory, finance, and internal operations, "
                    "we design software that saves time and keeps your business organized."
                ),
                "primary_button_text": "Explore Services",
                "primary_button_url": "#services",
                "secondary_button_text": "Talk to Us",
                "secondary_button_url": "#contact",
                "order": 1,
                "is_active": True,
            },
            {
                "title": "Helping Brands Stand Out with Modern Technology",
                "subtitle_badge": "Innovation • Branding • Growth",
                "description": (
                    "We combine design, development, and strategy to help startups and "
                    "established businesses build a strong digital presence that wins trust."
                ),
                "primary_button_text": "See Portfolio",
                "primary_button_url": "#products",
                "secondary_button_text": "Request a Quote",
                "secondary_button_url": "#contact",
                "order": 2,
                "is_active": True,
            },
        ]

        for item in hero_slides:
            HeroSlide.objects.get_or_create(
                title=item["title"],
                defaults=item
            )

        intro_points = [
            ("Custom software for real business workflows", "bi bi-check-circle-fill", 1),
            ("Clean modern UI/UX and responsive design", "bi bi-check-circle-fill", 2),
            ("Reliable support, deployment and maintenance", "bi bi-check-circle-fill", 3),
        ]
        for text, icon, order in intro_points:
            IntroPoint.objects.get_or_create(
                text=text,
                defaults={"icon": icon, "order": order, "is_active": True}
            )

        intro_stats = [
            ("Web", "Business websites, portals and web apps", 1),
            ("Mobile", "Android and cross-platform app development", 2),
            ("Systems", "Custom systems for schools, HR, inventory and finance", 3),
            ("Support", "Training, hosting, maintenance and upgrades", 4),
        ]
        for title, description, order in intro_stats:
            IntroStatCard.objects.get_or_create(
                title=title,
                defaults={"description": description, "order": order, "is_active": True}
            )

        services = [
            {
                "title": "Website Design & Development",
                "description": "We build responsive, modern and high-converting websites, company profiles, portals and custom web platforms for growing brands.",
                "icon": "bi bi-window-stack",
                "item_1": "Corporate websites",
                "item_2": "Business portals",
                "item_3": "E-commerce platforms",
                "order": 1,
                "is_active": True,
            },
            {
                "title": "Mobile App Development",
                "description": "We create mobile apps that improve customer service, internal workflows, reporting and access to digital services on the go.",
                "icon": "bi bi-phone",
                "item_1": "Android apps",
                "item_2": "Business mobile apps",
                "item_3": "Customer self-service apps",
                "order": 2,
                "is_active": True,
            },
            {
                "title": "Business Systems Development",
                "description": "We develop smart digital systems that reduce manual work, improve accuracy and give organizations better control of operations.",
                "icon": "bi bi-diagram-3",
                "item_1": "School management systems",
                "item_2": "HR & payroll systems",
                "item_3": "Inventory and finance systems",
                "order": 3,
                "is_active": True,
            },
            {
                "title": "Branding & UI/UX Design",
                "description": "We design beautiful visual identities and digital interfaces that make your business look premium, modern and trustworthy.",
                "icon": "bi bi-palette",
                "item_1": "Logo & identity design",
                "item_2": "UI/UX design systems",
                "item_3": "Marketing creatives",
                "order": 4,
                "is_active": True,
            },
            {
                "title": "Hosting, Deployment & Maintenance",
                "description": "We help you launch and maintain your digital products with hosting, system updates, backups, support and performance optimization.",
                "icon": "bi bi-cloud-check",
                "item_1": "Deployment setup",
                "item_2": "Maintenance & upgrades",
                "item_3": "Monitoring & backups",
                "order": 5,
                "is_active": True,
            },
            {
                "title": "IT Consulting & Digital Transformation",
                "description": "We guide businesses that want to digitize operations, improve systems and adopt smarter workflows for long-term growth.",
                "icon": "bi bi-shield-check",
                "item_1": "Process digitization",
                "item_2": "Technology advisory",
                "item_3": "System improvement planning",
                "order": 6,
                "is_active": True,
            },
        ]
        for item in services:
            Service.objects.get_or_create(title=item["title"], defaults=item)

        products = [
            {
                "title": "School Management System",
                "description": "Manage student records, attendance, exams, report cards, fees and school administration in one centralized platform.",
                "icon": "bi bi-mortarboard",
                "tag": "Education Technology",
                "order": 1,
                "is_active": True,
            },
            {
                "title": "HR & Payroll System",
                "description": "Handle staff data, payroll, attendance, leave tracking and reporting with a professional HR management platform.",
                "icon": "bi bi-people",
                "tag": "Business Operations",
                "order": 2,
                "is_active": True,
            },
            {
                "title": "Inventory Management System",
                "description": "Monitor stock movement, item issuance, supplies and asset records using a smart inventory and accountability solution.",
                "icon": "bi bi-box-seam",
                "tag": "Inventory & Assets",
                "order": 3,
                "is_active": True,
            },
            {
                "title": "Finance & Billing Solutions",
                "description": "Simplify invoicing, collections, tracking and operational financial records through custom billing and reporting tools.",
                "icon": "bi bi-cash-coin",
                "tag": "Finance Automation",
                "order": 4,
                "is_active": True,
            },
            {
                "title": "Recruitment & Agency Systems",
                "description": "Manage candidates, interviews, documentation, payments and workflows in a structured digital recruitment platform.",
                "icon": "bi bi-briefcase",
                "tag": "Workflow Management",
                "order": 5,
                "is_active": True,
            },
            {
                "title": "Custom Enterprise Platforms",
                "description": "We build bespoke platforms around your exact business workflow, reports, users and long-term operational goals.",
                "icon": "bi bi-sliders",
                "tag": "Custom Development",
                "order": 6,
                "is_active": True,
            },
        ]
        for item in products:
            SoftwareProduct.objects.get_or_create(title=item["title"], defaults=item)

        features = [
            ("Tailor-Made Solutions", "We build around your real workflow, not just generic templates.", "bi bi-check2-square", 1),
            ("Fast & Modern", "Clean interfaces, responsive layouts and high-performing platforms.", "bi bi-lightning-charge", 2),
            ("Secure Systems", "We prioritize stability, secure access and reliable architecture.", "bi bi-shield-lock", 3),
            ("Scalable Growth", "Solutions built to support growth as your organization expands.", "bi bi-graph-up-arrow", 4),
            ("Ongoing Support", "We stay with you after launch through updates and technical support.", "bi bi-headset", 5),
            ("Business Understanding", "We combine technical expertise with practical business thinking.", "bi bi-people-fill", 6),
        ]
        for title, description, icon, order in features:
            FeatureItem.objects.get_or_create(
                title=title,
                defaults={"description": description, "icon": icon, "order": order, "is_active": True}
            )

        plans = [
            {
                "title": "Starter",
                "price_prefix": "From",
                "currency": "UGX",
                "price_text": "800K+",
                "icon": "bi bi-rocket-takeoff",
                "button_text": "Request Package",
                "button_url": "#contact",
                "featured_label": "",
                "is_featured": False,
                "order": 1,
                "is_active": True,
                "features": [
                    "Simple business website",
                    "Responsive design",
                    "Basic contact forms",
                    "Essential pages setup",
                    "Best for startups & small businesses",
                ],
            },
            {
                "title": "Business",
                "price_prefix": "From",
                "currency": "UGX",
                "price_text": "2M+",
                "icon": "bi bi-building",
                "button_text": "Get Quote",
                "button_url": "#contact",
                "featured_label": "Most Popular",
                "is_featured": True,
                "order": 2,
                "is_active": True,
                "features": [
                    "Advanced website or web app",
                    "Admin dashboard",
                    "Custom business features",
                    "Database integration",
                    "Ideal for established organizations",
                ],
            },
            {
                "title": "Enterprise",
                "price_prefix": "",
                "currency": "",
                "price_text": "Custom",
                "icon": "bi bi-diagram-3-fill",
                "button_text": "Talk to Us",
                "button_url": "#contact",
                "featured_label": "",
                "is_featured": False,
                "order": 3,
                "is_active": True,
                "features": [
                    "Large-scale systems",
                    "Multi-user platforms",
                    "Custom workflows & reports",
                    "Deployment & support",
                    "Best for schools, agencies and enterprises",
                ],
            },
        ]

        for item in plans:
            feature_list = item.pop("features")
            plan, created = PricingPlan.objects.get_or_create(
                title=item["title"],
                defaults=item
            )
            if created:
                for idx, text in enumerate(feature_list, start=1):
                    PricingPlanFeature.objects.create(plan=plan, text=text, order=idx)

        quick_links, _ = FooterLinkGroup.objects.get_or_create(
            title="Quick Links",
            defaults={"order": 1, "is_active": True}
        )
        solution_links, _ = FooterLinkGroup.objects.get_or_create(
            title="Our Solutions",
            defaults={"order": 2, "is_active": True}
        )

        quick_items = [
            ("Home", "#hero", 1),
            ("Our Services", "#services", 2),
            ("Software Products", "#products", 3),
            ("Pricing", "#pricing", 4),
            ("Our Clients", "#clients", 5),
        ]
        for label, url, order in quick_items:
            FooterLink.objects.get_or_create(
                group=quick_links,
                label=label,
                defaults={"url": url, "order": order, "is_active": True}
            )

        solution_items = [
            ("School Management Systems", "#products", 1),
            ("HR & Payroll Systems", "#products", 2),
            ("Inventory Systems", "#products", 3),
            ("Website Development", "#services", 4),
            ("Custom Software Development", "#services", 5),
        ]
        for label, url, order in solution_items:
            FooterLink.objects.get_or_create(
                group=solution_links,
                label=label,
                defaults={"url": url, "order": order, "is_active": True}
            )

        self.stdout.write(self.style.SUCCESS("Homepage seed completed successfully."))