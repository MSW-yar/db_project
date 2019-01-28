

from tkinter import *
import requestMethod


def printtext(event):
    doc = entry.get()
    doc=doc.title()
################################## second window opens#######################################
    searchbutton.place_forget()
    lable.place_forget()
    lable2.place_forget()
    entry.place_forget()

    scrollbar = Scrollbar(main_window)
    scrollbar.pack(side=RIGHT, fill=Y)
    area = Text(main_window, yscrollcommand=scrollbar.set,
                font=('Courier New', 11))
    area.pack(expand=True, fill='both')
    scrollbar.config(command=area.yview)
    if doc == '':
        output = requestMethod.get()
        for x in output:

            for key,item in x.items():

                area.insert(INSERT, key)
                area.insert(INSERT, "\n\n")
                area.insert(INSERT, item)
                area.insert(INSERT, "\n\n")
    else:
        output=requestMethod.post(doc)
        length=len(output)
        if length> 0:
            for x in output:

                for key,item in  x.items():

                    area.insert(INSERT,key)
                    area.insert(INSERT, "\n\n")
                    area.insert(INSERT, item)
                    area.insert(INSERT, "\n\n")
        else:
            area.insert(INSERT,'Error 404, Not found')
    
    area.config(state=DISABLED)


############################## Start up window ###################################
main_window = Tk()
main_window.geometry('1100x650+50+100')
main_window.title('D-Checker')

entry = Entry(main_window, bd=2, relief='raised', width=60)
entry.place(x=340, y=250)
lable = Label(
    main_window, text='This is a medical search engine.', font='times 30')
lable.place(x=320, y=300)
lable2 = Label(main_window, text='D-Checker', fg='green', font='times 110')
lable2.place(x=280, y=80)

main_window.bind('<Return>',printtext)
searchbutton = Button(main_window, text='search', width=12,
                      height=1, bd=3, relief='raised')
searchbutton.bind('<Button-1>',printtext)
searchbutton.place(x=760, y=246)


main_window.mainloop()
