import requests
from bs4 import BeautifulSoup
import zipfile
import argparse

# Create argument parser
parser = argparse.ArgumentParser(description='Export and unzip Odoo Studio customizations')
parser.add_argument('-s', '--server', help='Server', required=True)
parser.add_argument('-user', '--username', help='Odoo username', required=True)
parser.add_argument('-pwd', '--password', help='Odoo password', required=True)
parser.add_argument('-d', '--database', help='Odoo database', required=True)

# Parse command line arguments
args = parser.parse_args()

# Specify the URL of the controller
url = f"{args.server}/web_studio/export"

# You need to use the appropriate credentials
# We'll use session cookies for authentication
login_url = f"{args.server}/web/login?db={args.database}"
login_payload = {
    "login": args.username,
    "password": args.password,
    "redirect": "/web_studio/export",
}
# Send GET request to login page to obtain CSRF token
session = requests.Session()
response = session.get(login_url)

# Parse HTML response to find CSRF token
soup = BeautifulSoup(response.text, 'html.parser')
csrf_token = soup.find('input', {'name': 'csrf_token'})['value']

# Include CSRF token in login payload
login_payload['csrf_token'] = csrf_token

# Send login request with CSRF token to get the session cookies
response = session.post(login_url, data=login_payload)

if response.status_code == 200:
    print("Logged in successfully")
else:
    print("Login failed")

# Send the request to export studio customizations
response = session.get(url)

# Handle the response
if response.status_code == 200:
    zip_filename = 'studio_export.zip'
    with open(zip_filename, 'wb') as f:
        f.write(response.content)

    # Unzip the file
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall('.')

    print("Studio customizations unzipped successfully")
else:
    print(f"Error: {response.status_code}")
