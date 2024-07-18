import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
#os.system(f"cd {ROOT_DIR}/bindings && go build -buildmode=c-shared -o library.so main.go && cd ..")

import typer
from typing import Optional
from typing_extensions import Annotated

from bindings.gobindings import apInstall,apList,apRemove,apUpdate ,Ping
# from plugs.mytui.terminal import ask
from plugs.mytui import terminal

import sys


app = typer.Typer()




#this is for installeing APP
@app.command()
def install(name: Annotated[Optional[str], typer.Argument()] = None,file: Annotated[Optional[str], typer.Argument()] = None,icon: Annotated[Optional[str], typer.Argument()] = None,version:  Annotated[Optional[str], typer.Argument()] = None):
    
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
    
    yn = terminal.confirm("do you want to install "+name+" ?" )    
    if yn:
        apInstall(name,file,icon,version)
        terminal.good(f"{name} install successfully.")
    else:
        terminal.error("Operation cancelled")
    
                

#this is for removing APP
@app.command()
def rm(id:  Annotated[Optional[str], typer.Argument()] = None):
    if not id:
        json_data = apList()
        app = []
        for i in json_data:
            app.append(f"{i['name']} - {i['id']} - {i['version']}")
        choosen = terminal.mcq(app,"Choose Your App to Delete")
        id = str(choosen).split(" - ")[1]
        name = str(choosen).split(" - ")[0]
    yn = terminal.confirm("do you want to remove "+name+" ?" )    
    if yn:
        apRemove(id)
        terminal.good(f"{name} removed successfully.")
    else:
        terminal.error("Operation cancelled")

# this is for listing alll the APP
@app.command()
def list():

    json_data = apList()
    app = []
    for i in json_data:
        app.append([i['name'],i['id'],i['version'],i['file']])
    terminal.table("AppImage App's List",["Name","ID","Version","AppImage File"],app)

# this is for updateing app registry
@app.command()
def update(id:  Annotated[Optional[str], typer.Argument()] = None, name: Annotated[Optional[str], typer.Argument()] = None,file: Annotated[Optional[str], typer.Argument()] = None,icon: Annotated[Optional[str], typer.Argument()] = None,version:  Annotated[Optional[str], typer.Argument()] = None):
    
    default = None
    

    if not id:
        json_data = apList()
        app = []
        for i in json_data:
            app.append(f"{i['name']} - {i['id']} - {i['version']}")
        choosen = terminal.mcq(app,"Choose Your App to Delete")
        id = str(choosen).split(" - ")[1]
        for i in json_data:
            if i['id'] == id:
                default = i
            
    
    if not name:
        name = terminal.ask("App Name",default=default['name'])    
    if not file:
        file = terminal.ask("AppImage File path",default=default['file'])
    if not icon:
        icon = terminal.ask("App icon path",default=default['icon'])
        
    if not version:
        version = terminal.ask("App version", default=default['version'])
    
    
    if name != default['name'] or file != default['file']  or icon != default['icon'] or version != default['version']:
    
        yn = terminal.confirm("do you want to update "+name+" ?" )    
        if yn:
            print(name,file,icon,version)
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
''')


if __name__ == "__main__":
    
    if len(sys.argv) != 1:
        app()
    else:
        typer.run(Home)

