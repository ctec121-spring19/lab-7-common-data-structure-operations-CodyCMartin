# dictionaries.py

# general instructions: 
#   - print a blank line between sections of output
#   - Add your comments using triple quotes. Example:
''' student comment'''

def main():
    '''
    - creation
    '''
    # create an empty dictionary named "dict" and print it

    dict = {}
    print(dict)

    # open your book to p. 401
    # create the "passwd" dictionary and print it

    passwd = {"guido":"superprogrammer" , "turing": "genius", "bill": "monopoly"}
    print(passwd)

    '''
    - element access
    '''
    # using the square bracket notation print out the value for "turing"

    print(passwd['turing'])

    '''
    - element updates
    '''
    # using the square bracket notation update the value for "turing" 
    # to "super genius", then print the dictionary

    '''
    - element insertion
    '''
    # add a new key value pair to passwd
    # key = "new key"
    # value = "new key value"

    # print passwd

    '''
    - element deletion
    '''
    # delete "turing" from passwd and print passwd

    '''
    - search
    '''
    # print the result of get("turing")

    # Use the "in" keyword to search the dictionary
    # print the value returned by ' "turing" in passwd '

    '''
    - some dictionary methods
    '''
    # print the list of keys

    # print the list of values

    # print the list of items - key-value pairs

    '''
    - deletion
    '''
    # delete all entries from passwd, then print it

main()