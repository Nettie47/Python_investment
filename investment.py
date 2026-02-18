"""
Program:investment.py
Nanette
2/18/26
Chapter 3 case study

Application that provides an investment report. User provides the details about the investment. Output is calculations for each year indivually and some final summaries
"""

# Input phase
startBalance = float(input("Please, enter the initial investment amount >> "))
years = int(input("Next, enter the number of years for the investment >> "))
rate = float(input("Finally, enter the annual interest rate as a % >> "))

# Processing phase
rate = rate / 100

# Initializing the accumulator variiable for the interest
totalInterest = 0.0

# Display the header for the table in tabular format
print() # gives a blank line for better readability
print("%4s%20s%12s%18s" % ("Year", "Starting Balance", "Interest", "Ending Balance"))

# Compute and display the results for each year using a FOR LOOP
for year in range(1, years + 1):
    interest = startBalance * rate
    endBalance = startBalance + interest
    print("%4d%20.2f%12.2f%18.2f" % (year, startBalance, interest, endBalance))
    startBalance = endBalance
    totalInterest += interest
 # end of loop

# Output phase displaying the totals
print("-" * 50)# gives a line of dashes for better readability
print("Final Balance: $%0.2f" % endBalance)
print("Total Interest Earned: $%0.2f" % totalInterest)

input("\nPress ENTER to quit...")
