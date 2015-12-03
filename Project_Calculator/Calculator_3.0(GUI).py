import tkinter
CAL_BUTTON = ['CE', 'C', 'BS', 'Log',
              '7',  '8', '9', '/',
              '4',  '5', '6', '*',
              '1',  '2', '3', '-',
              '0',  '.', '=', '+']
CAL_RESULT = 0
NUM_CHECK = ('0','1','2','3','4','5','6','7','8','9','.')
SIGN_CHECK = ('+','-','*','/')
BUTTON_SIZE = 5
GAP = 10
ROW = 1
COL = 0
NUM = []
PUSH_RESULT = 0

def Push(i):
    global PUSH_RESULT
    if i in NUM_CHECK:
        NUM.append(i)
        PUSH_RESULT = "".join(NUM)
    elif i in SIGN_CHECK:
        pass
    elif i == '=':
        pass

master = tkinter.Tk()
master.title('Calculator')
result = tkinter.Label(
    master,
    text=PUSH_RESULT,
    width=BUTTON_SIZE * 5,
    heigh=BUTTON_SIZE // 2 + 1,
    borderwidth=1,
    relief='sunken',
    background='lightgreen',
    padx=GAP,
    anchor='e'
)
result.grid(row=0, column=0, columnspan=4)

for i in CAL_BUTTON:
    PushI = Push(i)
    tkinter.Button(
        master,
        text=i,
        width=BUTTON_SIZE,
        height=BUTTON_SIZE // 2,
        command=PushI
    ).grid(
        row=ROW,
        column=COL
    )
    COL += 1
    if COL > 3:
        COL = 0
        ROW += 1


tkinter.mainloop()