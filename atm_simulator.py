correct_pin = 1234
balance = 100000

pin = int(input("Enter ATM Pin: "))

if pin == correct_pin:
    withdr = int(input("Amount to Withdraw: "))

    if withdr <= 0:
        print("Thank you for using ATM")
    elif withdr <= balance:
        balance = balance - withdr
        print("Collect Money ....")
        print(f"Remaining Balance: {balance}")
    else:
        print("Insufficient Balance")
else:
    print("Access Denied, Invalid PIN")
