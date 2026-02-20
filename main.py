import logging
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# Known accounts: account_number -> balance in Rs
ACCOUNT_BALANCES = {
    "1234567": 50_000,
}

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(message)s", datefmt="%H:%M:%S")
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Balance Inquiry API",
    description="Give account number, get balance. Account not found returns 404.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_balance(account_number: str) -> dict:
    """Return balance for account or raise 404."""
    logger.info("Balance inquiry | account_number=%s", account_number)
    if account_number not in ACCOUNT_BALANCES:
        logger.warning("Account not found | account_number=%s", account_number)
        raise HTTPException(status_code=404, detail="Account number does not exist")
    amount = ACCOUNT_BALANCES[account_number]
    logger.info("Balance found | account_number=%s | amount=%s Rs", account_number, f"{amount:,}")
    return {
        "account_number": account_number,
        "amount": amount,
        "currency": "Rs",
    }


class BalanceRequest(BaseModel):
    """Account number for balance inquiry."""

    account_number: str = Field(..., description="Account number")


@app.get("/balance-inquiry")
async def balance_inquiry_get(
    account_number: str = Query(..., description="Account number"),
) -> dict:
    """Get balance for an account. Returns amount and currency."""
    return get_balance(account_number)


@app.post("/balance-inquiry")
async def balance_inquiry_post(body: BalanceRequest) -> dict:
    """Get balance for an account. Returns amount and currency."""
    return get_balance(body.account_number)


if __name__ == "__main__":
    import uvicorn

    print("Starting server... Open in your browser: http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)
