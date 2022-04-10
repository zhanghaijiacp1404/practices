"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    NUMBER_OF_MONTHS = int(input("How many months? "))

    for month in range(1, NUMBER_OF_MONTHS + 1):
        #income = float(input("Enter income for month " + str(month) + ": "))
        income = float(input(f"Enter income for month {str(month)}: "))
        incomes.append(income)
    report_monthly_income(NUMBER_OF_MONTHS, incomes)

def report_monthly_income(NUMBER_OF_MONTHS, incomes):
    """This function will get the number of months and the corresponding income and print the result"""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, NUMBER_OF_MONTHS + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))
main()