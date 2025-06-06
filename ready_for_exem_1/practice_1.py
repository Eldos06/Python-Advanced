from decimal import Decimal
print(f"{0.1 + 0.2 == 0.3}: --> because 0.1 + 0.2 = {0.1 + 0.2}")        # False?


print(f'{Decimal("0.1") + Decimal("0.2") == Decimal("0.3")}: --> because Decimal("0.1") + Decimal("0.2") = {Decimal("0.3")}' )  # True?


