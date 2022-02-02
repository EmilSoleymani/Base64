import sys

# String index i has correpsonding base64 value
base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

# Converts a binary string to its decimal value
def binStringToDec(string):
  n = len(string) - 1
  dec = 0
  for s in string:
    if s == '1':
      dec += 2**n
    n-=1
  return dec

# Converts character to binary string, stripping '0b' at beginning, and makes sure exactly 8 bits are reperesnted
def binaryString(char):
  string = bin(ord(char))[2:]
  while not len(string) == 8:
    string = '0' + string
  return string

# Encodes message with base64 
def base64encode(message):
  length = len(message)

  if length < 3:
    print("Error: String too short")

  binString = ''  
  for s in message:  # For each character in message
    binString += binaryString(s)  # Append 8 bits representing character to binString 
  
  # Make sure number of 8 bit intervals is divisible by 3 by adding extra '='
  if length % 3 == 1:
    binString += binaryString('=') * 2
  elif length % 3 == 2:
    binString += binaryString('=') * 1

  encodedMsg = ''
  for i in range(0, len(binString), 6):  # Loop 6 chars at a time 
    fragment = binString[i:i+6]
    dec = binStringToDec(fragment)  # Each 6 chars represent 6 bit which can have a value from 0-63
    encodedMsg += base64[dec]  # Append corresponding base64 character to encoded string
  return encodedMsg

# Encodes given plain file to encoded file
def encodeFile(plain, encoded):
    encodedLines = []
    with open(plain, "r") as f:
        for line in f:
            line = line.strip() # Strip leading empty spaces
            if len(line) > 0:   # Ignore empty lines 
                encodedLines.append(base64encode(line))
    # New file name logic
    if encoded == "":  # Default case
        if plain[0] == '.':   # e.g. .password.txt -> ['', 'password', 'txt']
            name = plain.split(".")[1]  # We need item 1 in array above
        else:  # e.g password.txt -> ['password', 'txt']
            name = plain.split(".")[0]  # We need item 0 in array above

        dest = name + ".b64"  # Append .b64 file extension by default
    else:
        dest = encoded

    with open(dest, "w") as f:
        for line in encodedLines:
            f.write(line)
            f.write("\n")

if __name__ == "__main__":
    source = ''
    dest = ''
    if len(sys.argv) == 3:
        source = sys.argv[1]
        dest = sys.argv[2]
        encodeFile(source, dest)
    elif len(sys.argv) == 2:
        source = sys.argv[1]
        encodeFile(source, "")
    else:
        print("Error: invalid number of arguments")
        exit()
        
