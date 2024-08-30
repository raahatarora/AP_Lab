def compute_net_amount(transactions):

    balance = 0

    for transaction in transactions:
        parts = transaction.split()
        if len(parts) != 2:
            print("Invalid transaction format. Each transaction must have a type and an amount.")
            continue
        
        transaction_type = parts[0].upper()
        try:
            amount = int(parts[1])
        except ValueError:
            print(f"Invalid amount format: {parts[1]}")
            continue
        
        if transaction_type == 'D':
            balance += amount
        elif transaction_type == 'W':
            balance -= amount
        else:
            print(f"Invalid transaction type: {transaction_type}")
    
    return balance

def main():
    print("Enter transactions (type 'END' to finish):")
    
    transactions = []
    while True:
        transaction = input().strip()
        if transaction.upper() == 'END':
            break
        transactions.append(transaction)

    net_amount = compute_net_amount(transactions)
    
    print(f"Net amount in the bank account: {net_amount}")

if __name__ == "__main__":
    main()

