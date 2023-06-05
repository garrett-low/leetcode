# A Y
def rps():
    shape_score_dict = { "X" : 1, # rock
                    "Y" : 2, # paper
                    "Z" : 3 } # scissor
    outcome_dict = { "A X" : 3, # rock - rock
                "A Y" : 6, # rock - paper
                "A Z" : 0, # rock - scissor
                "B X" : 0, # paper - rock
                "B Y" : 3, # paper - paper
                "B Z" : 6, # paper - scissor
                "C X" : 6, # scissor - rock
                "C Y" : 0, # scissor - paper
                "C Z" : 3 } # scissor - scissor
    score = 0
    with open('input.txt', 'rt', encoding='utf-8') as file:
        for line in file:
            vals = line.split(' ')
            other_play = vals[0].strip()
            my_play = vals[1].strip()
            
            score += shape_score_dict[my_play] + outcome_dict[line.strip()]
    
    print(score)
    
rps()