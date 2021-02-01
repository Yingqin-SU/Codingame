# First solution

def line_verificateur():
    global check_win
    check_win = []
    for i in range(9):
        m = [1,2,3,4,5,6,7,8,9]
        line = [int(i) for i in input().split()]
        for j in line:
            try:
                m.remove(j)
            except:
                return False
        if m == []:
            check_win += [line]
        
def colonne_verificateur():
    if len(check_win) < 9:
        return False
    else:
        for i in range(len(check_win)):
            m = [1,2,3,4,5,6,7,8,9]
            for j in range(len(check_win)):
                try:
                    m.remove(check_win[j][i])
                except:
                    return False


def zone_verificateur():
    global check_win
    for i in range(9):
        if i%3==0:
            m = [1,2,3,4,5,6,7,8,9]
        for j in range(3):
            try:
                m.remove(check_win[i][j])
            except:
                return False
    
    for i in range(9):
        if i%3==0:
            m = [1,2,3,4,5,6,7,8,9]
        for j in range(3,6):
            try:
                m.remove(check_win[i][j])
            except:
                return False

    for i in range(9):
        if i%3==0:
            m = [1,2,3,4,5,6,7,8,9]
        for j in range(6,9):
            try:
                m.remove(check_win[i][j])
            except:
                return False
         
print('true'
if line_verificateur() == None
and colonne_verificateur() == None
and zone_verificateur() == None
else 'false')