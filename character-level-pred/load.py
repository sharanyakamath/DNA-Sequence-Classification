import random

def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text
 
# save tokens to file, one dialog per line
def save_doc(lines, filename):
	data = '\n'.join(lines)
	file = open(filename, 'w')
	file.write(data)
	file.close()
 
# load text

#repeating sequence
raw_text = "AGCTTGAGGC"*300

#random sequence
# dna = "ACGT"
# raw_text = ''.join(random.choice(dna) for i in range(3000))

#ecoli sequence
# raw_text = load_doc("ecoli.txt")

print(raw_text)
 
# clean
tokens = raw_text.split()
raw_text = ' '.join(tokens)
 
# organize into sequences of characters
length = 50
sequences = list()
for i in range(length, len(raw_text)):
	# select sequence of tokens
	seq = raw_text[i-length:i+1]
	# store
	sequences.append(seq)
print('Total Sequences: %d' % len(sequences))
 
# save sequences to file
out_filename = 'char_sequences.txt'
save_doc(sequences, out_filename)
