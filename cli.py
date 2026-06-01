import argparse
import logging
from client import client

from validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:

    args.side = validate_side(args.side)
    args.type = validate_order_type(args.type)
    args.quantity = validate_quantity(args.quantity)
    args.price = validate_price(args.price, args.type)


    if args.type.upper() == "MARKET":

        order = client.futures_create_order(
            symbol=args.symbol,
            side=args.side,
            type="MARKET",
            quantity=args.quantity
        )

    elif args.type.upper() == "LIMIT":

        if not args.price:
            raise ValueError("Price required for LIMIT order")

        order = client.futures_create_order(
            symbol=args.symbol,
            side=args.side,
            type="LIMIT",
            quantity=args.quantity,
            price=args.price,
            timeInForce="GTC"
        )

    print("\nORDER SUCCESS")
    print("Order ID:", order["orderId"])
    print("Status:", order["status"])

    logging.info(order)

except Exception as e:
    logging.error(str(e))
    print("ERROR:", e)