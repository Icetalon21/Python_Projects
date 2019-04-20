#compound_interest.py
def compound_interest_formula(principal, interest, iteration, year):
    return principal * ((1 + (interest/iteration))**(iteration*year))
    
def compound_interest_formula_display():
    P = int(input("Enter in the principal: "))
    r = float(input("Enter in the interest rate: "))
    n = int(input("Enter in the number of compounding periods per year: "))
    t = int(input("Enter in the number of years: "))
    
    print("The new balance after", t, "years is", compound_interest_formula(P, r, n, t))
    #passing the parameters
    
compound_interest_formula_display()
