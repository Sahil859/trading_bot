# Binance Futures Testnet Trading Bot

## Overview

This project is a simple Python-based trading bot that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

Features:

* Place MARKET orders
* Place LIMIT orders
* Supports BUY and SELL
* CLI-based input using argparse
* Logging of API requests and responses
* Exception handling
* Input validation

## Requirements

* Python 3.x
* Binance Futures Testnet Account
* API Key and Secret

## Installation

Install dependencies:

pip install -r requirements.txt

## Configuration

Update your API credentials in client.py:

API_KEY = "YOUR_API_KEY"

API_SECRET = "YOUR_API_SECRET"

## Run Examples

### MARKET BUY Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### MARKET SELL Order

python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001

### LIMIT BUY Order

python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 95000

### LIMIT SELL Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 110000

## Project Structure

trading_bot/

├── client.py

├── cli.py

├── validators.py

├── README.md

├── requirements.txt

└── bot.log

## Assumptions

* User has a valid Binance Futures Testnet account.
* API credentials are active.
* Internet connection is available.
* Trading is performed only on Binance Futures Testnet.

## Logging

All order activity and errors are stored in:

bot.log

## Error Handling

The application handles:

* Invalid side values
* Invalid order types
* Invalid quantities
* Missing price for LIMIT orders
* Binance API errors
* Network failures
