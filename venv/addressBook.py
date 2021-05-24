class personDetails:
    #reference to the class

 def __init__(self,first,last,email,addresss,age,phone_number):
  #dunder method(two underscores)
  self.first_name=first
  self.last_name=last
  self.email=email
  self.address=addresss
  self.age=age
  self.phone_number=phone_number


 def full_name(self):
  #print(self.first_name+" " + self.last_name) string concatenation
  print(f"{self.first_name} {self.last_name}")


 #def __str__(self):
  #string magic methods
 # return string=" \n"


  print("Welcome to Akal's address book program")
  print("Kindly add your contact details")
#storing contact information into variables

  first_name=input("first name = ")
  last_name=input("last name = ")
  email=input("email = ")
  address=input("addrress = ")
  age=input("age = ")
  phone_number=("phone_number = ")


print("Thank you, your contact information has been received!")
# first_contact=personDetails(first,last,email,addresss,age,phone_number)
# first_contact.full_name()#class instance



