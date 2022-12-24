def format_address(address_string):
  # Declare variables
  house_number = ""
  street_name = ""
  # Separate the address string into parts
  address_string = address_string.split()
  # Traverse through the address parts
  for number in address_string:
    # Determine if the address part is the
    # house number or part of the street name
    if number.isdigit():
      house_number = number
  # Does anything else need to be done 
  # before returning the result?
    else:
      street_name += number
      street_name += " "
  # Return the formatted string  
  return "house number {} on street named {}".format(house_number, street_name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"