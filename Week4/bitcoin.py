# In a file called bitcoin.py, implement a program that:

#   Expects the user to specify as a command-line argument the number of Bitcoins, n that they would like to buy. 
#   If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
#   Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, 
#   which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch 
#   any exceptions
#   Outputs the current cost of n Bitcoins in USD to four decimal places, using , as a thousands separator.

import sys, requests, json
if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = (requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")).json()
    rate = float(response["bpi"]["USD"]["rate"].replace(",", ""))
    value = rate*n
    print(f"${value:,.4f}")
except requests.RequestException:
    pass
