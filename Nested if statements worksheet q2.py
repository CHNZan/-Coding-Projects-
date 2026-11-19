income = int(input("Enter your monthly income : $"))
age = float(input("Enter your age: "))
spending_habits = input("Spending Habit Status: ")

if income < 2000 and age > 20 and age < 40 and spending_habits == "High" or spending_habits == "high":
    print('Suggesting a Basic Savings Plan... ')
    save_per_month = 10000 / (12 * 2)
    print(f'You need to save ${save_per_month} / month for 2 years in order to save $10,000')
elif income > 2000 and income < 5000 and spending_habits == "Moderate" or spending_habits == "moderate":
    print('Suggesting a Standard Savings Plan... ')
    save_per_month = income * 0.2
    print(f'You need to save ${save_per_month} monthly')
elif income > 5000 and age < 30 and spending_habits == 'Low' or spending_habits == 'low':
    print('Suggesting a Aggresive Investment Plan...')
    investment_income = (5 * 12 + (income * 12)) * 0.1
    print(f'Agressive Investment Plan Target: {investment_income}')
else:
    print('''TIPS:
- Invest in ETF's early for safe and low risk income
- Get a credit card early , dont overspend your credit card , and earn credit score for higher loan limits
- Always plan your income spendings early ( e.g. 50/30/20 rule )
- ALWAYS have an emergency savings account with atleast 6 months worth of savings''')