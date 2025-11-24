Bank_Account = []

def make_acount():
    print("\n..... Create a New Account .....")
    username = input("Name: ").strip()
    pin_code = input("Choose a 4-digit PIN: ").strip()

    account = {
        "user": username,
        "pin": pin_code,
        "balance": 0.0
    }

    Bank_Account.append(account)
    print("Account created!\n")


def find_acount():
    print("\n..... Login .....")
    username = input("Name: ").strip()
    pin_code = input("PIN: ").strip()

    for acct in Bank_Account:
        if acct["user"] == username and acct["pin"] == pin_code:
            print("Logged in successfully.\n")
            return acct

    print("Incorrect credentials!!\n")
    return None


def add_money(acct):
    print("\n..... Deposit .....")
    try:
        amount = int(input("Amount to be deposited: "))
        acct["balance"] += amount
        print(f"New balance: {acct['balance']}\n")
    except ValueError:
        print("Invalid amount!!\n")


def take_money(acct):
    print("\n..... Withdraw .....")
    try:
        amount = int(input("Amountt to be withdrawn: "))
        if amount > acct["balance"]:
            print("Insufficient funds!!\n")
        else:
            acct["balance"] -= amount
            print(f"Remaning balance: {acct['balance']}\n")
    except ValueError:
        print("Invalid amount!!\n")


def view_balance(acct):
    print("\n..... Acount Summary .....")
    print(f"Account Holder: {acct['user']}")
    print(f"Current Balance: {acct['balance']}\n")


def main():
    while True:
        print("..... BANKING SYSTEM .....")
        print("1) Create Account")
        print("2) Login")
        print("3) Quit")

        choice = input("Select: ").strip()

        if choice == "1":
            make_acount()

        elif choice == "2":
            active = find_acount()
            if active:
                while True:
                    print("\n..... Account Options .....")
                    print("1) Deposit")
                    print("2) Withdraw")
                    print("3) Check Balance")
                    print("4) Logout")

                    option = input("Select: ").strip()

                    if option == "1":
                        add_money(active)
                    elif option == "2":
                        take_money(active)
                    elif option == "3":
                        view_balance(active)
                    elif option == "4":
                        print("Logged out.\n")
                        break
                    else:
                        print("Invalid choice!!\n")

        elif choice == "3":
            print("Goodbye........")
            break

        else:
            print("Invalid menu option\n")


if __name__ == "__main__":
    main()

