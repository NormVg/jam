import os
import sys

import typer
from typing import Optional
from typing_extensions import Annotated

from bindings.gobindings import apInstall,apList,apRemove,apUpdate ,Ping
from plugs.mytui import terminal



app = typer.Typer()

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))



#this is for installeing APP
@app.command()
def install(name: Annotated[Optional[str], typer.Argument()] = None,
            file: Annotated[Optional[str], typer.Argument()] = None,
            icon: Annotated[Optional[str], typer.Argument()] = None,
            version:  Annotated[Optional[str], typer.Argument()] = None):
    
    if not name:
        name = terminal.ask("App Name",required=True)    
    if not file:
        file = terminal.ask("AppImage File path",required=True)
    if not icon:
        icon = terminal.ask("App icon path",default="jam-default-icon")
        if icon == "jam-default-icon":
            icon = f"{ROOT_DIR}/assets/icon.png"
    if not version:
        version = terminal.ask("App version", default="i-dont-care")
    
    name = name.replace(" ","-")

    if " " in file:
        terminal.error("Spaces in App paths are not allowed. Please rename without spaces.")
        sys.exit()

    if " " in icon:
        terminal.error("Spaces in Icon paths are not allowed. Please rename without spaces.")
        sys.exit()
    


    yn = terminal.confirm(f"Do you want to install {name}?")    
    if yn:
        apInstall(name,file,icon,version)
        terminal.good(f"{name} installed successfully.")
    else:
        terminal.error("Operation cancelled")
    
                

#this is for removing APP
@app.command()
def rm(id:  Annotated[Optional[str], typer.Argument()] = None):
    
    json_data = apList()
    if json_data == None:
        terminal.high("App List is Empty")
        sys.exit()

    if not id:
        app = []
        for i in json_data:
            app.append(f"{i['name']} - {i['id']} - {i['version']}")
        choosen = terminal.mcq(app,"Choose Your App to Delete")
        id = str(choosen).split(" - ")[1]
        name = str(choosen).split(" - ")[0]
    yn = terminal.confirm(f"Do you want to remove {name}?")    
    if yn:
        apRemove(id)
        terminal.good(f"{name} removed successfully.")
    else:
        terminal.error("Operation cancelled")

# this is for listing alll the APP
@app.command()
def list():
    print('''

 ╦┬ ┬┌─┐┌┬┐  ╔═╗┌─┐┌─┐╦┌┬┐┌─┐┌─┐┌─┐  ╔╦╗┌─┐┌┐┌┌─┐┌─┐┌─┐┬─┐
 ║│ │└─┐ │   ╠═╣├─┘├─┘║│││├─┤│ ┬├┤   ║║║├─┤│││├─┤│ ┬├┤ ├┬┘
╚╝└─┘└─┘ ┴   ╩ ╩┴  ┴  ╩┴ ┴┴ ┴└─┘└─┘  ╩ ╩┴ ┴┘└┘┴ ┴└─┘└─┘┴└─
    ''')
    json_data = apList()
    if json_data == None:
        
        terminal.high("App List is Empty")
        sys.exit()
    app = []
    for i in json_data:
        app.append([i['name'],i['id'],i['version'],i['file']])
    terminal.table("",["Name","ID","Version","AppImage File"],app)

# this is for updateing app registry
@app.command()
def update(id:  Annotated[Optional[str], typer.Argument()] = None, name: Annotated[Optional[str], typer.Argument()] = None,file: Annotated[Optional[str], typer.Argument()] = None,icon: Annotated[Optional[str], typer.Argument()] = None,version:  Annotated[Optional[str], typer.Argument()] = None):
    
    json_data = apList()
    if json_data == None:
        
        terminal.high("App List is Empty")
        sys.sys.exit()
    
    default = None
    

    if not id:
        
        app = []
        for i in json_data:
            app.append(f"{i['name']} - {i['id']} - {i['version']}")
        choosen = terminal.mcq(app,"Choose Your App to Update")
        id = str(choosen).split(" - ")[1]
        for i in json_data:
            if i['id'] == id:
                default = i
            
    
    if not name:
        name = terminal.ask("New App Name",default=default['name'])    
    if not file:
        file = terminal.ask("New AppImage File path",default=default['file'])
    if not icon:
        icon = terminal.ask("New App icon path",default=default['icon'])
        
    if not version:
        version = terminal.ask("New App version", default=default['version'])
    
    name = name.replace(" ","-")

    if " " in file:
        terminal.error("Spaces in App paths are not allowed. Please rename without spaces.")
        sys.exit()

    if " " in icon:
        terminal.error("Spaces in Icon paths are not allowed. Please rename without spaces.")
        sys.exit()
         



    if name != default['name'] or file != default['file']  or icon != default['icon'] or version != default['version']:
    
        yn = terminal.confirm("do you want to update "+name+" ?" )    
        if yn:
            apUpdate(name,file,icon,version,id)
            terminal.good(f"{name} updated successfully.")
        else:
            terminal.error("Operation cancelled")
    else:
        terminal.error("Nothing changes, Not Updating DB")

    


@app.command()
def ping():
    Ping()


def Home():
    print('''
		     ▄▄▄ ▄▄▄▄▄▄ ▄▄   ▄▄
		    █   █      █  █▄█  █
		    █   █  ▄   █       █
		 ▄  █   █ █▄█  █       █
		█ █▄█   █      █       █
		█       █  ▄   █ ██▄██ █
		█▄▄▄▄▄▄▄█▄█ █▄▄█▄█   █▄█

 ╦┬ ┬┌─┐┌┬┐  ╔═╗┌─┐┌─┐╦┌┬┐┌─┐┌─┐┌─┐  ╔╦╗┌─┐┌┐┌┌─┐┌─┐┌─┐┬─┐
 ║│ │└─┐ │   ╠═╣├─┘├─┘║│││├─┤│ ┬├┤   ║║║├─┤│││├─┤│ ┬├┤ ├┬┘
╚╝└─┘└─┘ ┴   ╩ ╩┴  ┴  ╩┴ ┴┴ ┴└─┘└─┘  ╩ ╩┴ ┴┘└┘┴ ┴└─┘└─┘┴└─
''')


if __name__ == "__main__":
    
    if len(sys.argv) != 1:
        app()
    else:
        typer.run(Home)

