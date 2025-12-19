from enum import Enum
from datetime import datetime

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