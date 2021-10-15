#!/usr/bin/env python

import sys, getopt, bech32

# e.g. ./convert-address.py -a rv1qf2x63qx4jdaxj83kkw2yytehvvmu6r2xll5gcp6c9rancmrfsgfwttnczx
instructions = './convert-address.py -a <rn1/rv1/tn1/tv1 address>'

def main(argv):
  input_address = None
  try:
    opts, args = getopt.getopt(argv,"ha:",["address="])
  except getopt.GetoptError:
    print(instructions)
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print(instructions)
      sys.exit()
    elif opt in ("-a", "--address"):
      input_address = arg
  if input_address == None:
    print(instructions)
    sys.exit(2)

  # Decode input address into human-readable part, e.g. 'rn', and data
  input_hrp, data = bech32.bech32_decode(input_address)

  input_note = None
  output_note = None

  print(input_address[1:2])

  # determine what type of address to convert to
  if input_address[1:2] == "n": # rn or tn
    target_hrp = input_address[:1] + 'v'
    input_note = 'Node'
    output_note = 'Validator'
  elif input_address[1:2] == "v": # rv or tv
    target_hrp = input_address[:1] + 'n'
    input_note = 'Validator'
    output_note = 'Node'

  # Encode data with target human-readable part, e.g. 'rv' to get address
  output_address = bech32.bech32_encode(target_hrp, data)

  print("Input Address  :", input_address, "(", input_note, ")")
  print("Output Address :", output_address, "(", output_note, ")")

if __name__ == "__main__":
  main(sys.argv[1:])
