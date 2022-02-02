import sys

base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def binStringToDec(string):
  n = len(string) - 1
  dec = 0
  for s in string:
    if s == '1':
      dec += 2**n
    n-=1
  return dec

def binaryString(char):
  string = bin(ord(char))[2:]
  while not len(string) == 8:
    string = '0' + string
  return string

def base64encode(message):
  length = len(message)

  if length < 3:
    print("Error: String too short")

  binString = ''
  for s in message:
    binString += binaryString(s)
  
  if length % 3 == 1:
    binString += binaryString('=') * 2
  elif length % 3 == 2:
    binString += binaryString('=') * 1

  # print(binString)

  encodedMsg = ''
  for i in range(0, len(binString), 6):
    fragment = binString[i:i+6]
    dec = binStringToDec(fragment)
    # print(fragment + ", " + str(dec))
    encodedMsg += base64[dec]
  return encodedMsg

def encodeFile(plain, encoded):
    encodedLines = []
    with open(plain, "r") as f:
        for line in f:
            line = line.strip()
            if len(line) > 0:
                encodedLines.append(base64encode(line))
    
    if encoded == "":
        if plain[0] == '.':
            name = plain.split(".")[1]
        else:
            name = plain.split(".")[0]

        dest = name + ".b64"
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
        
