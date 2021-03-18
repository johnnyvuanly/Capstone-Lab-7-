import requests

from pprint import pprint

def main():
    bitcoins = get_bitcoin_amount()
    converted = convert_bitcoin_to_dollars(bitcoins)
    display_result(bitcoins, converted)

def get_bitcoin_amount():
    """ Get number of bitcoin. """
    return float(input('Enter the number of bitcoin: '))

def convert_bitcoin_to_dollars(bitcoins):
    """ Convert amount of bitcoin to dollars """
    exchange_rate = get_exchange_rate()
    converted = convert(bitcoins, exchange_rate)
    return converted

def get_exchange_rate(currency):
    """ Call API and extra data from responses """
    response = requests.get(currency)
    rate = extract_rate(response, currency)
    return rate

def request_rates():
    """ Perform API request, return response """
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    return requests.get(url).json()

def extract_rate(rates, currency):
    """ Process the JSON response from the API, extract rate data """
    return rates['bpi']['USD']['rate_float']

def convert(amount, exchange_rate):
    """ Convert using the given exchange rate """ 
    return amount * exchange_rate

def display_result(bitcoins, converted):
    """ Format and display the result """
    print(f'{bitcoins} Bitcoin is equivalent to ${converted:.2f}')

if __name__ == '__main__':
    main()