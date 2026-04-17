#Name: Section13.11problem1
#Purpose:  Files
#Author: KamdynHagerty
#Created: 4/12/26



def reverse_file_lines(input_file, output_file):
    
    with open(input_file, 'r') as infile:
        lines = infile.readlines()
    
    
    reversed_lines = lines[::-1]
    
    
    with open(output_file, 'w') as outfile:
        outfile.writelines(reversed_lines)
