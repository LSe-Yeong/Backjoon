def make_2D(game):
    game_2D = [['0' for i in range(3)] for j in range(3)]
    idx = 0
    for r in range(3):
        for c in range(3):
            game_2D[r][c] = game[idx]
            idx+=1
    return game_2D

def count_bingo(game_2D):
    o_count = 0
    x_count = 0
    for r in range(3):
        if 'O' not in game_2D[r] and '.' not in game_2D[r]:
            x_count+=1
        elif 'X' not in game_2D[r] and '.' not in game_2D[r]:
            o_count+=1

    for c in range(3):
            if game_2D[0][c] == game_2D[1][c] and game_2D[1][c] == game_2D[2][c] and game_2D[0][c] == 'O':
                o_count+=1
            elif game_2D[0][c] == game_2D[1][c] and game_2D[1][c] == game_2D[2][c] and game_2D[0][c] == 'X':  
                x_count+=1
    
    if game_2D[0][0] == game_2D[1][1] and game_2D[1][1] == game_2D[2][2] and game_2D[0][0] == 'O':
        o_count+=1
    elif game_2D[0][0] == game_2D[1][1] and game_2D[1][1] == game_2D[2][2] and game_2D[0][0] == 'X':  
        x_count+=1
    
    if game_2D[0][2] == game_2D[1][1] and game_2D[1][1] == game_2D[2][0] and game_2D[0][2] == 'O':
        o_count+=1
    elif game_2D[0][2] == game_2D[1][1] and game_2D[1][1] == game_2D[2][0] and game_2D[0][2] == 'X':  
        x_count+=1
    
    return o_count,x_count

while True:
    game = input()
    if game=="end":
        break
    else:
        game_2D = make_2D(game)
        if '.' in game:
            O_count,X_count = count_bingo(game_2D)
            if O_count==0 and X_count==0:
                print("invalid")
                continue
            if X_count!=0 and O_count!=0:
                print("invalid")
                continue
            if X_count > O_count:
                if game.count('X') != game.count('O')+1:
                    print("invalid")
                    continue
            if X_count < O_count:
                if game.count('X') != game.count('O'):
                    print("invalid")
                    continue
            print("valid")
        else:
            O_count,X_count = count_bingo(game_2D)
            if O_count==0 and X_count==0:
                if game.count('X') != game.count('O')+1:
                    print("invalid")
                    continue
            if X_count!=0 and O_count!=0:
                print("invalid")
                continue
            if X_count > O_count:
                if game.count('X') != game.count('O')+1:
                    print("invalid")
                    continue
            if X_count < O_count:
                if game.count('X') != game.count('O'):
                    print("invalid")
                    continue
            print("valid")

           
