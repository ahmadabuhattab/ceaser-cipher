"""
Author: Ahmad Abu Hattab
Date: 02/24/2022
Decrypt a message using the ceaser cipher, but with a kick.
"""

# Input
# (A message to decrypt [any string])
from decimal import Overflow

'''
DECODE: Elqeh mw er Eqedmrk fsc!
shift: 4
'''

message = input('Enter a message to be decrypted: ')
shift = int(input('Enter a shift amount: '))
# Processing
# a b c d e f ... w x y z (z + 2? = b)
# 1 2 3 4 5 6 ... (1 + 2 = 3)
decrypted_message = ''




for char in message:
    # Convert the letter to a number
    char_num = ord(char)
    if char.isalpha():
        if char.islower():
                # Then add a shift to the number
                    char_num = ord(char)
                    # Then add a shift to the number
                    char_num = char_num - shift
                    if char_num > ord('z'):  ## if the character number is bigger than the z order, then the over flow would be the character number minus the order of z. Then the character number would first start at the order of a then add the extra overflow
                        overflow = char_num - ord('z') - 1
                        char_num = ord('a') + overflow
                    # Convert the shifted number back to a character
                    # and add it to our decrypted message
                    decrypted_message = decrypted_message + chr(char_num)

        else:
                char_num = ord(char)
                # Then add a shift to the number
                char_num = char_num - shift
                if char_num > ord('Z'):  ## if the character number is bigger than the z order, then the over flow would be the character number minus the order of z. Then the character number would first start at the order of a then add the extra overflow
                    overflow = char_num - ord('Z') - 1
                    char_num = ord('A') + overflow
                # Convert the shifted number back to a character
                # and add it to our decrypted message
                decrypted_message = decrypted_message + chr(char_num)
    else:
        decrypted_message = decrypted_message + char


print(decrypted_message)