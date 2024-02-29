#!/usr/bin/env python
# coding: utf-8

# In[24]:


print ("***************************************")
print ("My Coffee and Muffin Shop")
ncoffee = int(input("Number of coffees bought?\n"))
nmuffins = int(input("Number of muffins bought?\n"))
print ("***************************************\n")
print ("***************************************")

cprice = 5.0 * ncoffee
mprice = 4.0 * nmuffins

print ("My Coffee and Muffin Shop Receipt")
print ("1 Coffee at $5 each: $", cprice)
print ("2 Muffins at $4 each: $", mprice)
total = cprice + mprice
tax = 0.06 * total
print ("6% tax: $", tax)
print ("---------")
print ("Total: $", total + tax)
print ("***************************************")


# In[ ]:




