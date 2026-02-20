"""
Test the balance-inquiry API without curl. Run with: python test_api.py
(Make sure the server is running first: python main.py)
"""
import urllib.request
import json

BASE = "http://localhost:8000"

# Test GET
url = f"{BASE}/balance-inquiry?account_number=999888777666"
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode())
    print("GET /balance-inquiry response (accountNumber):", data["balanceInquiryRequest"]["accountDetail"]["accountIdentifier"]["accountNumber"])

# Test POST
url = f"{BASE}/balance-inquiry"
body = json.dumps({"account_number": "123456789012"}).encode()
req = urllib.request.Request(url, data=body, method="POST", headers={"Content-Type": "application/json"})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode())
    print("POST /balance-inquiry response (accountNumber):", data["balanceInquiryRequest"]["accountDetail"]["accountIdentifier"]["accountNumber"])

print("OK - API is working.")
