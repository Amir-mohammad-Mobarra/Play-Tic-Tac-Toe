import tkinter as tk
from tkinter import messagebox


class TicTacToeGUI:
    def __init__(self, board_size):
        self.buttons = None
        self.board_size = board_size
        self.window = tk.Tk()
        self.window.title('Tic Tac Toe')
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'X'
        self.creat_board_buttons()

    def creat_board_buttons(self):
        self.buttons = [[tk.Button(self.window, text=' ', font=('Arial', 20), width=3, height=1,
                                   command=lambda row=row, col=col: self.make_move(row, col)) for col in
                         range(self.board_size)]
                        for row in range(self.board_size)]
        for row in range(self.board_size):
            for col in range(self.board_size):
                self.buttons[row][col].grid(row=row, column=col)

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_win(self.current_player):
                messagebox.showinfo(title='Tic Tac Toe', message=f'player {self.current_player} wins!')
                self.reset_game()
            elif self.is_full():
                messagebox.showinfo(title='Tic Tac Toe', message='It\'s a tie!')
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            messagebox.showerror(title='Invalid Move', message='cell already taken. Try again!')

    def check_win(self, player):
        for i in range(self.board_size):
            if all(self.board[i][j] == player for j in range(self.board_size)) or all(self.board[j][i] == player
                                                                                      for j in range(self.board_size)):
                return True
        return all(self.board[i][i] == player for i in range(self.board_size)) or all(
            self.board[i][self.board_size - 1 - i] == player for i in range(self.board_size))

    def is_full(self):
        return all(all(cell != ' ' for cell in row) for row in self.board)

    def reset_game(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                self.board[row][col] = ' '
                self.buttons[row][col].config(text=' ')
        self.current_player = 'X'

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    tk_board_size = tk.Tk()
    tk_board_size.geometry('398x120')


    def check_num():
        global board_size2
        if ask.get() == '':
            board_size2 = 4
            tk_board_size.destroy()
        elif not ask.get().isdigit():
            lbl1.config(text='please enter numbers without char. try again', fg='red')
            lbl1.pack()
        elif int(ask.get()) > 5 or int(ask.get()) == 1:
            lbl1.config(text='please enter number smaller than the 5 and bigger than the 2', fg='red')
            lbl1.pack()
        else:
            if int(ask.get()) < 5 and int(ask.get()) != 1:
                board_size2 = int(ask.get())
                tk_board_size.destroy()


    tk.Label(tk_board_size, text='please enter the size of board of for play (2 or 3 or 4 or default = click apply)').pack()
    ask = tk.Entry(tk_board_size)
    ask.pack()
    btn_check = tk.Button(tk_board_size, text='apply', command=check_num)
    btn_check.pack()
    lbl1 = tk.Label(text='')
    tk_board_size.mainloop()
    tic_tac_toe = TicTacToeGUI(board_size2)
    tic_tac_toe.run()
