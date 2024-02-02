lower_case = "erik"
upper_case = "ERIK"

def is_lower_or_upper(input_str):
  if input_str.isupper():
    print("String is uppercase")
  elif input_str.islower():
    print("String is lowercase")
  else:
    print("String is something else")
    
is_lower_or_upper(lower_case)
is_lower_or_upper(upper_case)
is_lower_or_upper("Erik")