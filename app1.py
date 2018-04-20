#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 21:23:34 2020

@author: oyewunmi
"""
# importing the necessary packages
import tkinter as tk
from tkinter import messagebox as msg
import Pmw
from random import shuffle
# import tkinter.ttk as ttk


class Game(tk.Tk):
    "The class for the game"
    global b_list, appender_lst
    global t1, t2
    b_list = []
    appender_lst = []
    turns_list = ['X', 'O']
    shuffle(turns_list, random=None)
    t1 = turns_list[0]
    t2 = turns_list[1]
    for i in range(9):
        appender_lst.append('')

    def __init__(self, *args, **kwargs):
        "This is the constructor method"
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Tic Tac Toe')
        self.interface()

    def interface(self):
        "this is the class method for creating the game interface"
        self.Bar = tk.Frame(self, relief='raised', bd=2)
        self.Bar.pack(fill='x')
        self.make_sett()
        self.make_help()
        self.make_about()
        self.make_grid()
        # self.Bar.tk_menuBar(Settings_Btn, Help_Btn, About_btn)

    def make_sett(self):
        'creating the settings menubutton'
        self.var = tk.IntVar()
        Menu_buttons = tk.Menubutton(self.Bar, text='Settings')
        Menu_buttons.pack(side='left')
        Menu_buttons.menu = tk.Menu(Menu_buttons)
        Menu_buttons.menu.add_command(label='Play against', state='disabled')
        Menu_buttons.menu.add_radiobutton(label='Human', variable=self.var, value=0, command=self.rdbtn)
        Menu_buttons.menu.add_radiobutton(label='Computer', value=1, variable=self.var, command=self.rdbtn)
        Menu_buttons['menu'] = Menu_buttons.menu
        return Menu_buttons

    def make_help(self):
        'Creating the help menubutton'
        Menu_buttons2 = tk.Button(self.Bar, text='Help', relief='flat',
                                  command=self.Msg)
        Menu_buttons2.pack(side='left')
        return Menu_buttons2

    def make_about(self):
        'creating the about menubutton'
        Menu_buttons3 = tk.Button(self.Bar, text='About', relief='flat',
                                  command=self.About)
        Menu_buttons3.pack(side='left')
        return Menu_buttons3

    def Msg(self):
        'callback for the Help menubutton'
        msg.showinfo('Help')

    def About(self):
        'callback for the About menubutton'
        Frame = tk.Toplevel(self)
        Pmw.aboutversion('1.0')
        Pmw.aboutcontact('Credits:\n Oyewunmi oluwaseyi\n email:oluwaseyi oyewunmi\n github oyewunmio')
        Pmw.AboutDialog(Frame, applicationname='About')
        Frame.withdraw()

    def rdbtn(self):
        'callback to read the value of the radiobuttons in settings menubutton'
        self.Player2 = self.var.get()
        for i in appender_lst:
            if i != '':
                msg.showinfo('', 'Game in progress...settings will take effect after game')
        if self.Player2 == 1:
            self.computer_moves()

    def cb(self):
        'Callback for button 1'
        if 0 in b_list:
            msg.showerror('Error', 'Box filled')
        else:
            b_list.append(0)
        # print(b_list)
        self.turns()

    def cb1(self):
        'Callback for button 2'
        if 1 in b_list:
            msg.showerror('Error', 'Box filled')
        else:
            b_list.append(1)
        # print(b_list)
        self.turns()

    def cb2(self):
        'Callback for button 3'
        if 2 in b_list:
            msg.showerror('Error', 'Box filled')
        else:
            b_list.append(2)
        # print(b_list)
        self.turns()

    def cb3(self):
        'Callback for button 4'
        if 3 in b_list:
            msg.showerror('Error', 'Box filled')
        else:
            b_list.append(3)
        # print(b_list)
        self.turns()

    def cb4(self):
        'Callback for button 5'
        if 4 in b_list:
            msg.showerror('Error', 'Box filled')
        else:
            b_list.append(4)
        # print(b_list)
        self.turns()

    def cb5(self):
        'Callback for button 6'
        if 5 in b_list:
            msg.showerror('Error', 'Box filled')
        else:
            b_list.append(5)
        # print(b_list)
        self.turns()

    def cb6(self):
        'Callback for button 7'
        if 6 in b_list:
            msg.showerror('Error', 'Box filled')
        else:
            b_list.append(6)
        # print(b_list)
        self.turns()

    def cb7(self):
        'Callback for button 8'
        if 7 in b_list:
            msg.showerror('Error', 'Box filled')
        else:
            b_list.append(7)
        # print(b_list)
        self.turns()

    def cb8(self):
        'Callback for button 9'
        if 8 in b_list:
            msg.showerror('Error', 'Box filled')
        else:
            b_list.append(8)
        # print(b_list)
        self.turns()

    def make_grid(self):
        'class method to create the game 3x3 grid'
        S_frame = tk.Frame(self)
        S_frame.pack(fill='both')
        self.R1 = tk.Button(S_frame, text='', width=5, relief='sunken', bg='black', fg='white', command=self.cb)
        self.R2 = tk.Button(S_frame, text='', width=5, relief='sunken', bg='black', fg='white', command=self.cb1)
        self.R3 = tk.Button(S_frame, text='', width=5, relief='sunken', bg='black', fg='white', command=self.cb2)
        self.R4 = tk.Button(S_frame, text='', width=5, relief='sunken', bg='black', fg='white', command=self.cb3)
        self.R5 = tk.Button(S_frame, text='', width=5, relief='sunken', bg='black', fg='white', command=self.cb4)
        self.R6 = tk.Button(S_frame, text='', width=5, relief='sunken', bg='black', fg='white', command=self.cb5)
        self.R7 = tk.Button(S_frame, text='', width=5, relief='sunken', bg='black', fg='white', command=self.cb6)
        self.R8 = tk.Button(S_frame, text='', width=5, relief='sunken', bg='black', fg='white', command=self.cb7)
        self.R9 = tk.Button(S_frame, text='', width=5, relief='sunken', bg='black', fg='white', command=self.cb8)
        self.R1.grid(row=0, column=0)
        self.R2.grid(row=0, column=1)
        self.R3.grid(row=0, column=2)
        self.R4.grid(row=1, column=0)
        self.R5.grid(row=1, column=1)
        self.R6.grid(row=1, column=2)
        self.R7.grid(row=2, column=0)
        self.R8.grid(row=2, column=1)
        self.R9.grid(row=2, column=2)
        self.but_id = [self.R1, self.R2, self.R3, self.R4, self.R5, self.R6, self.R7, self.R8, self.R9]

    def turns(self):
        'determines the turns for the human moves'
        
        # v = value
        board1 = b_list[:]
        # print(board1)
        # print(v)
        for i in board1:
            if len(board1) > 0 and len(board1) <= 1:
                self.but_id[board1[0]].config(text=t2)
                appender_lst[board1[0]] = t2
            elif len(board1) > 1 and len(board1) <= 2:
                self.but_id[board1[1]].config(text=t1)
                appender_lst[board1[1]] = t1
            elif len(board1) > 2 and len(board1) <= 3:
                self.but_id[board1[2]].config(text=t2)
                appender_lst[board1[2]] = t2
            elif len(board1) > 3 and len(board1) <= 4:
                self.but_id[board1[3]].config(text=t1)
                appender_lst[board1[3]] = t1
            elif len(board1) > 4 and len(board1) <= 5:
                self.but_id[board1[4]].config(text=t2)
                appender_lst[board1[4]] = t2
            elif len(board1) > 5 and len(board1) <= 6:
                self.but_id[board1[5]].config(text=t1)
                appender_lst[board1[5]] = t1
            elif len(board1) > 6 and len(board1) <= 7:
                self.but_id[board1[6]].config(text=t2)
                appender_lst[board1[6]] = t2
            elif len(board1) > 7 and len(board1) <= 8:
                self.but_id[board1[7]].config(text=t1)
                appender_lst[board1[7]] = t1
            elif len(board1) > 8 and len(board1) <= 9:
                self.but_id[board1[8]].config(text=t2)
                appender_lst[board1[8]] = t2
        # print(appender_lst)
        self.winning()

    def winning(self):
        'Checks the game and checks if we have a winner or a tie'
        board = appender_lst[:]
        ways_to_win = ((0, 1, 2),
                       (3, 4, 5),
                       (6, 7, 8),
                       (0, 3, 6),
                       (1, 4, 7),
                       (2, 5, 8),
                       (0, 4, 8),
                       (2, 4, 6))
        winner = ''
        for rows in ways_to_win:
            if board[rows[0]] == board[rows[1]] == board[rows[2]] != '':
                winner = board[rows[0]]
                msg.showinfo('', 'Player {} won the game'.format(winner))
                self.restart()
        if len(board) == 9 and '' not in board:
            if winner != 'X' or 'O':
                msg.showinfo('', 'The game ended in a tie')
                self.restart()
        return winner
    

    def restart(self):
        'This method asks the user whether they are interested in playing the game again or not.'
        # Frame = tk.Toplevel(self)
        dialog = Pmw.MessageDialog(self, title='Play again?',
        buttons=('Yes', 'No'),
        message_text='Do you want to play again')
        option_s = dialog.activate()
        # print ('You selected', option_s)
        if option_s == 'No':
            self.destroy()
        else:
            b_list.clear()
            appender_lst.clear()
            for i in range(9):
                appender_lst.append('')
                self.but_id[i].config(text='')
           

    # def computer_moves(self):
    #     'finds the best moves for the computer to play in'
    #     print('am here')
    #     board = appender_lst[:]
    #     print(board)
    #     best_moves = (0, 1, 2, 3, 4, 5, 6, 7, 8)
    #     for moves in board:
    #         if moves != '':
    #             board[moves] = t2
    #             if self.winning() == t2:
    #                 print('am here')
            

Game().mainloop()
