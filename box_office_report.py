#Nicole Ajjan, CMP-131, LAB2, SEPTEMBER 10,2026

AdultTix = 10.00
ChildTix = 6.00
TheaterCut = 0.20

movie = input("Enter the name of the movie: ")
atix = int(input("Enter the number of adult tickets sold: "))
ctix = int(input("Enter the number of child tickets sold: "))

grossatix = atix * AdultTix
grossctix = ctix * ChildTix
grossbox = grossatix + grossctix

netbox = grossbox * TheaterCut
distributor = grossbox - netbox

print("\n----------------- BOX OFFICE REPORT -----------------")
print(f"Movie Name:              '{movie}'")
print(f"Adult Tickets Sold:      {atix}")
print(f"Child Tickets Sold:      {ctix}")
print(f"Gross Box Office Profit: ${grossbox:,.2f}")
print(f"Amount Paid to Distributor: ${distributor:,.2f}")
print(f"Net Box Office Profit (Theater): ${netbox:,.2f}")
print("-----------------------------------------------------")

