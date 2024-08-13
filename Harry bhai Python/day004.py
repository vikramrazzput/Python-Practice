print ("Hello, do you know me. I am your first program");

"""

The syntax of a print statement looks something like this:

CODE:

print(object(s), sep=separator, end=end, file=file, flush=flush);
 
    Other Parameters of Print Statement
        1. object(s): Any object, and as many as you like. Will be converted to string before printed
        2. sep='separator': Specify how to separate the objects, if there is more than one. Default is ' '
        3. end='end': Specify what to print at the end. Default is '\n' (line feed)
        4. file: An object with a write method. Default is sys.stdout

"""


print ("Hello, do you know me. I am your first program", 6, 7, 8, sep="~"); # it seperates different elements
# Hello, do you know me. I am your first program~6~7~8

print ("Hey", 6, 7, sep="_", end= "4314811921");
# end must be None or a string, not int

"""

leading zeros in decimal integer literals are not permitted.
Binary: 0b (e.g., 0b1010 for binary 1010)
Octal: 0o (e.g., 0o123 for octal 123)
Hexadecimal: 0x (e.g., 0x1A3 for hexadecimal 1A3)

"""

print ("Kya haal hain", 23, end = "234");
print ("Hello")
# the print() printing all the objects in single line because we have change the value of end.Default is '\n' (line feed)
#  end='end': Specify what to print at the end. Default is '\n' (line feed)