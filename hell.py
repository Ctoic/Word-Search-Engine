import PySimpleGUI as sg
sg.theme('DarkAmber')   # Add a touch of color

# THen create a layout how you position gui elements
layout = [
    [
        sg.Text("Enter your name")
    ]
        ,
    [
        sg.InputText(),
    ]
        ,
    [
         sg.Text("Enter your password")
    ]
    ,
[
        sg.InputText(),
    ]
        ,

    [
        sg.Button("Ok"), sg.Button("Cancel")
    ]
]
# Now set your window
window = sg.Window("Form", layout)
# set your event loop to read events
while True:
    event, values = window.read()
    if event == "Cancel" or event == sg.WIN_CLOSED:
        break
    print("You entered ", values[0])
    print("your Password is ", values[1])

# Finally close window when done
window.close() # A good practise

# Now you are good to Go
