# file = open("sample.txt")
#
# print(file)
# print(file.name)
# lines = file.readlines()
# # only reads once - open function has a cursor
# print(lines)
# for line in lines:
#     print(line)
#
# # need to close the file
# file.close()

# can you with instead, don't need to close file
# set the mode to read or write
# r+ == read and write
try:
    with open('sample.txt', mode='w') as my_file:
        text = my_file.write("Adding text to file")
        print(text)  # number of char written to file
except FileExistsError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print("IO Error")
    raise err
# a is append mode, adds to end of file
# w writes to a file - is assuming a new file and clears all content before hand
# in r+ you overwrite the current content
# w can create a new file as well if it doesn't exist

# Can give absolute paths!

# Path lib module
