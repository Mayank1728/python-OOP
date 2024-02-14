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


  enumerate works only on lists
  use .items() to get key value pairs
"""

class System:
 def __init__(self):
  self.data = {}
 
 def add(self, ab):
  if ab.name not in self.data:
    self.data[ab.name] = ab
  else:
   print("Address Book already exists")

 def find(self, fname: str)->bool:
  for _, ab_obj in self.data.items():
   if fname in ab_obj.contacts.keys():
    print("Found", fname)
    print(ab_obj.contacts[fname])
    return True
  print("NOT found")
  return False
 
 def people_from(self, loc: str):
   for _, ab_obj in self.data.items():
     for name, val in ab_obj.contacts.items():
       if loc == val["city"] or loc == val["state"]:
         print(name)
         return True
   print("No one lives here..")
   return False
         
 def total_people_from(self, loc: str):
   count = 0
   for _, ab_obj in self.data.items():
     for name, val in ab_obj.contacts.items():
       if loc == val["city"] or loc == val["state"]:
         count += 1
   print(count, "Person found")
   return count  


class AddressBook:
 def __init__(self, name):
  self.name = name
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
     

 def __getitem__(self, key):
  if key in self.contacts:
   return self.contacts[key]
  else:
   return False

 def delete(self, fname):
  if fname in self.contacts:
   del self.contacts[fname]
   print(fname + " contact is deleted")
  else:
   print(fname + " Contact NOT found")
 
 def display(self):
  for person in self.contacts:
   print(self.contacts[person])

 def __str__(self) -> str:
  return "This is address book Object"


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
p3 = Contact("Sarah", "Tancredi", "rue Van Hecke 47", "London")
p4 = Contact("Michael", "Scofield", "61642 Zulauf Plaza", "Wisconsin")
p5 = Contact("Lincon", "Burrows", "Studio 66 Miller Parkways", "London")
p6 = Contact("T", "Bag", "5455 Bauch Pine Suite 150", "East Raheemborough")
book1 = AddressBook("book1")
book1.add(p1)
book1.add(p2)
book1.add(p3)
book1.add(p4)
book1.add(p5)
book1.add(p6)
# book1.edit_contact("Mayank", "city", "South Park")
# book1.delete("Sarah")
sys = System()
sys.add(book1)
# print(sys.data)
sys.people_from("LA")
sys.total_people_from("London")



