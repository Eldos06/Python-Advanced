import json
from decimal import Decimal
from decimal import date

def json_encode_default(obj):
  if isinstance(obj, date):
    return obj.isoformat()
  if isinstance(obj, Decimal):
    return str(obj)
  raise TypeError(f"Type {type(obj)} not serializable")

json_encoder = json.JSONEncoder(
  ensure_ascii=False,
  indent = 2,
  default = json_encode_default,
)

json_decoder = json.JSONDecoder(
  parse_int = Decimal,
  parse_float = Decimal,
)