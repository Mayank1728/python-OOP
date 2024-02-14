"""
 Overall structure of
 
 AddressBook Object
  contacts = {
   "mayank" : Contact Obj
   "Sarah" : Contact Obj
   }
 
 Contact Object
  details = {
   "fname" : ...
   "lname" : ...
   "city" : ...
   ...
  }
"""


class AddressBook:
 def __init__(self):
  self.contacts = {}
 
 def add(self, contact):
  if contact["fname"] not in self.contacts:
    self.contacts[contact["fname"]] = contact
  else:
   print("Contact already Exists")
 
 def edit_contact(self, fname, att, value)->bool:
  if fname in self.contacts and self.contacts[fname][att]:
   self.contacts[fname][att] = value
   print(fname + "'s Contact was Edited")
   print(self.contacts[fname])
  else:
   print(fname + " Contact NOT found")
  # O(1) Time Complexity
 
 def delete(self, fname):
  if fname in self.contacts:
   del self.contacts[fname]
   print(fname + " contact is deleted")
  else:
   print(fname + " Contact NOT found")
 
 def display(self):
  for person in self.contacts:
   print(self.contacts[person])


class Contact:
 def __init__(self, fname, lname, address, city):
  self.detail = {}
  self.detail["fname"] = fname
  self.detail["lname"] = lname
  self.detail["address"] = address
  self.detail["city"] = city
  self.detail["state"] = "Haryana"
  self.detail["zip"] = "122001"
  self.detail["ph"] = "7290833669"
  self.detail["email"] = "mm1919@srmist.edu.in"
 
 def __getitem__(self, key):
  # TODO try catch block
  if key in self.detail:
   return self.detail[key]
  else:
   return False
  
 def __setitem__(self, key, value):
  # can add try catch block
  if key in self.detail:
   self.detail[key] = value
  else:
   return False
  
 def __str__(self) -> str:
  return self.detail["fname"] + " " + self.detail["lname"] + " " + self.detail["address"] + " " + self.detail["city"]
 # + " " + self.detail["state"] +  " " + self.detail["ph"] 
 # + " " + self.detail["email"]
  
p1 = Contact("Mayank", "Mudgal", "3867 Treutel Greens", "LA")
p2 = Contact("Sucre", "", "49 Paucek Lane", "Detroit")
p3 = Contact("Sarah", "Tancredi", "rue Van Hecke 47", "Torhout")
p4 = Contact("Michael", "Scofield", "61642 Zulauf Plaza", "Wisconsin")
p5 = Contact("Lincon", "Burrows", "Studio 66 Miller Parkways", "London")
p6 = Contact("T", "Bag", "5455 Bauch Pine Suite 150", "East Raheemborough")
print(p1["fname"])
book = AddressBook()
book.add(p1)
book.add(p2)
book.add(p3)
book.add(p4)
book.add(p1)
book.add(p5)
book.add(p6)
book.edit_contact("Mayank", "city", "South Park")
book.delete("Sarah")
# book.display()


