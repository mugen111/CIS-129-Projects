# Author: Mary Ellen Fitzpatrick # Module 3 lab #  Interactive text based Coffee Shop

print ("***************************************")
print ("My Coffee and Muffin Shop")
ncoffee = int(input("Number of coffees bought?\n"))
nmuffins = int(input("Number of muffins bought?\n"))
nbrownie = int(input("number of brownies bought?\n"))
nscones = int(input("number of scones bought?\n"))
print ("***************************************\n")
print ("***************************************")

cprice = 5.0 * ncoffee
mprice = 4.0 * nmuffins
bprice = 3.0 * nbrownie
sprice = 4.0 * nscones

print ("My Coffee and Muffin Shop Receipt")
print ("1 Coffee at $5 each: $", cprice)
print ("2 Muffins at $4 each: $", mprice)
print ("1 Brownie at $3 each: $", bprice)
print ("2 Scones at $4 each: $", sprice)
total = cprice + mprice + bprice + sprice
tax = 0.06 * total
print ("6% tax: $", tax)
print ("---------")
print ("Total: $", total + tax)
print ("Thank you for coming by. We hope to see you again soon!")
print ("***************************************")





