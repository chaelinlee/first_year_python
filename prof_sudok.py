#Sudok 4x4

import random
def create_board():  #완벽히 이해감 
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
    return top + bottom 

def transpose(board): #가로와 세로를 바꾸어주는 함수 
    transposed = []
    for _ in range(len(board)): #변수가 밑에서 필요하지 않으니까 빈칸으로 두어도 괜춘 
        transposed.append([])  #여기까지는 transposed=[[],[],[],[]]가 됬다는 의미 
        
    for row in board: #가로를 의미한다. 
        i = 0
        for entry in row: #세로를 의미한다.
            transposed[i].append(entry) # transposed의 빈 리스트에 보드의 세로를 붙인다.
            i +=1 #하나의 세로가 완성되면 다음 빈 리스트로 갈수 있게 만든 장치이다. 
    return transposed  

def create_solution_board():
    board= create_board()
    board= shuffle_ribbons(board)#가로줄을 섞는다. 
    board= transpose(board) #가로와 세로를 바꾸어준다.
    board= shuffle_ribbons(board) #가로를 섞는다. 즉 세로를 섞는 의미가 된다.  
    board= transpose(board) # 가로와 세로를 다시 바꾸어준다. 
    return board

def get_level():
    level = input("난이도(상,중,하)중에서 하나 선택하여 입력: ")
    while level not in {'상','중','하'}:
        level = input("난이도(상,중,하)중에서 하나 선택하여 입력: ")
    if level ==  '하':
        return 6
    elif level== '중':
        return 8
    else:
        return 10


def make_holes(board,no_of_holes): #퍼즐보드는 정답보드와 똑같은 보드를 하나 복제하고, 난이도

    holeset = set() #공직합이다.      #에 따라 무작위로 빈칸을 적절하게 만들어 제적한다. 
    while no_of_holes > 0: #0이 되기 전까지 계속 빈칸을 만든다.
        i= random.randint(0,3)
        j= random.randint(0,3)
        if board[i][j] !=0: #똑같은 것이 중복 될 수도 있으니깐 
            board[i][j] =0
            holeset.add((i,j))
            no_of_holes -= 1
            
    return (board,holeset) #holeset에는 빈칸의 좌표가 

def copy_board(board):
    board_clone= []
    for row in board:
        row_clone= row[:]
        board_clone.append(row_clone)
    return board_clone 

def show_board(board):
    print()
    print('S','|','1','2','3','4')
    print('-','+','-','-','-','-')
    i=1
    for row in board:
        print(i,end=' ')
        print('|',end=' ')
        for entry in row:
            if entry ==0:
                print('.',end=' ')
            else:
                print(entry,end=' ')
        print()
        i +=1
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
            





    





    
