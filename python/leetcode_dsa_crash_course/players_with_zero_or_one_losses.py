# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

# Return a list answer of size 2 where:

    # answer[0] is a list of all players that have not lost any matches.
    # answer[1] is a list of all players that have lost exactly one match.

# The values in the two lists should be returned in increasing order.
from collections import defaultdict

def players(matches):
    win_count = defaultdict(int)
    loss_count = defaultdict(int)
    
    for match in matches:
        winner_i = match[0]
        loser_i = match[1]
        win_count[winner_i] += 1
        loss_count[loser_i] += 1
    
    
    no_loss = []
    for winner in win_count:
        if loss_count[winner] == 0:
            no_loss.append(winner)
    
    one_loss = []
    for loser in loss_count:
        if loss_count[loser] == 1:
            one_loss.append(loser)
    
    print(sorted(no_loss), sorted(one_loss))
    return [sorted(no_loss), sorted(one_loss)]

players([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]])