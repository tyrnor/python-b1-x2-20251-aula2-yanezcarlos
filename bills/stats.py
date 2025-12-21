from item import Bill
from enum import Enum


class OrderType(Enum):
    ASC = "Ascendent"
    DESC = "Descendent"


class Statistics:
    def __init__(self, bills: list[Bill]) -> None:
        self.bills = bills

    def find_top_sell_product(self) -> tuple:
        products_count = {}
        for bill in self.bills:
            for product in bill.products:
                products_count[product] = products_count.get(product, 0) + 1

        max_key = None
        max_value = 0

        for key, value in products_count.items():
            if value > max_value:
                max_value = value
                max_key = key

        return (max_key, max_value)

    def find_top_two_sellers(self) -> list:
        sellers_totals = {}

        for bill in self.bills:
            sellers_totals[bill.seller] = (
                sellers_totals.get(bill.seller, 0) + bill.calculate_total()
            )

        sorted_sellers = sorted(
            sellers_totals.items(), key=lambda item: item[1], reverse=True
        )
        it = iter(sorted_sellers)
        top1 = next(it)[0]
        top2 = next(it)[0]

        return [top1, top2]

    def find_buyer_lowest_total_purchases(self) -> tuple:

        buyers_totals = {}

        for bill in self.bills:
            buyers_totals[bill.buyer] = (
                buyers_totals.get(bill.buyer, 0) + bill.calculate_total()
            )

        sorted_buyers = sorted(
            buyers_totals.items(), key=lambda item: item[1], reverse=False
        )
        lowest_buyer = next(iter(sorted_buyers))

        return (lowest_buyer[0], lowest_buyer[1])

    def order_products_by_tax(self, order_type: OrderType) -> list:

        products_list = []

        for bill in self.bills:
            for product in bill.products:
                total_taxes = product.calculate_total_taxes()
                products_list.append((product, total_taxes))

        if order_type == OrderType.DESC:
            products_list = sorted(
                products_list, key=lambda item: item[1], reverse=True
            )
        elif order_type == OrderType.ASC:
            products_list = sorted(
                products_list, key=lambda item: item[1], reverse=False
            )
        return products_list
