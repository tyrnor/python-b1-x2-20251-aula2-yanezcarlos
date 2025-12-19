from enum import Enum
from datetime import datetime

ISD_FACTOR = 0.25

class TaxType(Enum):
    IVA = 'IVA'
    ISD = 'ISD'

class Tax:
    def __init__(self, tax_id: str, tax_type: TaxType, percentage: float) -> None:
        self.tax_id = tax_id
        self.tax_type = tax_type
        self.percentage = percentage

class Product:
    def __init__(
        self,
        product_id: str,
        name: str,
        expiration_date: datetime,
        bar_code: str,
        quantity: int,
        price: float,
        taxes: list[Tax],
    ) -> None:
        self.product_id = product_id
        self.name = name
        self.expiration_date = expiration_date
        self.bar_code = bar_code
        self.quantity = quantity
        self.price = price
        self.taxes = taxes
    
    def calculate_tax(self, tax: Tax) -> float:
        tax_value = self.quantity * self.price * tax.percentage

        if tax.tax_type == TaxType.ISD:
            tax_value *= ISD_FACTOR

        return tax_value

    def calculate_total_taxes(self):
        pass
    
    def calculate_total(self):
        pass