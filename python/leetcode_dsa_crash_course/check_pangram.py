def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    
    for c in sentence:
        if c in alphabet:
            alphabet.remove(c)
        if len(alphabet) <= 0:
            print("True")
            return True
    
    print("False")
    return False

is_pangram('thequickbrownfoxjumpsoverthelazydog')
is_pangram('leetcode')