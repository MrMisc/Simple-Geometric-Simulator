import subprocess
import json
import tkinter as tk
from tkinter.ttk import *
from tkinter import simpledialog
import customtkinter


#Default values
number = 1
trials = 100


customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("1650x700")
app.title("Bob")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)
# app.withdraw()
# the input dialog
# USER_INP = simpledialog.askstring(title="Test",
#                                   prompt="What's your Name?:")

# # check it out
# print("Hello", USER_INP)

# def infodump(info, methodology):
#     #methodology is going to be the type of data entry we are considering
#     # we want to generalise data collection and allocation to different variables
#     if methodology == 1:
#         return (method := int(info))
#     elif methodology == 2:
#     else: return None




class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Simple Roulette Simulator")
        self.geometry(f"{1080}x{600}")

        # configure grid layout (4x4)
        self.grid_columnconfigure((0,1,2),weight=1)
        # self.grid_columnconfigure((1,2,3,4,5,6), weight=7)
        self.grid_rowconfigure((0, 1,2,3,4), weight=1)
        # self.grid_rowconfigure((3,4), weight=4)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=20, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, columnspan = 1,rowspan=5, sticky="nsew")
        # self.sidebar_frame.grid_rowconfigure(4, weight=1)
        # self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Roulette Simulator", font=("CF Spaceship", 45))
        # self.logo_label.grid(row=0, column=0, padx=10, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,text = "Simulate" ,command=self.simulate,height=200, width = 400,hover_color="black", font=("Microsoft Yi Baiti", 60), corner_radius=20) # Microsoft Yi Baiti,OCR A Extended, Prestige Elite Std
        self.sidebar_button_1.grid(row=2, column=0, rowspan = 1, padx=0, pady=50)

        self.sidebar_trialentry = customtkinter.CTkEntry(self.sidebar_frame,placeholder_text = "     No of Trials" ,font=("OCR A Extended", 25), corner_radius=5, width=350, height= 100) # Microsoft Yi Baiti,OCR A Extended, Prestige Elite Std
        self.sidebar_trialentry.grid(row=1, column=0, rowspan = 1, padx=0, pady=50)        
        self.sidebar_itemnoentry = customtkinter.CTkEntry(self.sidebar_frame,placeholder_text = "     No of items" ,font=("OCR A Extended", 25), corner_radius=5, width=350, height= 100) # Microsoft Yi Baiti,OCR A Extended, Prestige Elite Std
        self.sidebar_itemnoentry.grid(row=0, column=0, rowspan = 1, padx=0, pady=20)                
        # self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        # self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        # self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        # self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        #Appearance mode 
        # self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="center", font=("Microsoft Yi Baiti", 20))
        # self.appearance_mode_label.grid(row=1, column=0, padx=20, pady=(0, 0))
        # self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
        #                                                                command=self.change_appearance_mode_event,font=("Microsoft Yi Baiti", 16))
        # self.appearance_mode_optionemenu.grid(row=2, column=0, padx=20, pady=(10, 10))
        # self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        # # self.scaling_label.grid(row=3, column=0, padx=20, pady=(10, 0))
        # self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
        #                                                        command=self.change_scaling_event)
        # self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        #Simulation 1
        self.entry = customtkinter.CTkEntry(self, placeholder_text= "Item names", font=("Microsoft Yi Baiti", 16), fg_color=("gray78", "gray28"),justify = "center")  #text inside typing spot
        self.entry.grid(row=1, column=1, columnspan=1,rowspan=3, padx=(40, 20), pady=(20, 20), sticky="nsew") 
        # self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=self.button1)
        # self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # self.entry2 = customtkinter.CTkEntry(self, placeholder_text="Number of runs ", font=("Microsoft Yi Baiti", 16), justify = "center")  #text inside typing spot
        # self.entry2.grid(row=2, column=2, columnspan=1, padx=(40, 20), pady=(20, 20), sticky="nsew") 

        # self.entry3 = customtkinter.CTkEntry(self, placeholder_text="Probability Structure", font=("Microsoft Yi Baiti", 16),justify = "center")
        # self.entry3.grid(row=3, column=1, columnspan=3, padx=(20, 0), pady=(20, 20), sticky="nsew")         

        # self.entry4 = customtkinter.CTkEntry(self, placeholder_text="Monetary Scheme", font=("Microsoft Yi Baiti", 16),justify = "center") 
        # self.entry4.grid(row=4, column=1, columnspan=3, padx=(20, 0), pady=(20, 20), sticky="nsew")        

        # self.entry5 = customtkinter.CTkEntry(self, placeholder_text="Starting point", font=("Microsoft Yi Baiti", 16),justify = "center") 
        # self.entry5.grid(row=5, column=2, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")                

        # self.entry6 = customtkinter.CTkEntry(self, placeholder_text="Falsecap parameter", font=("Microsoft Yi Baiti", 16),justify = "center")
        # self.entry6.grid(row=6, column=2, columnspan=1, padx=(40, 20), pady=(20, 20), sticky="nsew")                





    #simulation 2
        self.entry21 = customtkinter.CTkEntry(self, placeholder_text="Probabilities. Make them add to 1.", font=("Microsoft Yi Baiti", 16),justify = "center")
        self.entry21.grid(row=1, column=2, columnspan=1,rowspan=3, padx=(0,20), pady=(20, 20), sticky="nsew")  
        # self.main_button_2= customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=self.button2)
        # self.main_button_2.grid(row=2, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")        

        # self.entry22 = customtkinter.CTkEntry(self, placeholder_text="Number of runs ", font=("Microsoft Yi Baiti", 16),justify = "center")  
        # self.entry22.grid(row=2, column=5, columnspan=1, padx=(0,20), pady=(20, 20), sticky="nsew") 


        # self.entry23 = customtkinter.CTkEntry(self, placeholder_text="Probability Structure",font=("Microsoft Yi Baiti", 16),justify = "center")  
        # self.entry23.grid(row=3, column=4, columnspan=3, padx=(20, 0), pady=(20, 20), sticky="nsew")   

        # self.entry24 = customtkinter.CTkEntry(self, placeholder_text="Monetary Scheme",font=("Microsoft Yi Baiti", 16),justify = "center")  
        # self.entry24.grid(row=4, column=4, columnspan=3, padx=(20, 0), pady=(20, 20), sticky="nsew")      

        # self.entry25 = customtkinter.CTkEntry(self, placeholder_text="Starting point",font=("Microsoft Yi Baiti", 16),justify = "center")  
        # self.entry25.grid(row=5, column=5, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")     

        # self.entry26 = customtkinter.CTkEntry(self, placeholder_text="Falsecap parameter",font=("Microsoft Yi Baiti", 16),justify = "center")  
        # self.entry26.grid(row=6, column=5, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")                 


    

    def simulate(self):
        global trials
        global number
        try:number = max(1,int(self.sidebar_itemnoentry.get()))
        except:pass
        #falsecap
        try:probabilities = [float(x) for x in self.entry21.get().split(",")]
        except:pass
        try:items = self.entry.get().split(",")
        except:pass        
        try:trials = int(self.sidebar_trialentry.get())
        except:pass
        print(f"Number of trials set to {trials}")
        outputjson = {
            "items":items,"probabilities":probabilities, "number":number,"trials":trials
        }
        with open("./output.json", "w") as outfile:
            json.dump(outputjson, outfile)       
        # app.destroy()
        subprocess.Popen("cargo run | Rscript plot.R", shell=True) 
        # p_status = p.wait()
        # os.system("cargo run | py plot.py")
        # return None

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())


if __name__ == "__main__":
    app = App()
    app.mainloop()