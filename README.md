# Balance Inquiry API

FastAPI backend on **port 8000**. Send an account number, get the balance. Unknown accounts return 404.

## Setup

```bash
cd BalanceInquiryTest
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate      # macOS/Linux
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

Server runs at **http://localhost:8000**. Open **http://localhost:8000/docs** for Swagger UI.

## Endpoints

| Method | Endpoint            | Description                    |
|--------|---------------------|--------------------------------|
| GET    | `/balance-inquiry`  | Get balance (query: `account_number`) |
| POST   | `/balance-inquiry`  | Get balance (body: `{"account_number": "..."}`) |

**Success (200)** — known account:
```json
{
  "account_number": "1234567",
  "amount": 50000,
  "currency": "Rs"
}
```

**Not found (404)** — unknown account:
```json
{
  "detail": "Account number does not exist"
}
```

## Test data

- **1234567** → balance **50,000 Rs**
- Any other account number → 404

## Examples

```bash
# GET
curl "http://localhost:8000/balance-inquiry?account_number=1234567"

# POST
curl -X POST http://localhost:8000/balance-inquiry -H "Content-Type: application/json" -d "{\"account_number\": \"1234567\"}"
```

Or use **http://localhost:8000/docs** and try the endpoints there.

## Project layout

- `main.py` — FastAPI app and balance logic
- `requirements.txt` — Python dependencies
- `test_api.py` — Script to test the API (run with server up)
- `server.js` / `package.json` — Optional Node server (not required for the API above)

CORS is enabled so the API can be called from browsers and other origins.
