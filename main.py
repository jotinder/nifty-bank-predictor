# Install requests package for python
import requests
 
# Set the request parameters
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=RELIANCE.BSE&outputsize=full&apikey=demo"'
 
# Set the user credentials
#user = 'username'
#pwd = 'password'
 
# Set the proper headers
headers = {"Accept":"application/json"}
 
# Make the HTTP request
#response = requests.get(url, auth=(user, pwd), headers=headers)
response = requests.get(url,headers=headers)

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.content)
    exit()
 
# Decode the XML response into a dictionary and use the data
print(response.content)
