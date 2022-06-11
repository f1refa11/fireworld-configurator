print("FireWorld III Connection configuring tool")
print("Loading argparse")
from argparse import ArgumentParser, BooleanOptionalAction

cliParse = ArgumentParser("fireworld3_install.exe")
cliParse.add_argument("--nogui", required=False, help="Install Zerotier and configure connection to the FireWorld server", action=BooleanOptionalAction)
cliArgs = cliParse.parse_args()

print("Loading libraries")
from urllib.request import urlretrieve
from os.path import join
from os import remove, system, getenv, name
from nbtlib import load
from nbtlib.tag import String
from subprocess import call
from tkinter import Label, CENTER, messagebox, Tk, Button

def install():
    if name == "nt":
        urlretrieve("https://download.zerotier.com/dist/ZeroTier%20One.msi", "zerotier.msi")
        call('msiexec /i zerotier.msi')
        remove("zerotier.msi")
    else:
        call('curl -s https://install.zerotier.com | sudo bash')
    system("zerotier-cli join 8286ac0e47a7616d")
    if name == "nt":
        serverFilePath = join(getenv('APPDATA'), ".minecraft")
    else:
        from os.path import expanduser
        serverFilePath = join(expanduser("~"), ".minecraft")
    serverFile = load(join(serverFilePath, "servers.dat"))
    serverFile[""]["servers"].append({'ip': String('10.147.19.15'), 'name': String('FireWorld III')})
    serverFile.save()

if cliArgs.nogui:
    print("RUNNING CONSOLE MODE")
    install()
else:
    def installGui():
        install()
        messagebox.showinfo(title="FWCCT v3", message="Установка завершена!")
    root = Tk()
    root.geometry("320x102")
    root.title("FWCCT v3")
    root.configure(bg="#ffffff")
    mainTitle = Label(root, text="FWCCT", font="Arial 18", background="#ffffff")
    mainTitle.place(relx=0.5, y=25, anchor=CENTER)
    installButton = Button(text="Установить", bd=1, height=2, width=20, command=installGui, font="Arial 12 bold")
    installButton.place(x=5, y=50)
    root.mainloop()