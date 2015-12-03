import tkinter

CALCULATOR_BUTTON = {
    'CE': 0,   'C': 1,  'BS': 2,   'Log': 3,
    '7' : 4,   '8': 5,  '9' : 6,   '/'  : 7,
    '4' : 8,   '5': 9,  '6' : 10,  '*'  : 11,
    '1' : 12,  '2': 13, '3' : 14,  '-'  : 15,
    '0' : 16,  '.': 17, '=' : 18,  '+'  : 19
}
NUM_CHECK = ('0','1','2','3','4','5','6','7','8','9','.')
SIGN_CHECK = ('+','-','*','/')
RESULT = 0
ROW = 1
COL = 0
PUSHED_VALUE = []

def Make_button(name):
    BT = tkinter.Button(
        root,
        text=name,
        width=5,
        height=2,
        font='Verdana 11',
        relief='groove',
        bg='darkgray'
    )
    return BT

root = tkinter.Tk()
root.title('UI\'s Calculator')
result_window = tkinter.Label(root)
result_window.config(text=RESULT, font='Verdana 14', bg='lightgreen', relief='sunken', width=17, height=3, anchor='e', padx=10)
result_window.grid(row=0, column=0, columnspan=4)

for key in sorted(CALCULATOR_BUTTON, key=CALCULATOR_BUTTON.get):
    CALCULATOR_BUTTON[key] = Make_button(key)
    CALCULATOR_BUTTON[key].grid(row=ROW, column=COL)
    COL += 1
    if COL > 3:
        COL = 0
        ROW += 1

tkinter.mainloop()