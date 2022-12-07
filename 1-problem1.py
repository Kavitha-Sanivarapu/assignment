import re

# phone_number = "2124567890"
# phone_number = "212-456-7890"
# phone_number = "(212)456-7890"
# phone_number = "(212)-456-7890"
# phone_number = "212.456.7890"
# phone_number = "212 456 7890"
# phone_number = "+12124567890"
# phone_number = "+1 212.456.7890"
# phone_number = "+212-456-7890"
# phone_number = "1-212-456-7890"


def is_phone_number_valid(phone_number):
    return re.search("[-(+ \d{1}]*\d{3}[-). ]*\d{3}[-. ]*\d{4}", phone_number)


phone_number = input("Please enter a phone number: ")

if is_phone_number_valid(phone_number):
    print("It's a valid phone number")
else:
    print("It's not a valid phone number")
