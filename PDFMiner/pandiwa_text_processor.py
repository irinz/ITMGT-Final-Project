# Generates a new, processed text file based on the unprocessed one
import re

pandiwa_text_file = open("pandiwa_text_unprocessed.txt", "r").read().splitlines()
characters_to_remove = ['', ' ', 'samutsamot.com ', '© 2014 Pia Noche ', 'Mga Pandiwa sa Iba’t ibang Aspekto o Panahunan ', 'Pangnagdaan  Pangkasalukuyan  Panghinaharap ', 'Salitang-ugat ', 'Pawatas ', 'Katatapos ']

for character in characters_to_remove:
    while character in pandiwa_text_file:
        pandiwa_text_file.remove(character)
for i in range(16):
    pandiwa_text_file.remove(f'Page {i+1} ')

for i in range(len(pandiwa_text_file)):
    pandiwa_text_file[i] = pandiwa_text_file[i].replace(" ", "")
    pandiwa_text_file[i] = re.sub(r'\([^)]*\)', '', pandiwa_text_file[i])  # https://stackoverflow.com/questions/640001/how-can-i-remove-text-within-parentheses-with-a-regex

print(pandiwa_text_file)

processed_pandiwa_text_file = pandiwa_text_file

processedfile = open("pandiwa_text_processed.txt", "w") # The final file is manually processed to account for some leftover extra characters from PDF processing

for pandiwa in processed_pandiwa_text_file:
    processedfile.write(f"{pandiwa}\n")

processedfile.close()