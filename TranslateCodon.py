#This script takes in your DNA string and translates the codons into amino
#acid codes.

def validate_sequence (sequence):
    #TODO: length is divisible by 3
    #TODO: only A U G C is present
    return None

def split_sequence (sequence):
    #TODO: separate the sequence into groups of 3.
    #TODO: return an array of codons.
    return None

def translate_codon (codon):
    #TODO: Match the three letters to the appropriate amino acid
    #TODO: return amino single character
    return None

def sequence_to_codon (sequence):
    sequence.upper()
    validate_sequence(sequence)
    codons = split_sequence(sequence)
    amino_acids = []
    for codon in codons:
        amino_acid = translate_codon(codon)
        amino_acids.append(amino_acid)
    return amino_acids

#Test main
test_sequence = "AUGAAGACGGUA"
translated_acid = sequence_to_codon(test_sequence)
print(test_sequence)
print(translated_acid)
if translated_acid == "MKTV":
    print("Success")
else:
    print("Failed")