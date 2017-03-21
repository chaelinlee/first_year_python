def creat_init_board():
    return [[0,15,14,13],
            [12,11,10,9],
            [8,7,6,5],
            [4,3,2,1]]

def set_goal_board():
    return [[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,0]]

def print_board(board):
    for row in board:   #행이 하나씩 보드변수에 저장이된다.
        for num in row: #row의 수가 하나씩 변수에 저장이 된다. 
            if num== 0: #0이라는 숫자대신에 빈칸이 나오고 줄을 맞춰어야하니깐 빈칸을 한개 더 만든다.
                print("  ",end=' ')
            elif 10<=num<=15: #두자리 수에서는 숫자는 나오고 줄맞춰기위해 한칸 띈다.
                print(num,end=' ')
            else:
                print(str(num).rjust(2),end=' ')
        print() #내부에서 한 행이 끝나면 다음줄로 넘어가야하기 때문                    
        
def find_position(num,board): #보드안에 있는 수의 행과열을 튜플로 내준다. 
    for x in range(0,4):
        for y in range(0,4):
            if board[x][y] == num:
                return (x,y)
            
def move(pos,empty,board): #이해잘 안가니깐 잘 보기!! pos= 이동대상좌표,empty=빈칸좌표
    
    (x,y) = pos # 이동할 수 있는지의 판단은 빈칸과 그 입력숫자가 이웃해 있으면 된다. 
    if empty == (x-1,y) or empty == (x+1,y) or \
       empty == (x,y-1) or empty == (x,y+1):
        board[empty[0]][empty[[1]] == board[x][y] #빈칸을 지정한 좌표로 이동한다.
        board[x][y] == 0
        return (pos,board)                
    else:
        print("Can't move! Try again.")
    return (empty,board)
         
def get_number():
    number=input ('Type the number you want to move (Type 0 to quit): ')
    while not (number.isdigit() and 0 <= int(number) <= 15):
           number=input ('Type the number you want to move (Type 0 to quit): ')        
    return int(number)


def sliding_puzzle():
    board = creat_init_board()
    goal = set_goal_board()
    empty = (0,0)
    while True :
        print_board(board)
        if board == goal:
            print("Congratulations!")
            break
        num = get_number()
        if num == 0:
            break
        pos = find_position(num,board)
        (empty,board) = move(pos,empty,board)
    print("please come again.")
sliding_puzzle()
     
