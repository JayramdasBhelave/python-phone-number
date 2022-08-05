import phonenumbers
from phonenumbers import timezone,geocoder, carrier
number=input("Enter your no. with +__: ")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
# Validating a phone number
valid = phonenumbers.is_valid_number(phone)

# Checking possibility of a number
possible = phonenumbers.is_possible_number(phone)

print(phone)
print("The timezone of the given phone number is: ", time)
print("Service Provider is: ",car)
print("The region of the given phone number is: ", reg)
print("Is the given phone number is valid?: ", valid)
print("Is the given phone number is possible?: ",possible)