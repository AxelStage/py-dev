#!python3

"""
    Custom JSONDecoder class to deserialize hat can deserialize a JSON structure
    containing Stock and Trade objects.
"""
import json
from datetime import date, datetime
from decimal import Decimal
from json_encoder import encoded, Trade, Stock

def decode_stock(d):
    # assumes "class": "Stock" is in the dictionary
    # and contains all the required serialized fields needed to re-create the object
    # if working in Python 3.7, we could use date.fromisoformat(d['date']) instead
    stock = Stock(d['symbol'],
              datetime.strptime(d['date'], '%Y-%m-%d').date(),
              Decimal(d['open']),
              Decimal(d['high']),
              Decimal(d['low']),
              Decimal(d['close']),
              int(d['volume']))
    return stock

def decode_trade(d):
    # assumes "class": "Trade" is in the dictionary
    # and contains all the required serialized fields needed to re-create the object
    trade = Trade(d['symbol'],
              datetime.strptime(d['timestamp'], '%Y-%m-%dT%H:%M:%S'),
              d['order'],
              Decimal(d['price']),
              int(d['volume']),
              Decimal(d['commission']))
    return trade

def decode_financials(d):
    object_type = d.get("object", None)

    if object_type == "Stock":
        return decode_stock(d)
    elif object_type == "Trade":
        return decode_trade(d)
    return d

class CustomDecoder(json.JSONDecoder):
    def decode(self, arg):
        data = json.loads(arg)
        # now we have to recursively look for `Trade` and `Stock` objects
        return self.parse_financials(data)

    def parse_financials(self, obj):
        if isinstance(obj, dict):
            obj = decode_financials(obj)
            if isinstance(obj, dict):
                for key, value in obj.items():
                    obj[key] = self.parse_financials(value)
        elif isinstance(obj, list):
            for index, item in enumerate(obj):
                obj[index] = self.parse_financials(item)
        return obj

decoded = json.loads(encoded, cls=CustomDecoder)

print(decoded)
