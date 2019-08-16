def main():
    print('[evaluate codebreaker]')
    
    choice = 0
    
    while (choice != '3'):
        choice = input('What would you like to do? [1] Decrypt, [2] Encrypt [3] Quit: ')
        if choice == '1':
            # ask for input file
            file_name = input('Enter the input filename to decrypt (don\'t include .txt): ') # secret_code.txt
            
            # open and read file
            code_file = open(file_name+'.txt', 'r')
            code_data = code_file.read()
            code_file.close()
            
            # put code into list
            code_list = code_data.splitlines()
            
            # decipher code
            for item in code_list:
                # this is so that if an empty line is in the text document 
                # the empty line doesn't get evaluated
                if len(item) > 0:
                    try : 
                        code, key = item.split(' ')
                        print(decrypt(code,key))
                    except ValueError :
                        # occurs when key isnt present
                        print('Missing key! Attempting brute force...')
                        attempts = bruteForce(item)
                        for attempt in attempts:
                            print(attempt);
                        
        elif choice == '2':
            # ask for output file
            file_name = input('Enter the output filename to decrypt (don\'t include .txt): ')
            
            code = input('Enter the message you\'d like to encrypt (letters only): ').upper()
            key = input('Choose a numerical value for the key (between 1 and 25 inclusive): ')
            
            code = encrypt(code, key)
            
            include = input('Would you like to include the key? y/n: ')
            if include != 'y':
                key = ''
            # open and write to file
            code_file = open(file_name+'.txt', 'w')
            code_data = code_file.write(code + ' ' + key)
            code_file.close()
            
    
def decrypt(code, key):
    deciphered_word = ''
    for letter in code:
        letter_ASCII = ord(letter) 
        deciphered_ASCII = letter_ASCII + int(key)
        if deciphered_ASCII > ord('Z'):
            deciphered_ASCII -= 26
        elif deciphered_ASCII < ord('A'):
            deciphered_ASCII += 26
        deciphered_letter = chr(deciphered_ASCII)
        deciphered_word = deciphered_word + deciphered_letter
    return deciphered_word

def bruteForce(code):
    brute_force_list = []
    for key in range(26):
        brute_force_list.append('    '+decrypt(code, key))
    return brute_force_list

def encrypt(not_code, key):
    code = ''
    for letter in not_code:
        letter_ASCII = ord(letter) 
        ecrypted_ASCII = letter_ASCII - int(key)
        if ecrypted_ASCII > ord('Z'):
            ecrypted_ASCII -= 26
        elif ecrypted_ASCII < ord('A'):
            ecrypted_ASCII += 26
        ecrypted_letter = chr(ecrypted_ASCII)
        code = code + ecrypted_letter    
    return code
main()