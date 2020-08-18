##From PySpellChecker
from spellchecker import SpellChecker

# simple text spelling error correction
spell = SpellChecker()
def correct_sentence(line):
    lines = line.strip().split(' ')
    new_line = ""
    similar_word = {}
    for l in lines:
        new_line += spell.correction(l) + " "
    return new_line
