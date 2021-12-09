#read a position from the user.
position_user = input('Enter a position of the chess board: ').lower()

# determine if the column begins with a black or a white square.
# assume that a valid position will always be entered. 

if len(position_user) == 2 and position_user[1].isdigit():

    column = str(position_user[0])
    row = int(position_user[1])

    if column == 'a' or column == 'c'or column == 'e' or column == 'g' and 0 < row <= 8:

        # use modular arithmetic to report the color in that row
        if row % 2 == 0:
            print('The square is white.')
        elif row % 2 != 0:
            print('The square is black.')   

    elif column == 'b' or column == 'd' or column == 'f' or column == 'h' and 0 < row <= 8:
        if row % 2 == 0:
            print('The square is black.')
        elif row % 2 != 0:
            print('The square is white.')




