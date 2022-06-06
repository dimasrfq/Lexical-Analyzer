print("TUGAS BESAR BAHASA AUTOMATA | KELOMPOK X | IF4403")
print("========LEXICAL ANALYZER=========")

import string

#input example
#sentence = 'brother wear hat'
#input_string = sentence.lower()+'#'


def lexical(sentence):

    #initialization
    alphabet_list = list(string.ascii_lowercase)
    state_list = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 
              'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33']

    transition_table = {}

    for state in state_list:
        for alphabet in alphabet_list:
            transition_table[(state, alphabet)] = "error"
        transition_table[(state, "#")] = "error"
        transition_table[(state, " ")] = "error"

    #start state
    transition_table["q0", " "] = "q0"

    #finish state
    transition_table[("q33", "#")] = "accept"
    transition_table[("q33", " ")] = "q34"

    transition_table[("q34", "#")] = "accept"
    transition_table[("q34", " ")] = "q34"

    #string weruh
    transition_table[("q0", "w")] = "q1"
    transition_table[("q1", "e")] = "q2"
    transition_table[("q2", "r")] = "q3"
    transition_table[("q3", "u")] = "q4"
    transition_table[("q4", "h")] = "q33"
    transition_table[("q34", "w")] = "q1"

    #string aku
    transition_table[("q0", "a")] = "q5"
    transition_table[("q5", "k")] = "q6"
    transition_table[("q6", "u")] = "q33"
    transition_table[("q34", "a")] = "q5"

    #string buku
    transition_table[("q0", "b")] = "q7"
    transition_table[("q7", "u")] = "q5"
    transition_table[("q34", "b")] = "q7"

    #string tas
    transition_table[("q0", "t")] = "q8"
    transition_table[("q8", "a")] = "q9"
    transition_table[("q9", "s")] = "q33"
    transition_table[("q34", "t")] = "q8"

    #string tali
    transition_table[("q9", "l")] = "q10"
    transition_table[("q10", "i")] = "q33"

    #string goleki
    transition_table[("q0", "g")] = "q11"
    transition_table[("q11", "o")] = "q12"
    transition_table[("q12", "l")] = "q13"
    transition_table[("q13", "e")] = "q14"
    transition_table[("q14", "k")] = "q10"
    transition_table[("q34", "g")] = "q11"

    #string sandal
    transition_table[("q0", "s")] = "q15"
    transition_table[("q15", "a")] = "q16"
    transition_table[("q16", "n")] = "q17"
    transition_table[("q17", "d")] = "q18"
    transition_table[("q18", "a")] = "q19"
    transition_table[("q19", "l")] = "q33"
    transition_table[("q34", "s")] = "q15"

    #string dheweke
    transition_table[("q0", "d")] = "q20"
    transition_table[("q20", "h")] = "q21"
    transition_table[("q21", "e")] = "q22"
    transition_table[("q22", "w")] = "q23"
    transition_table[("q23", "e")] = "q24"
    transition_table[("q24", "k")] = "q25"
    transition_table[("q25", "e")] = "q33"
    transition_table[("q34", "d")] = "q20"

    #string kowe
    transition_table[("q0", "k")] = "q26"
    transition_table[("q26", "o")] = "q27"
    transition_table[("q27", "w")] = "q25"
    transition_table[("q34", "k")] = "q26"

    #string ndemok
    transition_table[("q0", "n")] = "q28"
    transition_table[("q28", "d")] = "q29"
    transition_table[("q29", "e")] = "q30"
    transition_table[("q30", "m")] = "q31"
    transition_table[("q31", "o")] = "q32"
    transition_table[("q32", "k")] = "q33"
    transition_table[("q34", "n")] = "q28"

    #lexical analysis
    idx_char = 0
    state = 'q0'
    current_token = ''
    while state != 'accept':
        current_char = input_string[idx_char]
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state=='q33': 
            print('current token: ', current_token, ', valid')
            current_token = ''
        if state =="error":
            print("error")
            break
        idx_char = idx_char + 1

    #conclusion
    if state == "accept":
        print('semua token diinput: ', sentence, ', valid')
    
    return lexical

print("terminal: aku, kowe, dheweke, weruh, ndemok, goleki, buku, sandal, tas, tali \n ")
sentence = input("input here: ")
input_string = sentence.lower()+'#'
lexical(sentence)