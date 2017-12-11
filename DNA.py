#  File: DNA.py

#  Description: Program determines whether two sequences have any identical substrings. User inputs the data file 
#  and output is the identical substrings for every two strings 

#  Student Name: Brian Tsai

#  Student UT EID: byt76

#  Course Name: CS 303E

#  Unique Number: 51850 

#  Date Created: 3/10/17

#  Date Last Modified: 3/10/17

# check_sequence returns a list with all the matching substrings
def check_sequence(sequence_one, sequence_two):
	pair_list = []

	# Rotate sequence_one len(sequence_one)
	for shift_one in range(0, len(sequence_one)): 
		
		# Rotate sequence_two len(sequence_one) * len(sequence_two) 
		for shift_two in range(0, len(sequence_two)):
			
			# Iterate over the substrings in sequence_two
			for length in range(1, len(sequence_two)):

				# Append the string to pair_list if the substring matches the beginning of sequence_one
				if (sequence_one.startswith(sequence_two[0: length+1])):
					pair_list.append(sequence_two[0: length+1])			
			
			# Rotate left the string in sequence_two 
			temp = sequence_two[0]
			sequence_two = sequence_two[1:]
			sequence_two += temp

		# Rotate left the string in sequence_one 	
		temp = sequence_one[0]
		sequence_one = sequence_one[1:]
		sequence_one += temp 

	# Return list of all matching substrings	
	return pair_list


def main():

	# Open the file and store buffer area to DNA 
	DNA = open("dna.txt", "r")

	# Number_of_pairs holds the number of comparisons
	number_of_pairs = int(DNA.readline())

	# Pair_number holds the numerical index
	pair_number = 1
	print("Longest Common Sequence")
	print()

	# Iterate over the entire file
	for sequence in range(0, number_of_pairs):

		# strand_one and strand_two holds the temporary lines to compare 
		strand_one = ((DNA.readline()).strip()).upper()
		strand_two = ((DNA.readline()).strip()).upper()
		
		# pair_list holds the list with all matching substrings for each comparison
		pair_list = []
		
		# pair_list holds the result list from check_sequence
		if (len(strand_one)>=len(strand_two)):
			pair_list = check_sequence(strand_one, strand_two)

		else:
			pair_list = check_sequence(strand_two, strand_one)
		

		# Format the table to be displayed	
		print ("Pair", pair_number, end=": ")
		
		# If pair_list is not empty, print the table
		if (pair_list):
			
			# Remove the duplicate elements
			pair_list = list(set(pair_list))
			next_line = False

			# Find the string with the max_length
			max_length = max(len(strand) for strand in pair_list)
			
			# Print all sequences that have the max length
			for sequence in pair_list:
				if (not next_line):
					if (max_length == len(sequence)):
						print(format(sequence, "s"))
						next_line = True


				else:
					if (max_length == len(sequence)):
						print(format(sequence, ">12s"))
			print()			
		
		# If pair_list is empty, print "No Common Sequence Found"
		else:
			print ("No Common Sequence Found")	
			print()					
		pair_number += 1

	DNA.close()
		
main()		
