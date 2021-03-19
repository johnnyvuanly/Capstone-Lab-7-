import requests

from pprint import pprint

def main():
    currency = get_target_currency()
    bitcoins = get_bitcoin_amount()
    converted = convert_bitcoin_to_target(bitcoins, currency)
    display_result(bitcoins, converted, currency)

def get_target_currency():
    """ Get target currency, and return as uppercase symbol """
    currency = input('Enter target currency code e.g. EUR, USD, GBP: ')
    return currency.upper()

def get_bitcoin_amount():
    """ Get number of bitcoin. """
    return float(input('Enter the number of bitcoin: '))

def convert_bitcoin_to_target(bitcoins, target_currency):
    """ Convert amount of bitcoin to dollars """
    exchange_rate = get_exchange_rate(target_currency)
    converted = convert(bitcoins, exchange_rate)
    return converted

def get_exchange_rate(currency):
    """ Call API and extra data from responses """
    response = request_rates(currency)
    rate = extract_rate(response, currency)
    return rate

def request_rates(currency):
    """ Perform API request, return response """
    params = {'bpi': currency}
    url = 'https://api.coindesk.com/v1/bpi/currentprice/'
    return requests.get(url, params=params).json()

def extract_rate(rates, currency):
    """ Process the JSON response from the API, extract rate data """
    return rates['bpi'][currency]['rate_float']

def convert(amount, exchange_rate):
    """ Convert using the given exchange rate """ 
    return amount * exchange_rate

def display_result(bitcoins, currency, converted):
    """ Format and display the result """
    print(f'{bitcoins} Bitcoin is equivalent to {converted:.2f} {currency}')

if __name__ == '__main__':
    main()