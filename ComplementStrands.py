__authors__ = "Morgan Bakelmun"
__maintainer__ = "Morgan Bakelmun"
__email__ = "morganbakelmun@hotmail.com"

# Function for verifying that only valid base codes are in the input string.
def validate_sequence(sequence):
    valid_characters = {'A', 'B', 'C', 'D', 'G', 'H', 'I', 'K', 'M', 'N', 'R', 'S', 'T', 'V', 'W', 'Y'}
    for char in sequence:
        if char not in valid_characters:
            print(f"Invalid character '{char}'.")
            return False
    return True

# Gets the compliment of the DNA string
def get_complement(sequence):
    # Nucleotide codes, including ambiguous codes
    complements = {'A': 'T',
                   'T': 'A',
                   'C': 'G',
                   'G': 'C',
                   'R': 'Y',
                   'Y': 'R',
                   'H': 'D',
                   'D': 'H',
                   'V': 'B',
                   'B': 'V',
                   'K': 'M',
                   'M': 'K',
                   'S': 'S',
                   'W': 'W',
                   'N': 'N',
                   'I': 'I'}
    
    # Generate the complement sequence
    complement_sequence = ''.join(complements[base] for base in sequence)
    return complement_sequence

# Reverse the DNA string
def get_reverse(sequence):
    return sequence[::-1]

#Start of the script. This is a TUI for a menu to select what strand you're starting with.
print("Which type of sequence is this? Please type one of these numbers.")
print("1. Forward")
print("2. Reverse")
print("3. Forward Complement")
print("4. Reverse Complement")

# First menu. User must select what strand they are providing.
while True:
    # User input
    selection = input("Enter the number corresponding to the sequence type: ")

    if selection not in ['1', '2', '3', '4']:
        print("Invalid input! Please enter a number between 1 and 4.")
    else:
        if selection == '1':
            input_type = 'forward'
        elif selection == '2':
            input_type = 'reverse'
        elif selection == '3':
            input_type = 'forward-comp'
        else:
            input_type = 'reverse-comp'
        break

# Second menu. Now user must type/paste their DNA sequence.
while True:
    # User input
    input_sequence = input("Please type your DNA sequence: ")
    #In the event the user typed in lowercase, make it upper case.
    input_sequence = input_sequence.upper()
    
    if not validate_sequence(input_sequence):
        print("Invalid DNA sequence.")
    else:
        break

# From whichever input was used, determine the other three.
try:
    match input_type:
        case 'forward':
            forward = input_sequence
            forward_complement = get_complement(forward)
            reverse = get_reverse(input_sequence)
            reverse_complement = get_complement(reverse)
            print("Forward: " + forward)
            print("Forward Complement: " + forward_complement)
            print("Reverse: " + reverse)
            print("Reverse Complement: " + reverse_complement)
        case 'reverse':
            forward = get_reverse(input_sequence)
            forward_complement = get_complement(forward)
            reverse = input_sequence
            reverse_complement = get_complement(reverse)
            print("Forward: " + forward)
            print("Forward Complement: " + forward_complement)
            print("Reverse: " + reverse)
            print("Reverse Complement: " + reverse_complement)
        case 'forward-comp':
            forward = get_complement(input_sequence)
            forward_complement = input_sequence
            reverse = get_reverse(forward)
            reverse_complement = get_complement(reverse)
            print("Forward: " + forward)
            print("Forward Complement: " + forward_complement)
            print("Reverse: " + reverse)
            print("Reverse Complement: " + reverse_complement)
        case 'reverse-comp':
            reverse_complement = input_sequence
            reverse = get_complement(reverse_complement)
            forward = get_reverse(reverse)
            forward_complement = get_complement(forward)
            print("Forward: " + forward)
            print("Forward Complement: " + forward_complement)
            print("Reverse: " + reverse)
            print("Reverse Complement: " + reverse_complement)
            
        case _:
            raise ValueError("That's weird. You should probably tell Morgan that you got this message.")

    print("Done!")

except ValueError as error:
    print(error)
    print("Program Terminated.")