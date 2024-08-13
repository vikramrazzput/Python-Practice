# use of double quotes inside a string

print ("Hey where are you going ?");  # this is possible

# print ("Hey, "How are you" ?");  # this is not possible

# to overcame this
print ("Hey, \"How are you\" ?");  # this is, how it's possible

# NOTE: [ \"  ] this is also a space sequence character

"""

Escape Sequence Characters:
To insert characters that cannot be directly used in a string, we use an escape sequence character.

An escape sequence character is a backslash ( \ ) followed by the character you want to insert.

"""


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