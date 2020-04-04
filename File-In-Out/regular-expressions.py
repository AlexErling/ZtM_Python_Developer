import re  # import for regular expressions

# used for matching patterns

pattern = re.compile('this')
string = 'search this this inside of this text please!'
a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)  # full match has to be identical
print(a.span())
print(b)
print(c)
# re returns an object

# becomes really useful for advanced patterns
# regex101.com
# https://regexone.com/
# pattern = re.compile(r"([a-zA-Z]).([a])")

 