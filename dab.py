import PySimpleGUI as Sg
import io
import os

layout = [[Sg.Text("lol", key='what', text_color='black'), [Sg.Button("Load All data!", key='refresh'), Sg.Button("Open Where is saved?", visible=False, key='tftf')]]]

window = Sg.Window('Test', layout, icon='icon.ico')
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == Sg.WINDOW_CLOSED or event == 'Quit':
        break
    if event == 'tftf':
        path = 'data.txt'
        path = os.path.realpath(path)
        os.startfile(path)
    if event == 'refresh':
        window.refresh()
        f = open("data.txt", "r")
        window['what'].update(f.read().upper())
        window['tftf'].update(visible=True)
        window.refresh()
        f = open("data.txt", "r")
        print(f.read().upper())
window.close()
