import functions
import FreeSimpleGUI as sg

lable = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")


window = sg.Window('My To-Do App', 
                   layout= [[lable], [input_box], [add_button] ], 
                   font=('Helvetica', 20)
                   
                   )
#layput is a argu that expect a list, item in the inner square bracket will be on the same row

while True:
        
        event, values = window.read()
        match event:
                case "Add":
                        todos = functions.get_todos()
                        new_todo = values['todo'] + "\n"
                        todos.append(new_todo)
                        functions.write_todos(todos)
                case sg.WIN_CLOSED:
                        break
                
                        


window.close()

 