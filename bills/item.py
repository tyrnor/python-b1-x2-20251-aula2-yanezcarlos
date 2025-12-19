from enum import Enum
from datetime import datetime
from entity import Buyer, Seller

ISD_FACTOR = 0.25


class TaxType(Enum):
    IVA = "IVA"
    ISD = "ISD"


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

    def calculate_total_taxes(self) -> float:
        total = 0.0
        for tax in self.taxes:
            total += self.calculate_tax(tax)

        return total

    def calculate_total(self) -> float:
        return (self.price * self.quantity) + self.calculate_total_taxes()


class Bill:
    def __init__(
        self,
        bill_id: str,
        sale_date: datetime,
        seller: Seller,
        buyer: Buyer,
        products: list[Product],
    ) -> None:
        self.bill_id = bill_id
        self.sale_date = sale_date
        self.seller = seller
        self.buyer = buyer
        self.products = products

    def calculate_total(self) -> float:
        return sum(product.calculate_total() for product in self.products)
