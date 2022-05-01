# mortgage.py
# Exercise 1.7
# Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage, Stock Investment, 
# and Bitcoin trading corporation. The interest rate is 5% and the monthly payment is $2684.11.
# Here is a program that calculates the total amount that Dave will have to pay over the life of the mortgage:
# Exercise 1.8 - 1.9
# Modify the program so that extra payment information can be more generally handled. 
# Make it so that the user can set the extra payment variables
# Exercise 1.10
# Modify the program to print out a table showing the month, total paid so far, and the remaining principal.

principal = 500000.0;
rate = 0.05;
payment = 2684.11;
total_paid = 0.0;
months=0;

extra_payment_start_month = int(input("Extra payment starts at month (number): "))
print(extra_payment_start_month)
extra_payment_end_month = int(input("Extra payment ends at month (number): "))
print(extra_payment_end_month)
extra_payment = int(input("How much will you extra pay each month ($): "))
print(extra_payment)

while principal > 0:
    if(extra_payment_start_month <= months & months <= extra_payment_end_month):
        principal = principal - extra_payment;
        total_paid = total_paid + extra_payment;
    principal =  principal * (1+rate/12) - payment;
    total_paid = total_paid + payment;
    if(principal<0): #correct bug for negative principal in the last month
        total_paid =  total_paid - abs(principal);
        principal = 0;
    months += 1;
    print(months,round(total_paid,2),round(principal,2))

        

print('Total paid', round(total_paid,2));
print('Months',months);
