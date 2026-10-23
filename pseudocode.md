
Psudocode session output
1- display board:
OUTPUT board view
OUTPUT choose a symbol

2- choose player:
REPEAT
    INPUT choice 
    IF choice is not X or O Invalid Input
UNTIL choice is "X" or "O"
STORE choice in current_player

3- player choose move
REPEAT
    OUTPUT Choose a square 
    INPUT player move
    IF move is not a number between 1 and 9 THEN
        OUTPUT "Please enter a number from 1 to 9"
    ELSE IF board square move is not empty THEN
        OUTPUT "That square is taken, choose another"
UNTIL move is valid and the square is empty

4- check for winner: winner lines (8)
FOR each line in winning lines
    IF all three squares in line equal current_player THEN
        RETURN True
    RETURN False

5- check draw:
IF no square on the board is empty THEN
    RETURN True
RETURN False

6- switch player:
IF current_player is "X" THEN
    current_player = "O"
ELSE
    current_player = "X"

7- main:
game_going = TRUE

REPEAT
SET board empty
OUTPUT BOARD
OUTPUT EXPLAIN RULES
SET current_player = chose player
    WHILE game_going
        move = get_move
        PLACE current_player on board square move
        OUTPUT board
        IF check_winner is True
            OUTPUT winner
            game_going = Flase
            Stop loop
        IF check_draw is True
            OUTPUT draw
            game_going = Flase
            stop loop
        Switch player
    INPUT start an new game or quit 
        start -> game goint to TRUE
        or FALSE
until game_going is False
