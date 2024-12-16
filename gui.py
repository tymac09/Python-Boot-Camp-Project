import functions
import FreeSimpleGUI as sg

lable = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")


window = sg.Window('My To-Do App', layout= [[lable], [input_box],[add_button]]) #layput is a argu that expect a list, item in the inner square bracket will be on the same row

window.read()
window.close()

 