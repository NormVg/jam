import inquirer
from inquirer import themes

from rich.console import Console
from rich.theme import Theme
from rich.prompt import Prompt ,Confirm
from rich.markdown import Markdown
from rich.table import Table


from yaspin import yaspin

theme = Theme({"ok":"green","err":"red","high":"cyan"})
console = Console(theme=theme)

mytheme = themes.load_theme_from_dict({
    "Question": {
                 "mark_color": "yellow",
                 "brackets_color": "red",
                 
                 },
    "List": {
                 "selection_color": "green",
                 "selection_cursor": ">"
             }
})


class terminal:
    
    def error(txt:str):
        console.print(txt,style="err")
    
    def high(txt:str):
        console.print(txt,style="high")
    
    def good(txt:str):
        console.print(txt,style="ok")
    
    def show(txt:str):
        console.print(txt)
    
    def ask(txt:str,default=None,required=False):
        if not required:
            resp = Prompt.ask(f"[green]{txt}[/green]",default=default)   
            return resp
        if required:
            while True:
                resp = Prompt.ask(f"[green]{txt}[/green]",default=None)   
                if not resp:
                    pass
                else:
                    return resp
        
    
    def confirm(txt:str):
        resp = Confirm.ask(txt)
        return resp
    
    def markdown(md:str,style=None):
        txt = Markdown(md)
        if style == "error":
            console.print(txt,style="err")
        
        elif style == "good":
            console.print(txt,style="ok")
        
        elif style == "high":
            console.print(txt,style="high")
        
        else:
            console.print(txt)
    
    def mcq(option:list,questions:str):
        questions = [
                    inquirer.List('answer',message=questions, choices=option, ),
                    ]
        answers = inquirer.prompt(questions,theme=mytheme)
        return answers['answer']
    
    def loading(txt:str):
        spinner = yaspin(text=txt,color="yellow")
        spinner.start()
        return spinner

    def table(name:str,column:list , row: list):
        table = Table(title=name,expand=True,title_style="ok")
        
        for i in column:
            table.add_column(i, justify="center", style="red", no_wrap=False,overflow="fold")
        
        for x in row:
            table.add_row(*x)

        console.print(table)