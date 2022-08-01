import PySimpleGUI as Sg
import io

layout = [[Sg.InputText("000-000-000", key='lol')], [Sg.In("Call Type", key='ews')], [Sg.In(visible=False, key='teras'),
                                                     Sg.CalendarButton("When they call you?", key="test", target='teras'),
                                                     Sg.Button("Put Data?", key="3232", visible=True)],
         [Sg.Button('Are You Sure?', key='lot', visible=False)]]

window = Sg.Window('Test', layout, icon='icon.ico')
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == Sg.WINDOW_CLOSED or event == 'Quit':
        break
    if event == '3232':
        window['lot'].update(visible=True)
    if event == 'lolr':
        l3r = Sg.popup_get_date(modal=True, no_titlebar=False)
        if l3r != "":
            print("lol")
            window.refresh()
            window['rrer'].update(l3r, visible=True), window['lot'].update(visible=True)
    if event == 'lot':
        print(values['teras'])
        print(values['lol'])
        with io.open("data.txt", "a", encoding="utf8") as f:
            f.write("Phone Number: " + values['lol'])
            f.write(" ")
            f.write("When he call + date when it was post " + values['teras'])
            f.write(" Call type: " + values['ews'] + '\n')
        f.close()
        Sg.popup("SUCCES", "YOU PUT DATA IN SYSTEM!", icon='icon.ico')
        import dab
window.close()
