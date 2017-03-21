# Sudoku 4x4

import random
def create_board():
    seed =[1,2,3,4]
    random.shuffle(seed)
    n1= seed[0]
    n2= seed[1]
    n3= seed[2]
    n4= seed[3]
    return [[n1,n2,n3,n4],
            [n3,n4,n1,n2],
            [n2,n1,n4,n3],
            [n4,n3,n2,n1]]

def shuffle_ribbons(board):
    top=board[:2]
    bottom=board[2:]
    random.shuffle(top)
    random.shuffle(bottom)
    return top + bottom #이해는가는데 처음부터 이렇게 코딩하기는 힘들듯 

def transpose(board):
    transposed = []
    for i in range(len(board)):
        transposed.append([])
    for j in range(0,4):
        for k in range(0,4):
            transposed[k].append(board[j][k])# transposed[k]라는게 빈 리스트 하나하나에 
    return transposed                        # board[i][j]를 넣는다는 소리이다. 
        
        
def create_solution_board():
    board= create_board()
    board= shuffle_ribbons(board)
    board= transpose(board)
    board= shuffle_ribbons(board)
    board= transpose(board)
    return board

def get_level():
    level = input("난이도(상,중,하)중에서 하나 선택하여 입력: ")
    while not level in ('상','중','하'):
        level = input("난이도(상,중,하)중에서 하나 선택하여 입력: ")
    if level ==  '하':
        return 6
    elif level== '중':
        return 8
    else:
        return 10 #이부분은 완벽히 이해가 간다. 
    
def make_holes(board,no_of_holes):
    holeset = set()
    while no_of_holes >0:
        i = random.randint(0,3)
        j = random.randint(0,3)
        if not board[i][j] == 0:
            board[i][j] = 0
            holeset.add((i,j))
            no_of_holes -= 1
        else:
            continue
    return (board,holeset) 
        
def copy_board(board):
    board_clone= []
    for row in board:
        row_clone= row[:]
        board_clone.append(row_clone)
    return board_clone    
           
def show_board(board):
    print("S | 1 2 3 4 ")
    print("- + - - - - ")
    print("1 |",end='')
    for j in range(0,4):
        if board[0][j]==0:
            print("",".",end = "")
        else:
            print('',str(board[0][j]),end="")
    print()
    print("2 |",end='')
    for j in range(0,4):
        if board[1][j]==0:
            print('',".",end = '')
        else:
            print('',str(board[1][j]),end="")
    print()
    print("3 |",end='')
    for j in range(0,4):
        if board[2][j]==0:
            print("",".",end = "")
        else:
            print('',str(board[2][j]),end="")
    print()
    print("4 |",end='')
    for j in range(0,4):
        if board[3][j]==0:
            print("",".",end = "")
        else:
            print('',str(board[3][j]),end="")
    print()
    
 

def get_integer(message,mininum,maxinum):
    n=input(message)
    while not (n.isdigit() and mininum <=int(n)<= maxinum):
           n=input(message)
    return int(n)


def sudokmini():
    solution = create_solution_board()
    no_of_holes = get_level()
    puzzle = copy_board(solution)
    (puzzle,holeset) = make_holes(puzzle,no_of_holes)
    show_board(puzzle)
    while no_of_holes >0:
        i = get_integer("가로줄번호(1~4): ",1,4)-1
        j = get_integer("세로줄번호(1~4): ",1,4)-1
        if (i,j) not in holeset:
            print("빈칸이 아닙니다.")
            continue
        n= get_integer("숫자(1~4): ",1,4)
        sol = solution[i][j]
        if n == sol:
            puzzle[i][j] = sol
            show_board(puzzle)
            holeset.remove((i,j))
            no_of_holes -= 1
        else:
             print(n,"가 아닙니다. 다시 해보세요.")
    print("잘 하셨습니다. 또 들려주세요.")       
