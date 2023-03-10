import tkinter, customtkinter, os, requests, subprocess, shutil

# TODO: 
# 1. make minecraft server folder
#   1.5. download minecraft server file
# 2. make button for run minecraft server
# 3. make button for run ngrok tcp 25565
# 4. make button for remove world

def delete_world():
    shutil.rmtree(os.path.join("./", "world"))    

CONST_DONE = "done."

root_dir = "./"
print("make server folder...")
if not os.path.isdir("./server"):
    os.mkdir(os.path.join("./", "server"))
print(CONST_DONE)

print("download server file...")
if not os.path.exists(os.path.join("./", "server", 'server.jar')):
    url = "https://launcher.mojang.com/v1/objects/886945bfb2b978778c3a0288fd7fab09d315b25f/server.jar"
    res = requests.get(url)
    open("./server/server.jar", "wb").write(res.content)
print(CONST_DONE)

with open("./eula.txt", "w+") as f:
    f.write("eula=true")

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.title = "마크 서버 구동기"

def run_server():
    subprocess.Popen('java -jar ./server/server.jar nogui', creationflags=subprocess.CREATE_NEW_CONSOLE)

def run_ngrok():
    subprocess.Popen('ngrok tcp 25565', creationflags=subprocess.CREATE_NEW_CONSOLE)


btn_server = customtkinter.CTkButton(master=app, text="서버 시작", command=run_server)
btn_server.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
btn_ngrok = customtkinter.CTkButton(master=app, text="ngrok 시작", command=run_ngrok)
btn_ngrok.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
btn_ngrok = customtkinter.CTkButton(master=app, text="world 삭제", command=delete_world)
btn_ngrok.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)


app.mainloop()