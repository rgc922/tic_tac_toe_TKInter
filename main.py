import tkinter as tk

from random import randint

turno = 0

def announce():
    global turno

    if turno % 2 != 0:
        canvas.itemconfig(my_text, text='Ganaste', fill='Red')
    else:
        canvas.itemconfig(my_text, text='Perdiste', fill='Green')



def pc_move():
    global board
    global turno

    row_pc = randint(0, 2)
    column_pc = randint(0, 2)

    if board[row_pc][column_pc]['text'] == '':
        turno += 1
        set_board(board[row_pc][column_pc], 'X')
    else:
        pc_move()
    



def check_winner(btn):
    global board
    global turno

    for letters in ('X', 'O'):
        for a in range(3):
            if board[a][0]['text'] == board[a][1]['text'] == board[a][2]['text'] == letters or \
               board[0][a]['text'] == board[1][a]['text'] == board[2][a]['text'] == letters or \
               board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] == letters or \
               board[2][0]['text'] == board[1][1]['text'] == board[0][2]['text'] == letters:

                return True
            
    if turno % 2 != 0:
        pc_move()



def set_board(btn, letter):
    #print('Set board')

    if letter == 'X':
        btn['fg'] = 'red'
    else:
        btn['fg'] = 'green'
    btn['text'] = letter


    if check_winner(btn) == True:
        announce()




def clicked(event):
    global turno

    btn = event.widget

    if btn['text'] == '':
        turno += 1
        set_board(btn, 'O')


    #print(event)



window = tk.Tk()
window.title("My Tic Tac Toe GAME")

board = [["" for i in range(3)] for j in range (3)]

for rows in range(3):
    for columns in range(3):
        new_btn = tk.Button(window, width=2, height=1, 
                            font=("Arial", "80", "bold"), bg="gray")
        new_btn.bind("<Button-1>", clicked)
        new_btn.grid(row=rows, column=columns)
        board[rows][columns] = new_btn


canvas = tk.Canvas(window, width=100, height=30, bg='white')
text_start = 'Playing'
my_text = canvas.create_text(50, 15, text=text_start,
                             font=('Arial', '15', 'bold'),
                             justify=tk.CENTER,
                             fill='yellow')
canvas.grid(row=3, column=1)

### primer movimiento en posición central al PC
set_board(board[1][1], "X")

window.mainloop()
