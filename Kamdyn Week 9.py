#Name: Section8.17problem5
#Purpose: Strings 
#Author: KamdynHagerty
#Created: 3/30/26



song_lyrics = """
Do you ever feel like a plastic bag
Drifting through the wind, wanting to start again?
Do you ever feel, feel so paper-thin
Like a house of cards, one blow from caving in? """


words = song_lyrics.split()
total_words = len(words)
print(total_words)
number_of_e = 0
total_chars = 0
for this_char in song_lyrics:
            total_chars = total_chars + 1
            if this_char == "e":
                number_of_e = number_of_e + 1
percent_with_e = (number_of_e / total_chars) * 100
print(f"Your text contains {total_chars} alphabetic characters of which {number_of_e} ({percent_with_e}%) are 'e'.")


