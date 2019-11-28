#!/usr/local/bin/python3

# Python 3 script to convert 12 hour clock format to 24 hour format
#
# e.g. 11:21:30 PM => 23:21:30
#      12:12:20 AM => 00:12:20
#
def time_convert_24(input_str):

    # Check for 12 ... AM
    if input_str[-2:] == 'AM' and input_str[:2] == '12':
        return "00" + input_str[2:8]

    # Remove the AM
    elif input_str[-2:] == 'AM':
        return input_str[:8]

    # Check for 12 ... PM
    elif input_str[-2:] == 'PM' and input_str[:2] == '12':
        return input_str[0:8]

    # otherwise add 12 to hours and remove 'PM'
    else:
        return str(int(input_str[:2]) + 12) + input_str[2:8]

