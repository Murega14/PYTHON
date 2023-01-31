import phonenumbers

from phonenumbers import geocoder

phone_number = phonenumbers.parse(input("enter phone number: "))
print(geocoder.description_for_number(phone_number, 'en'))
