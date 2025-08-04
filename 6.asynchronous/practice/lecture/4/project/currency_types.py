from dataclasses import dataclass
from datetime import date
from decimal import Decimal

ResponseType = dict[str, str | dict[str, Decimal]]


@dataclass(frozen=True)
class CurrencyValue:
  currency: str
  value: Decimal

@dataclass(frozen=True)
class CurrencyInfo:
  date: date
  currency: str
  values: list[CurrencyValue]

  @classmethod
  def from_currency_info_response(
    cls,
    info: ResponseType,
    source_currency: str,
    target_currency: set[str],

  ) -> "CurrencyInfo":
    return cls(
      date=date.fromisoformat(info["date"]),
      currency = source_currency,
      value = [

        #prepare object
        CurrencyValue(currency=name, value=value)
        #read all items
        for name, value in info[source_currency].items()
        #filter out those which are not in our target
        if name in target_currency
      ],
    )















