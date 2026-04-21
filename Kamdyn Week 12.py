
#Name: Section20.8problem3
#Purpose:  Dictionaries
#Author: KamdynHagerty
#Created: 4/17/26




import string

def count_words(input_file, output_file):
    word_counts = {}

    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            
            line = line.lower()
            
            
            line = line.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
            
            
            words = line.split()
            
            for word in words:
                word_counts[word] = word_counts.get(word, 0) + 1

    
    sorted_words = sorted(word_counts.items())


    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(f"{'Word':<18}Count\n")
        file.write("=" * 23 + "\n")
        
        for word, count in sorted_words:
            file.write(f"{word:<18}{count}\n")


if __name__ == "__main__":
    input_filename = "alice.txt"
    output_filename = "alice_words.txt"
    
    count_words(input_filename, output_filename)

            
