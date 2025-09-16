#
# Build words in dictionary (like Linux /usr/share/dict/words) for use with Wordle
#
import re

# Enter text dictionary
path_to_dict = input("Text dictionary of words to build from [/usr/share/dict/words]: ")
if path_to_dict == "":
    path_to_dict = '/usr/share/dict/words'

# Enter output file name
path_to_new_dict = input("Output file name [words.txt]: ")
if path_to_new_dict == "":
    path_to_new_dict = 'words.txt'

# Read all lines into a list
print("Getting words from", path_to_dict)
words = []
with open(path_to_dict, 'r', encoding='utf-8') as file:
    for line in file.readlines():
        words.append(line)

# Words we never want to show up in the dictionary:
# ***Trigger Warning***  The following words may be offensive or triggering
sensitive_words = ["fucks", "shits", "cunts", "spiks", "spics", "spick", "kikes", "chink", "gooks", "whore", "sluts",
                   "negro", "bitch", "vulva", "penis", "slave", "narcs", "narks", "pimps", "rapes", "fetus", "porno"]
# ... and probably a lot more I can't think of

# Only five English letters and a LF (how to remove plurals?)
valid = re.compile(r"^[A-Za-z]{5}\n$")
new_words = []
for word in words:
    if valid.match(word) and word.rstrip() not in sensitive_words:
        new_words.append(word.lower())

print("Original size:", len(words))
print("New size:", len(new_words))
print("Writing new file...")

# Write back to words file
with open(path_to_new_dict, 'w', encoding='utf-8') as file:
    file.writelines(new_words)

print("fin")
