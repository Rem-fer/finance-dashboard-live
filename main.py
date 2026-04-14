print("Starting...")
from dotenv import load_dotenv
from auth import get_access_token
from db_operations import save_all_transactions_to_db, save_daily_balance_snapshot, categorise_transactions
from account_data import get_accounts_info, get_account_ids, fetching_all_transactions, get_all_accounts_balance

load_dotenv()
PROVIDERS = ["BARCLAYS", "REVOLUT", "BARCLAYCARD"]
if __name__ == "__main__":
    for provider in PROVIDERS:
        access_token = get_access_token(provider)
        if not access_token:
            print(f"No token for {provider}, skipping")
            continue

        accounts_info = get_accounts_info(provider)
        bank_ids = get_account_ids(accounts_info, account_type=["TRANSACTION", "SAVINGS"])
        card_ids = get_account_ids(accounts_info, account_type=["CREDIT"])

        for ids, is_card in [(bank_ids, False), (card_ids, True)]:
            if not ids:
                continue
            all_transactions = fetching_all_transactions(access_token, ids, is_card)
            save_all_transactions_to_db(all_transactions, provider)
            balance_info = get_all_accounts_balance(access_token, ids, is_card)
            save_daily_balance_snapshot(balance_info)


    categorise_transactions()