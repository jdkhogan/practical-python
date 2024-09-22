# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
i = 0

extra_payment_start_month = int(input("What month does the extra payment start? "))
extra_payment_end_month =   int(input("What month does the extra payment end? "))
extra_payment =             int(input("How much is the extra payment? "))


while (principal > 0):
    # 1.7
    # principal = principal * (1 + rate/12) - payment
    # total_paid = total_paid + payment
    
    # 1.8
    # principal = principal * (1 + rate/12) - payment
    # total_paid = total_paid + payment
    # if (i < 12):
    #     principal = principal - 1000
    #     total_paid = total_paid + 1000
        
    # i = i + 1
    
    # 1.9
    principal = principal * (1 + rate/12) - payment
    total_paid = total_paid + payment
    if (i >= extra_payment_start_month and i <= extra_payment_end_month):
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
        
    i = i + 1
    
    if principal < 0:
        total_paid = total_paid + principal
        principal = 0
    
    # 1.10
    print(f'{i} {total_paid:0.2f} {principal:0.2f}')
    
# print(f'''Total paid: {round(total_paid, 2)}
# Month paid off: {i}''')
