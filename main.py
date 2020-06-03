from solutions import *

def main():
  # call the is_sweltering() function and output a response
  if (is_sweltering()):
    print("Oh no, it is sweltering hot today!")
  else:
    print("Thankfully, it's not too hot today.")

  # call the is_warm() function and output a response
  if (is_warm()):
    print("Ok... I suppose warm is ok!")
  else:
    print("It's not warm today.")

  # call the is_humid() function and output a response
  if (is_humid()):
    print("Ugh... another humid day.")
  else:
    print("I'm so happy it's not humid today!")

  # call the is_inclement() function and output a response
  if (is_inclement()):
    print("Take your umbrella!")
  else:
    print("No need to take your umbrella!")

  # call the is_typical_new_york_summer() function and output a response
  if (is_typical_new_york_summer()):
    print("A typical summery day in New York!")
  else:
    print("We must not be in New York anymore.")

  # call the is_typical_new_york_summer() function and output a response
  if (is_cool_and_nice()):
    print("Such a cool and nice day today!")
  else:
    print("I wish it were cool and nice today.")

# call the main function
main()
