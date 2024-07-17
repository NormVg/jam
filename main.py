import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
os.system(f"cd {ROOT_DIR}/bindings && go build -buildmode=c-shared -o library.so main.go && cd ..")

import typer
from typing import Optional
from typing_extensions import Annotated

from bindings.gobindings import apInstall,apList,apRemove,apUpdate ,Ping
# from plugs.mytui.terminal import ask
from plugs.mytui import terminal




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
    
    
    apInstall(name,file,icon,version)
                

#this is for removing APP
@app.command()
def rm(name: str):
    apRemove()

# this is for listing alll the APP
@app.command()
def list():

    apList()

# this is for updateing app registry
@app.command()
def update(name: str):
    apUpdate()


@app.command()
def ping():
    Ping()


if __name__ == "__main__":
    app()