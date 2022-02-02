# BASE-64 ENCODING / DECODING

### ABOUT
	Base-64 encoding is a widely used in computer programming to implement binary to text encoding and vice verse. More info is available [on Wikipedia](https://en.wikipedia.org/wiki/Base64).

### ENCODING
	The python file **b64encode.py** handles the encoding process. It is meant to be invoked from the command line with the passage of 1 or 2 arguments. The argument for the source file is mandatory, while the argument for the destination is not, as it will default to the current directory with a default name of *filename*.b64. Example invocations can be copied into the command line:

##### SINGLE ARGUMENT
```
python3 b64encode.py password.txt
```
##### DOUBLE ARGUMENT
```
python3 b64encode.py password.txt encoded.b64
```
