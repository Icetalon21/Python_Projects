#compound.py

def compound_interest_calculation():
    P = int(input("Enter in the principal: "))
    r = float(input("Enter in the interest rate: "))
    n = int(input("Enter in the number of compounding periods per year: "))
    t = int(input("Enter in the number of years: "))
    formula = P * ((1 + (r/n))**(n*t))
    print("The new balance after", t, "years is", formula)

compound_interest_calculation()
