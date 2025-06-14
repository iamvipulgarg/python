board = {1:'-',2:'-',3:'-',4:'-',5:'-',6:'-',7:'-',8:'-',9:'-'}

p1=input('Enter Player 1 Name :');
p2=input('Enter Player 2 Name :');
counter = 0;
flag = 0;

def print_baord():
    print(board[1],board[2],board[3])
    print(board[4],board[5],board[6])
    print(board[7],board[8],board[9])
 
def winner():
    if board[1] != '-' and board[1] == board[2] == board[3]:
        return 1
    if board[4] != '-' and board[4] == board[5] == board[6]:
        return 1
    if board[7] != '-' and board[7] == board[8] == board[9]:
        return 1
    
    if board[1] != '-' and board[1] == board[4] == board[7]:
        return 1
    if board[2] != '-' and board[2] == board[5] == board[8]:
        return 1
    if board[3] != '-' and board[3] == board[6] == board[9]:
        return 1
    
    if board[1] != '-' and board[1] == board[5] == board[9]:
        return 1
    if board[3] != '-' and board[3] == board[5] == board[7]:
        return 1
    return 0
    
while(counter < 9):
    if flag == 0:
        pos = int(input(p1 + ' Turn : '))
        if board[pos] != '-':
            continue;
        board[pos] = 'X'
        
        flag = 1
    else:
        pos = int(input(p2 + ' Turn : '))
        if board[pos] != '-':
            continue;
        board[pos] = '0'
        
        flag = 0
    print_baord()
    win = winner()
    if win == 1:
        if flag == 1:
            print("Winner " + p1)
        else:
            print("Winner " + p2)
        break;
    counter +=1
    if counter == 9:
        print('Game Draw')