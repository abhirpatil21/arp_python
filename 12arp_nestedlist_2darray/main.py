#nested list or 2D array
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

array2d = [row1, row2, row3]

def check_cell_selection(cell): {
    if ((int(cell[0]) >= 1) and (int(cell[0]) <= 3) and (int(cell[2]) >= 1) and (int(cell[2]) <=3 )) == true:
        return true
    else:
        return false
}

def row_selection(cell): {
    if (int(cell[0]) == 1)
        row = row1
    elif (int(cell[0]) == 2):
        row = row2
    else (int(cell[0]) == 3):
        row = row3
    return row
}

print("GAME : TIC TOC")
user1 = input("User1 name : ")
user2 = input("User2 name : ")
row = [" ", " ", " "]

cell = input(f"{user} input in format x,y : eg: 1,2 - row, colomn:")

check = true
user = user1
while check:
    input = check_cell_selection(cell)
    if input == true:
        row = row_selection(cell)
    else
        cell = input(f"Invalid input...{user} input in format x,y : eg: 1,2 - row, colomn:")

    i
        else:


if user_selection == 1):
    user = user1
else:
    user = user2


#print(f"cell type : {type(cell)}, Cell content : {cell}")
#print(f" cell(0) : {cell[0]}, cell(1) : {cell[1]}, cell(2) : {cell[2]}")
#check col and row
if ((int(cell[0]) >= 1) and (int(cell[0]) <= 3) and (int(cell[2]) >= 1) and (int(cell[2]) <=3 )) == true
    if ( int(cell[0]) == 1 ):
        row = row1
    elif ( int(cell[0]) == 2 ):
        row = row2
    else ( int(cell[0]) == 3):
        row = row3
    colomn = int(cell[2])
    if (row[colomn] != " ")
        cell = input(f"Invalid input...{user} input in format x,y : eg: 1,2 - row, colomn:")


    user_selection = 2
else:
    print("Invalid entry")
    user_selection = 1

print(f"2D Array :\n{row1}\n{row2}\n{row3}")
user = user2

if (row[colomn] != " ")
        cell = input(f"Invalid input...{user} input in format x,y : eg: 1,2 - row, colomn:")