

#Nicole Ajjan, CMP-131, Week 4, Lab 2, Interest Earned, September 15, 2026

principal = float(input("Enter the starting principal balance: "))
annualrate = float(input("Enter the annual interest rate: "))
yearlycompound = int(input("Enter the number of times interest is compounded per year: "))
rate = annualrate / 100.0
amount = principal * (1 + rate / yearlycompound) ** yearlycompound


print("\n--- Savings Account Report ---")
print(f"Interest Rate: {annualrate}%")
print(f"Times Compounded: {yearlycompound}")
print(f"Starting Principal: ${principal:.2f}")
print(f"Balance after 1 Year: ${amount:.2f}")
