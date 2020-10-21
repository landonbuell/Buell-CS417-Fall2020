"""
Landon Buell
Alejo hausner
CS 417.01 - Lab11
20 Oct 2020
"""

upto_ten = range(1,11)

# Exercise 1:
evens_to_20 = [x for x in range(1,21) if x % 2 == 0]

# Exercise 2:
upto_ten_odd = [x for x in upto_ten if x % 2 != 0]

# Exercise 3:
upto_10_squares = [x**2 for x in upto_ten]

# Exercise 4:
upto_10_and_square = [[x,x**2] for x in upto_ten]

# Exercise 5:
upto_5_pairs = [[x,y] for x in range(1,6) for y in range(1,6)]

# Exercise 6:
upto_5_products = [x*y for x in range(1,6) for y in range(1,6)]

# Exercise 7:
matrix = [[1,2,3], [4,5,6], [7,8,9,10], [11,12]]
flattened = []
flattened = ["flattened not implemented! Help?"]


# Exercise 8:
names = ['Jim', 'Jan', 'Zaphod', 'David', 'Bart', 'Lisa']
initials = [name[0] for name in names ]

# Exercise 9:
people = [['Malinda',1.5], ['Indrajit', 1.6], ['Lake', 2.1], ['Seetha', 1.7],
          ['Ronny', 1.5], ['Pauline', 1.7], ['Nanna', 1.75]]
tall_people = [x[0] for x in people if x[1] > 1.7 ]

# Exercise 10:
employees = [
    [1,'Bagley','Malinda R',12],
    [2,'Wray','Indrajit H',15],
    [3,'Stacks','Lake N',12],
    [4,'Herberts','Seetha S',15.75],
    [5,'Ingham','Ronny R',12.50],
    [6,'Styles','Pauline G',12],
    [7,'Morse','Nanna E',12.50],
    [8,'Midgley','Thankful R',12.50],
    [9,'Apted','Shevaun A',15],
    [10,'Jewell','Keeleigh M',15],
    [11,'Vilhjalmsson','Napier Z',15],
    [12,'Kay','Hanna L',12]
]
ids = [employee[0] for employee in employees]

# Exercise 11:
high_pay_rates = [[x[1],x[-1]] for x in employees if x[-1] >= 15]

# Exercise 12:
colors = ['red','green','yellow']
things = ['tree','house','ball']
colored_things = [[x,y] for x in colors for y in things]

print ("evens_to_20:",evens_to_20)
print ("upto_ten_odd:",upto_ten_odd)
print ("upto_10_squares:",upto_10_squares)
print ("upto_10_and_square:",upto_10_and_square)
print ("upto_5_pairs:",upto_5_pairs)
print ("upto_5_products:",upto_5_products)
print ("flattened:",flattened)
print ("initials:",initials)
print ("tall_people:",tall_people)
print ("ids:",ids)
print ("high_pay_rates:",high_pay_rates)
print ("colored_things:",colored_things)
