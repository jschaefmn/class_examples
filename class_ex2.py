# Write function to alternate upper and lower case
def to_spongebob_case(input_str):
  return_string = ""
  # code goes here
  # split input, assign even number to lowercase, odd number to upper
  for i, c in enumerate(input_str):
    if i % 2 == 0:
      return_string += c.lower()
    else:
      return_string += c.upper()
    
  
  return return_string


sb_name = to_spongebob_case("jacob schaefbauer")
print(sb_name)
