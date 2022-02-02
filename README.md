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

### ADD ALIAS (MAC/LINUX)

If you will be encoding a lot of base64, or you want a fun exercise on the UNIX terminal, you can add an alias in your `.bash_profile` to make command invocation simpler. Add the following line to your `.bash_profile`:

```
alias b64e="python3 ~/.b64encode.py"
```
> NOTE: I have my python script saved as `.b64encode.py` in my home directory to keep it hidden and out of my way in everyday computer usage. Add path to your script accordingly. Change *b64e* to whatever you want the command alias to be.

After appending previous line to `bash_profile`, run the following command to commit changes:
```
source .bash_profile
```
> NOTE: Command was run from same directory as `.bash_profile`

You should now have the alias working in any directory. Example syntax:
```
b64e secret.txt encoded.b64
```
