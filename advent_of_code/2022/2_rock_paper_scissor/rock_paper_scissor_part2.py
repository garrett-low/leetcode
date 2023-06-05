# A Y
def rps():
    shape_score_dict = { "X" : 1, # rock
                    "Y" : 2, # paper
                    "Z" : 3 } # scissor
    play_dict = { "A X" : "Z", # rock - scissor
                "A Y" : "X", # rock - rock
                "A Z" : "Y", # rock - paper
                "B X" : "X", # paper - rock
                "B Y" : "Y", # paper - paper
                "B Z" : "Z", # paper - scissor
                "C X" : "Y", # scissor - paper
                "C Y" : "Z", # scissor - scissor
                "C Z" : "X" } # scissor - rock
    outcome_dict = { "X" : 0, # lose
                     "Y" : 3, # draw
                     "Z" : 6 } # win
    score = 0
    with open('input.txt', 'rt', encoding='utf-8') as file:
        for line in file:
            vals = line.split(' ')
#             other_play = vals[0].strip()
            my_outcome = vals[1].strip()
            
            my_play = play_dict[line.strip()]
            score += shape_score_dict[my_play] + outcome_dict[my_outcome]
    
    print(score)
    
rps()
