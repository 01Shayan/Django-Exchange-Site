from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length=20, unique=True)  # Currency code
    name = models.CharField(max_length=50)             # Currency name
    buy_rate = models.FloatField()                     # Buy rate
    sell_rate = models.FloatField()                    # Sell rate
    flag_url = models.URLField(null=True, blank=True)  # URL for the country flag
    order = models.PositiveIntegerField(default=0)     # Custom order field
    is_active = models.BooleanField(default=True)      # Active status (hidden or visible)
    updated_at = models.DateTimeField(auto_now=True)   # Updated timestamp

    def hidden_status(self):
        return "Hidden" if not self.is_active else "Visible"
    hidden_status.short_description = "Visibility"


    class Meta:
        db_table = "currency"
        ordering = ['order']  # Default ordering by the 'order' field

    def __str__(self):
        return f"{self.code} - {self.name}"
    


class Configuration(models.Model):
    prices_fee = models.FloatField(default=0.2, help_text="Prices fee percentage (e.g., 0.2 for 0.2%)")
    show_prices_fee = models.BooleanField(default=True, help_text="Show or hide prices fee on the homepage")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "configuration"

    def __str__(self):
        return f"Configuration - Prices Fee: {self.prices_fee}% (Visible: {self.show_prices_fee})"
