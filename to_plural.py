#!/usr/bin/env python

## https://codeshare.io/21OXj7

#pip install open-tamil
import tamil

debug = False

def is_nedil(letter):
    return (sum(tamil.utf8.calculate_maththirai(letter)) > 1)

def is_kuril(letter):
    return not is_nedil(letter)


def to_plural(word):
    ## exceptions to the 4 rules
    ## TODO: anything else?
    pl_exceptions = {
            'நான்'  : 'நாங்கள்',
            'நீ'   : 'நீங்கள்',
            'அவன்' : 'அவர்கள்',
            'அவள்' : 'அவர்கள்',
            'அது'  : 'அவை '
        }
            
    ## pseudo code
    '''
    if word.endswith('ம்'):
        ## remove last letter ‘ம்’ and add ‘ங்கள்’
        ## மரம் -> மரங்கள், குடம் -> குடங்கள்
        plural = word[:-1] + 'ங்கள்'
    elif (len(word) == 2) and (word[0] is குறில்) and word.endswith('ல்'):
        ## remove last letter ‘ல் ’ and add ‘ற்கள்
        ## கல் -> கற்கள்,  சொல் -> சொற்கள்
        plural = word[:-1] + 'ற்கள்'
    elif word[-1] is நெடில்:
        ## add ‘க்கள்’
        ## பூ -> பூக்கள், பூங்கா -> பூங்காக்கள்
        plural = word + 'க்கள்'
    else:
        ## add ‘கள்’
        ## பாடல் -> பாடல்கள்,  வண்டி -> வண்டிகள்
        plural = word + 'கள்'
    '''

    ## working code using open-tamil utilities

    if word in pl_exceptions.keys():
        return pl_exceptions[word]

    ## use get_letters() method to correctly count the number of tamil letters
    ta_letters = tamil.utf8.get_letters(word)
    
    if debug: print('singular word: {}, word_len: {}, letters: {}, letters_len: {}'.format(word, len(word), ta_letters, len(ta_letters)))
    
    if word.endswith('ம்'):
        if debug: print('word ends with ம்')
        return ''.join(ta_letters[:-1]) + 'ங்கள்'

    if (len(ta_letters) == 2) and is_kuril(ta_letters[0]) and word.endswith('ல்'):
        if debug: print('2-letter word ends with ல்')
        return ''.join(ta_letters[:-1]) + 'ற்கள்'

    if is_nedil(ta_letters[-1]):
        if debug: print('word ends with நெடில்')
        return word + 'க்கள்'

    ## default
    return word + 'கள்'
        


if __name__ == '__main__':
    word = input('Enter a singular tamil word: ')
    print('{}  =>  {}'.format(word, to_plural(word)))

