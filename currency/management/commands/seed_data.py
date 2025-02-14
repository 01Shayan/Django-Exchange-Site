
from django.core.management.base import BaseCommand
from currency.models import Currency, Configuration
from about.models import About

class Command(BaseCommand):
    help = "Seed the database with initial currency data, configuration settings, and About page information"

    def handle(self, *args, **kwargs):
        
        # Currency Data
        initial_data = [
            {'code': 'USD', 'name': 'United States Dollar', 'buy_rate': 35.6, 'sell_rate': 35.85, 'flag_url': 'https://flagcdn.com/w160/us.png', 'order': 1, 'is_active': True},
            {'code': 'EUR', 'name': 'European Union', 'buy_rate': 37.25, 'sell_rate': 37.65, 'flag_url': 'https://flagcdn.com/w160/eu.png', 'order': 2, 'is_active': True},
            {'code': 'GBP', 'name': 'British Pound', 'buy_rate': 44.0, 'sell_rate': 44.7, 'flag_url': 'https://flagcdn.com/w160/gb.png', 'order': 3, 'is_active': True},
            {'code': 'CAD', 'name': 'Canadian Dollar', 'buy_rate': 24.3, 'sell_rate': 24.9, 'flag_url': 'https://flagcdn.com/w160/ca.png', 'order': 4, 'is_active': True},
            {'code': 'AUD', 'name': 'Australian Dollar', 'buy_rate': 21.85, 'sell_rate': 22.5, 'flag_url': 'https://flagcdn.com/w160/au.png', 'order': 5, 'is_active': True},
            {'code': 'IRT', 'name': 'Iranian Toman', 'buy_rate': 1.185, 'sell_rate': 1.191, 'flag_url': 'https://flagcdn.com/w160/ir.png', 'order': 6, 'is_active': True},
            {'code': 'TRY', 'name': 'Turkish Lira', 'buy_rate': 1.185, 'sell_rate': 1.191, 'flag_url': 'https://flagcdn.com/w160/tr.png', 'order': 7, 'is_active': True},
            {'code': 'SAR', 'name': 'Saudi Riyal', 'buy_rate': 9.45, 'sell_rate': 9.6, 'flag_url': 'https://flagcdn.com/w160/sa.png', 'order': 8, 'is_active': True},
            {'code': 'JPY', 'name': 'Japanese Yen', 'buy_rate': 0.22, 'sell_rate': 0.229, 'flag_url': 'https://flagcdn.com/w160/jp.png', 'order': 9, 'is_active': True},
            {'code': 'CHF', 'name': 'Swiss Franc', 'buy_rate': 38.75, 'sell_rate': 39.4, 'flag_url': 'https://flagcdn.com/w160/ch.png', 'order': 10, 'is_active': True},
            {'code': 'DKK', 'name': 'Danish Krone', 'buy_rate': 0.0, 'sell_rate': 0.0, 'flag_url': 'https://flagcdn.com/w160/dk.png', 'order': 11, 'is_active': True},
            {'code': 'SEK', 'name': 'Swedish Krona', 'buy_rate': 0.0, 'sell_rate': 0.0, 'flag_url': 'https://flagcdn.com/w160/se.png', 'order': 12, 'is_active': True},
            {'code': 'NOK', 'name': 'Norwegian krone', 'buy_rate': 0.0, 'sell_rate': 0.0, 'flag_url': 'https://flagcdn.com/w160/no.png', 'order': 13, 'is_active': True},
        ]

        for currency in initial_data:
            Currency.objects.update_or_create(code=currency['code'], defaults=currency)

        self.stdout.write(self.style.SUCCESS("Successfully seeded the database with currency data."))

        # Global Configuration (Prices Fee & Visibility)
        config_data = {
            'prices_fee': 0.2,  # Default fee
            'show_prices_fee': True  # Set to False to hide the prices fee
        }

        config, created = Configuration.objects.update_or_create(defaults=config_data)
        if created:
            self.stdout.write(self.style.SUCCESS("Created new Configuration entry."))
        else:
            self.stdout.write(self.style.SUCCESS("Updated existing Configuration entry."))

        # About Page Information
        about_data = {
            'address': "Cumhuriyet, Sakarya Cd., 06430 Çankaya/Ankara, Türkei",
            'email': "FarnazEx@support.com",
            'phone': "+1234567890",
            'whatsapp': "+1234567890",
            'location': "39.92169639191772, 32.85462243844915",
            'show_address': True,
            'show_email': True,
            'show_phone': True,
            'show_whatsapp': True,
            'show_location': True
        }

        about, created = About.objects.update_or_create(defaults=about_data)
        if created:
            self.stdout.write(self.style.SUCCESS("Created new About page entry."))
        else:
            self.stdout.write(self.style.SUCCESS("Updated existing About page entry."))
