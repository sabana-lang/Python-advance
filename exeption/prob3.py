class InsufficientBalanceError(Exception):
    pass
try:
    n=int(input("Enter an amount:"))
    balance=int(input("Enter the balance:"))
    if balance<n:
        raise InsufficientBalanceError("Not enough balance.Transaction Failed ")
    else:
        print("Transaction success")
except InsufficientBalanceError as e:
    print(e) 



