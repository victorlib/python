# Some examples of reading text data files with different options
#
# The file sample.txt is a UTF-8 encoded text file with Windows
# line-endings (\r\n).

# (a) Reading a basic text file (UTF-8 default encoding)

print("Reading a simple text file (UTF-8)")
with open('sample.txt', 'rt') as f:
    for line in f:
        print(repr(line))

# (b) Reading a text file with universal newlines turned off
print("Reading text file with universal newlines off")
with open('sample.txt', 'rt', newline='') as f:
    for line in f:
        print(repr(line))

# (c) Reading text file as ASCII with repalcement error handling
print("Read text as ASCII with reaplcaement error handing")
with open('sample.txt', 'rt', encoding='ascii', errors='replace') as f:
    for line in f:
        print(repr(line))

# (d) Reading text file as ASCII with ignore error handing
print("Reading text as ASCII with ignore error handing")
with open('sample.txt', 'rt', encoding='ascii', errors='ignore') as f:
    for line in f:
        print(repr(line))

