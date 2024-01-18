import tkinter as ttk

root = ttk.Tk()
root.geometry("1000x1000")



class button_creation_env:
    def __init__(self) -> None:
        pass

    def copy_script(self):
        root.clipboard_clear()
        root.clipboard_append(self.show_button_script_text.get())

    def button_update(self,*args):

        skip=False
        #Verifies that there are integers in the entrys that require it
        try:
            int(self.font_size.get())
            int(self.height_value.get())
            int(self.width_value.get())
        except ValueError:
            skip=True

        #Verifies that the colour are colours supported by tkinter
        try:
            root.winfo_rgb(self.background_colour_value.get())
            root.winfo_rgb(self.foreground_colour_value.get())
            root.winfo_rgb(self.active_foreground_colour_value.get())
            root.winfo_rgb(self.active_background_colour_value.get())
        except ttk.TclError:
            skip=True
        

        if skip != True:
            
            #Changes the boolean values in checkboxes to text
            state="normal"
            if self.status.get()==True:
                state="normal"
            elif self.status.get()==False:
                state="disabled"

            border=1
            if self.border.get()==True:
                border=1
            elif self.border.get()==False:
                border=0
            
            #Showcase button
            self.show_button.config(foreground=self.foreground_colour_value.get(), background=self.background_colour_value.get()
                                    , activeforeground=self.active_foreground_colour_value.get(), activebackground=self.active_background_colour_value.get()
                                    , font=("Arial",int(self.font_size_var.get())), state=state,border=border, height=int(self.height_value.get()),
                                    width=int(self.width_value.get()))
            #Button line
            self.show_button_script_text.set(f"tkinter.Button(root, foreground=\"{self.foreground_colour_value.get()}\", background=\"{self.background_colour_value.get()}\""+
            f", activeforeground=\"{self.active_foreground_colour_value.get()}\", activebackground=\"{self.active_background_colour_value.get()}\""+
            f", text=\"{self.button_text.get()}\", font=(\"Arial\", {int(self.font_size.get())}), state=\"{state}\", border={border}, height={self.height_value.get()}"+
            f", width={self.width_value.get()})")

    def placement(self):
        skip=False
        #Verifies that there are integers in the entrys that require it
        try:
            int(self.font_size.get())
            int(self.height_value.get())
            int(self.width_value.get())
            int(self.row.get())
            int(self.column.get())
        except ValueError:
            skip=True

        #Verifies that the colour are colours supported by tkinter
        try:
            root.winfo_rgb(self.background_colour_value.get())
            root.winfo_rgb(self.foreground_colour_value.get())
            root.winfo_rgb(self.active_foreground_colour_value.get())
            root.winfo_rgb(self.active_background_colour_value.get())
        except ttk.TclError:
            skip=True
        
        placeable=True
        for listed in stuff:
            if listed[1] == self.row.get() and listed[2] == self.column.get():
                placeable=False
                break

        if skip != True and placeable:
            
            #Changes the boolean values in checkboxes to text
            state="normal"
            if self.status.get()==True:
                state="normal"
            elif self.status.get()==False:
                state="disabled"

            border=1
            if self.border.get()==True:
                border=1
            elif self.border.get()==False:
                border=0
            

            button=ttk.Button(element_frame,text=self.text_change_field.get() , foreground=self.foreground_colour_value.get(), background=self.background_colour_value.get()
                                    , activeforeground=self.active_foreground_colour_value.get(), activebackground=self.active_background_colour_value.get()
                                    , font=("Arial",int(self.font_size_var.get())), state=state,border=border, height=int(self.height_value.get()),
                                    width=int(self.width_value.get()))
            button.grid(row=self.row.get(), column=self.column.get())
            stuff.append([button,self.row.get(),self.column.get(),self.show_button_script_text.get(),self.button_text.get()])         

    def edit_enable(self):

        #Enables editting and sets the default values
        self.font_size_var.set(15)
        self.foreground_colour_value.set("Black")
        self.background_colour_value.set("Grey")
        self.active_foreground_colour_value.set("Black")
        self.active_background_colour_value.set("White")
        self.height_value.set("3")
        self.width_value.set("10")
        self.row.set("1")
        self.column.set("1")

        self.font_size.config(state="normal")
        self.text_change_field.config(state="normal")
        self.status_button.config(state="normal")
        self.border_button.config(state="normal")
        self.foreground_colour_entry.config(state="normal")
        self.background_colour_entry.config(state="normal")
        self.active_foreground_colour_entry.config(state="normal")
        self.active_background_colour_entry.config(state="normal")
        self.height_entry.config(state="normal")
        self.width_entry.config(state="normal")
        self.row_entry.config(state="normal")
        self.column_entry.config(state="normal")
        self.config_update.destroy()

    def create_button_env(self):
        self.new_window_cbe = ttk.Toplevel(root)
        self.new_window_cbe.title("Test")


        #Makes the button showcase
        self.button_text=ttk.StringVar(self.new_window_cbe,"Text")
        
        self.show_button = ttk.Button(self.new_window_cbe,foreground="Black",background="Grey",activeforeground="Black",activebackground="White"
                                      ,textvariable=self.button_text,font=("Arial",15),border=1,height=3,width=10)
        
        self.show_button_script_text= ttk.StringVar(self.new_window_cbe,f"tkinter.Button(root, foreground=\"Black\", background=\"Grey\", activeforeground=\"Black\""+
        f", activebackground=\"White\", text=\"{self.button_text.get()}\", font=(\"Arial\",15), state=\"normal\", border=1, height=3, width=10)")


        #The button that holds the button script!
        self.show_button_script = ttk.Button(self.new_window_cbe,textvariable=self.show_button_script_text,command=self.copy_script,border=0)

        #This button is the one to enable editing
        self.config_update = ttk.Button(self.new_window_cbe, command=self.edit_enable, text="Edit",border=0)

        #A frame to hold all the config widgets
        self.configs=ttk.Frame(self.new_window_cbe,name="configs",borderwidth=1)

        #This is the font_size config
        self.font_size_var=ttk.StringVar(self.new_window_cbe,"Font Size",)
        self.font_size=ttk.Entry(self.configs,textvariable=self.font_size_var,state="readonly",border=0)
        self.font_size.bind("<KeyRelease>", self.button_update)

        #This is the field to set the button text
        self.text_change_field=ttk.Entry(self.configs,textvariable=self.button_text,state="readonly",border=0)
        self.text_change_field.bind("<KeyRelease>", self.button_update)

        #This is a widget to change the state of the button
        self.status=ttk.BooleanVar(self.new_window_cbe,value=True)
        self.status.trace_add("write",self.button_update)
        self.status_button=ttk.Checkbutton(self.configs,text="Active?",variable=self.status,state="disabled",border=0)

        #This is a widget to enable or disable the border
        self.border=ttk.BooleanVar(self.new_window_cbe,True)
        self.border.trace_add("write",self.button_update)
        self.border_button=ttk.Checkbutton(self.configs,text="Border",variable=self.border,state="disabled",border=0)

        #Button colour changer
        self.foreground_colour_value=ttk.StringVar(self.new_window_cbe,"Foreground Colour")
        self.foreground_colour_entry=ttk.Entry(self.configs,textvariable=self.foreground_colour_value,state="readonly",width=25,border=0)
        self.foreground_colour_entry.bind("<KeyRelease>",self.button_update)

        self.background_colour_value=ttk.StringVar(self.new_window_cbe,"Background Colour")
        self.background_colour_entry=ttk.Entry(self.configs,textvariable=self.background_colour_value,state="readonly",width=25,border=0)
        self.background_colour_entry.bind("<KeyRelease>",self.button_update)

        self.active_foreground_colour_value=ttk.StringVar(self.new_window_cbe,"Active Foreground Colour")
        self.active_foreground_colour_entry=ttk.Entry(self.configs,textvariable=self.active_foreground_colour_value,state="readonly",width=25,border=0)
        self.active_foreground_colour_entry.bind("<KeyRelease>",self.button_update)

        self.active_background_colour_value=ttk.StringVar(self.new_window_cbe,"Active Background Colour")
        self.active_background_colour_entry=ttk.Entry(self.configs,textvariable=self.active_background_colour_value,state="readonly",width=25,border=0)
        self.active_background_colour_entry.bind("<KeyRelease>",self.button_update)

        #Change the buttons height slash width
        self.height_value=ttk.StringVar(self.new_window_cbe,"Height")
        self.height_entry=ttk.Entry(self.configs,textvariable=self.height_value,state="readonly",border=0)
        self.height_entry.bind("<KeyRelease>",self.button_update)

        self.width_value=ttk.StringVar(self.new_window_cbe,"Width")
        self.width_entry=ttk.Entry(self.configs,textvariable=self.width_value,state="readonly",border=0)
        self.width_entry.bind("<KeyRelease>",self.button_update)

        #Button location on grid
        self.row=ttk.StringVar(self.new_window_cbe,value="Row")
        self.row_entry=ttk.Entry(self.new_window_cbe,border=0,state="readonly",textvariable=self.row)

        self.column=ttk.StringVar(self.new_window_cbe,value="Column")
        self.column_entry=ttk.Entry(self.new_window_cbe,border=0,state="readonly",textvariable=self.column)

        self.place=ttk.Button(self.new_window_cbe,text="Place",border=0,command=self.placement)

        #Sets the location of screen elements
        self.show_button.grid(column=1,row=1)
        self.show_button_script.grid(column=1,row=2)
        self.configs.grid(column=1,row=3)
        self.status_button.grid(column=1,row=1)
        self.border_button.grid(column=1,row=2)
        self.font_size.grid(column=2,row=1)
        self.text_change_field.grid(column=2,row=2)
        self.foreground_colour_entry.grid(column=3,row=1)
        self.background_colour_entry.grid(column=3,row=2)
        self.active_foreground_colour_entry.grid(column=3,row=3)
        self.active_background_colour_entry.grid(column=3,row=4)
        self.height_entry.grid(column=2,row=3)
        self.width_entry.grid(column=2,row=4)
        self.row_entry.grid(column=1,row=100)
        self.column_entry.grid(column=1,row=101)
        self.place.grid(column=1,row=102)
        self.config_update.grid(column=1,row=499)
        ttk.Button(self.new_window_cbe,text="Close",command=self.new_window_cbe.destroy,border=0,foreground="red",activeforeground="red").grid(column=1,row=500)

class label_creation_env:
    def __init__(self) -> None:
        pass

    def copy_script(self):
        root.clipboard_clear()
        root.clipboard_append(self.show_label_script_text.get())

    def label_update(self,*args):
        skip=False
        #Verifies that there are integers in the entrys that require it
        try:
            int(self.font_size.get())
            int(self.height_value.get())
            int(self.width_value.get())
        except ValueError:
            skip=True

        #Verifies that the colour are colours supported by tkinter
        try:
            root.winfo_rgb(self.background_colour_value.get())
            root.winfo_rgb(self.foreground_colour_value.get())
        except ttk.TclError:
            skip=True
        

        if skip != True:
            border=1
            if self.border.get()==True:
                border=1
            elif self.border.get()==False:
                border=0
            
            #Showcase button
            self.show_label.config(foreground=self.foreground_colour_value.get(), background=self.background_colour_value.get()
                                    , font=("Arial",int(self.font_size_var.get())), border=border, height=int(self.height_value.get()),
                                    width=int(self.width_value.get()))
            #Button line
            self.show_label_script_text.set(f"tkinter.Label(root, foreground=\"{self.foreground_colour_value.get()}\", background=\"{self.background_colour_value.get()}\""+
            f", text=\"{self.label_text.get()}\", font=(\"Arial\", {int(self.font_size.get())}), border={border}, height={self.height_value.get()}"+
            f", width={self.width_value.get()})")

    def placement(self):
        skip=False
        #Verifies that there are integers in the entrys that require it
        try:
            int(self.font_size.get())
            int(self.height_value.get())
            int(self.width_value.get())
            int(self.row.get())
            int(self.column.get())
        except ValueError:
            skip=True

        #Verifies that the colour are colours supported by tkinter
        try:
            root.winfo_rgb(self.background_colour_value.get())
            root.winfo_rgb(self.foreground_colour_value.get())
        except ttk.TclError:
            skip=True
        
        placeable=True
        for listed in stuff:
            if listed[1] == self.row.get() and listed[2] == self.column.get():
                placeable=False
                break

        if skip != True and placeable:
            
            #Changes the boolean values in checkboxes to text

            border=1
            if self.border.get()==True:
                border=1
            elif self.border.get()==False:
                border=0
            

            label=ttk.Label(element_frame,text=self.text_change_field.get() , foreground=self.foreground_colour_value.get(), background=self.background_colour_value.get()
                                    , font=("Arial",int(self.font_size_var.get())),border=border, height=int(self.height_value.get()),
                                    width=int(self.width_value.get()))
            label.grid(row=self.row.get(), column=self.column.get())
            stuff.append([label,self.row.get(),self.column.get(),self.show_label_script_text.get(),self.label_text.get()])  

    def edit_enable(self):

        #Enables editting and sets the default values
        self.font_size_var.set(15)
        self.foreground_colour_value.set("Black")
        self.background_colour_value.set("Grey")
        self.height_value.set("3")
        self.width_value.set("10")
        self.row.set("1")
        self.column.set("1")

        self.font_size.config(state="normal")
        self.text_change_field.config(state="normal")
        self.border_button.config(state="normal")
        self.foreground_colour_entry.config(state="normal")
        self.background_colour_entry.config(state="normal")
        self.height_entry.config(state="normal")
        self.width_entry.config(state="normal")
        self.row_entry.config(state="normal")
        self.column_entry.config(state="normal")
        self.config_update.destroy()

    def create_label_env(self):
        self.new_window_cbe = ttk.Toplevel(root)
        self.new_window_cbe.title("Test")


        #Makes the label showcase
        self.label_text=ttk.StringVar(self.new_window_cbe,"Text")
        
        self.show_label = ttk.Label(self.new_window_cbe,foreground="Black",background="Grey",textvariable=self.label_text,font=("Arial",15),border=1,height=3,width=10)
        
        self.show_label_script_text= ttk.StringVar(self.new_window_cbe,f"tkinter.Label(root, foreground=\"Black\", background=\"Grey\""+
        f", text=\"{self.label_text.get()}\", font=(\"Arial\",15), border=1, height=3, width=10)")


        #The button that holds the label script!
        self.show_button_script = ttk.Button(self.new_window_cbe,textvariable=self.show_label_script_text,command=self.copy_script,border=0)

        #This button is the one to enable editing
        self.config_update = ttk.Button(self.new_window_cbe, command=self.edit_enable, text="Edit",border=0)

        #A frame to hold all the config widgets
        self.configs=ttk.Frame(self.new_window_cbe,name="configs",borderwidth=1)

        #This is the font_size config
        self.font_size_var=ttk.StringVar(self.new_window_cbe,"Font Size",)
        self.font_size=ttk.Entry(self.configs,textvariable=self.font_size_var,state="readonly",border=0)
        self.font_size.bind("<KeyRelease>", self.label_update)

        #This is the field to set the button text
        self.text_change_field=ttk.Entry(self.configs,textvariable=self.label_text,state="readonly",border=0)
        self.text_change_field.bind("<KeyRelease>", self.label_update)

        #This is a widget to enable or disable the border
        self.border=ttk.BooleanVar(self.new_window_cbe,True)
        self.border.trace_add("write",self.label_update)
        self.border_button=ttk.Checkbutton(self.configs,text="Border",variable=self.border,state="disabled",border=0)

        #Label colour changer
        self.foreground_colour_value=ttk.StringVar(self.new_window_cbe,"Foreground Colour")
        self.foreground_colour_entry=ttk.Entry(self.configs,textvariable=self.foreground_colour_value,state="readonly",width=25,border=0)
        self.foreground_colour_entry.bind("<KeyRelease>",self.label_update)

        self.background_colour_value=ttk.StringVar(self.new_window_cbe,"Background Colour")
        self.background_colour_entry=ttk.Entry(self.configs,textvariable=self.background_colour_value,state="readonly",width=25,border=0)
        self.background_colour_entry.bind("<KeyRelease>",self.label_update)

        #Change the labels height slash width
        self.height_value=ttk.StringVar(self.new_window_cbe,"Height")
        self.height_entry=ttk.Entry(self.configs,textvariable=self.height_value,state="readonly",border=0)
        self.height_entry.bind("<KeyRelease>",self.label_update)

        self.width_value=ttk.StringVar(self.new_window_cbe,"Width")
        self.width_entry=ttk.Entry(self.configs,textvariable=self.width_value,state="readonly",border=0)
        self.width_entry.bind("<KeyRelease>",self.label_update)

        #Label location on grid
        self.row=ttk.StringVar(self.new_window_cbe,value="Row")
        self.row_entry=ttk.Entry(self.new_window_cbe,border=0,state="readonly",textvariable=self.row)

        self.column=ttk.StringVar(self.new_window_cbe,value="Column")
        self.column_entry=ttk.Entry(self.new_window_cbe,border=0,state="readonly",textvariable=self.column)

        self.place=ttk.Button(self.new_window_cbe,text="Place",border=0,command=self.placement)

        #Sets the location of screen elements
        self.show_label.grid(column=1,row=1)
        self.show_button_script.grid(column=1,row=2)
        self.configs.grid(column=1,row=3)
        self.border_button.grid(column=1,row=2)
        self.font_size.grid(column=2,row=1)
        self.text_change_field.grid(column=2,row=2)
        self.foreground_colour_entry.grid(column=3,row=1)
        self.background_colour_entry.grid(column=3,row=2)
        self.height_entry.grid(column=4,row=1)
        self.width_entry.grid(column=4,row=2)
        self.row_entry.grid(column=1,row=100)
        self.column_entry.grid(column=1,row=101)
        self.place.grid(column=1,row=102)
        self.config_update.grid(column=1,row=499)
        ttk.Button(self.new_window_cbe,text="Close",command=self.new_window_cbe.destroy,border=0,foreground="red",activeforeground="red").grid(column=1,row=500)

class entry_creation_env:
    def __init__(self) -> None:
        pass

    def copy_script(self):
        root.clipboard_clear()
        root.clipboard_append(self.show_entry_script_text.get())

    def entry_update(self,*args):
        skip=False
        #Verifies that there are integers in the entrys that require it
        try:
            int(self.font_size.get())
            int(self.width_value.get())
        except ValueError:
            skip=True

        #Verifies that the colour are colours supported by tkinter
        try:
            root.winfo_rgb(self.background_colour_value.get())
            root.winfo_rgb(self.foreground_colour_value.get())
        except ttk.TclError:
            skip=True
        

        if skip != True:
            #Changes the boolean values in checkboxes to text
            state="normal"
            if self.status.get()==True:
                state="normal"
            elif self.status.get()==False:
                state="readonly"
            
            border=1
            if self.border.get()==True:
                border=1
            elif self.border.get()==False:
                border=0
            
            #Showcase entry
            self.show_entry.config(foreground=self.foreground_colour_value.get(),text=self.entry_text.get(), background=self.background_colour_value.get()
                                    , font=("Arial",int(self.font_size_var.get())), border=border, state=state, width=int(self.width_value.get()))
            #Button line
            self.show_entry_script_text.set(f"tkinter.Label(root, foreground=\"{self.foreground_colour_value.get()}\", background=\"{self.background_colour_value.get()}\""+
            f", text=\"{self.entry_text.get()}\", font=(\"Arial\", {int(self.font_size.get())}), state=\"{state}\", border={border}"+
            f", width={self.width_value.get()})")

    def placement(self):
        skip=False
        #Verifies that there are integers in the entrys that require it
        try:
            int(self.font_size.get())
            int(self.width_value.get())
            int(self.row.get())
            int(self.column.get())
        except ValueError:
            skip=True

        #Verifies that the colour are colours supported by tkinter
        try:
            root.winfo_rgb(self.background_colour_value.get())
            root.winfo_rgb(self.foreground_colour_value.get())
        except ttk.TclError:
            skip=True
        
        placeable=True
        for listed in stuff:
            if listed[1] == self.row.get() and listed[2] == self.column.get():
                placeable=False
                break

        if skip != True and placeable:
            
            #Changes the boolean values in checkboxes to text
            state="normal"
            if self.status.get()==True:
                state="normal"
            elif self.status.get()==False:
                state="disabled"

            border=1
            if self.border.get()==True:
                border=1
            elif self.border.get()==False:
                border=0
            

            entry=ttk.Entry(element_frame,text=self.entry_text.get() , foreground=self.foreground_colour_value.get(), background=self.background_colour_value.get()
                                    , font=("Arial",int(self.font_size_var.get())), state=state,border=border,width=int(self.width_value.get()))
            entry.grid(row=self.row.get(), column=self.column.get())
            stuff.append([entry,self.row.get(),self.column.get(),self.show_entry_script_text.get(),self.entry_text.get()])

    def edit_enable(self):

        #Enables editting and sets the default values
        self.font_size_var.set(15)
        self.entry_text_variable.set("entry_text")
        self.foreground_colour_value.set("Black")
        self.background_colour_value.set("Grey")
        self.width_value.set("10")
        self.row.set("1")
        self.column.set("1")

        self.font_size.config(state="normal")
        self.text_change_field.config(state="normal")
        self.status_button.config(state="normal")
        self.border_button.config(state="normal")
        self.foreground_colour_entry.config(state="normal")
        self.background_colour_entry.config(state="normal")
        self.width_entry.config(state="normal")
        self.row_entry.config(state="normal")
        self.column_entry.config(state="normal")
        self.config_update.destroy()

    def create_entry_env(self):
        self.new_window_cbe = ttk.Toplevel(root)
        self.new_window_cbe.title("Test")


        #Makes the entry showcase
        
        self.show_entry = ttk.Entry(self.new_window_cbe,text=self.entry_text.get(),foreground="Black",background="Grey",font=("Arial",15),border=1,width=10)
        
        self.show_entry_script_text= ttk.StringVar(self.new_window_cbe,f"tkinter.Label(root, foreground=\"Black\", background=\"Grey\""+
        f", text=\"Text\", font=(\"Arial\",15), state=\"normal\", border=1, width=10)")


        #The button that holds the entry script!
        self.show_button_script = ttk.Button(self.new_window_cbe,textvariable=self.show_entry_script_text,command=self.copy_script,border=0)

        #This button is the one to enable editing
        self.config_update = ttk.Button(self.new_window_cbe, command=self.edit_enable, text="Edit",border=0)

        #A frame to hold all the config widgets
        self.configs=ttk.Frame(self.new_window_cbe,name="configs",borderwidth=1)

        #This is the font_size config
        self.font_size_var=ttk.StringVar(self.new_window_cbe,"Font Size",)
        self.font_size=ttk.Entry(self.configs,textvariable=self.font_size_var,state="readonly",border=0)
        self.font_size.bind("<KeyRelease>", self.entry_update)

        #This is the field to set the entry textvariable
        self.entry_text=ttk.StringVar(self.new_window_cbe,value="Text")
        self.text_change_field=ttk.Entry(self.configs,textvariable=self.entry_text,state="readonly",border=0)
        self.text_change_field.bind("<KeyRelease>", self.entry_update)

        #This is a widget to change the state of the entry
        self.status=ttk.BooleanVar(self.new_window_cbe,value=True)
        self.status.trace_add("write",self.entry_update)
        self.status_button=ttk.Checkbutton(self.configs,text="Active?",variable=self.status,state="disabled",border=0)

        #This is a widget to enable or disable the border
        self.border=ttk.BooleanVar(self.new_window_cbe,True)
        self.border.trace_add("write",self.entry_update)
        self.border_button=ttk.Checkbutton(self.configs,text="Border",variable=self.border,state="disabled",border=0)

        #Label colour changer
        self.foreground_colour_value=ttk.StringVar(self.new_window_cbe,"Foreground Colour")
        self.foreground_colour_entry=ttk.Entry(self.configs,textvariable=self.foreground_colour_value,state="readonly",width=25,border=0)
        self.foreground_colour_entry.bind("<KeyRelease>",self.entry_update)

        self.background_colour_value=ttk.StringVar(self.new_window_cbe,"Background Colour")
        self.background_colour_entry=ttk.Entry(self.configs,textvariable=self.background_colour_value,state="readonly",width=25,border=0)
        self.background_colour_entry.bind("<KeyRelease>",self.entry_update)

        #Change the entrys height slash width

        self.width_value=ttk.StringVar(self.new_window_cbe,"Width")
        self.width_entry=ttk.Entry(self.configs,textvariable=self.width_value,state="readonly",border=0)
        self.width_entry.bind("<KeyRelease>",self.entry_update)

        #Button location on grid
        self.row=ttk.StringVar(self.new_window_cbe,value="Row")
        self.row_entry=ttk.Entry(self.new_window_cbe,border=0,state="readonly",textvariable=self.row)

        self.column=ttk.StringVar(self.new_window_cbe,value="Column")
        self.column_entry=ttk.Entry(self.new_window_cbe,border=0,state="readonly",textvariable=self.column)

        self.place=ttk.Button(self.new_window_cbe,text="Place",border=0,command=self.placement)

        #Sets the location of screen elements
        self.show_entry.grid(column=1,row=1)
        self.show_button_script.grid(column=1,row=2)
        self.configs.grid(column=1,row=3)
        self.status_button.grid(column=1,row=1)
        self.border_button.grid(column=1,row=2)
        self.font_size.grid(column=2,row=1)
        self.text_change_field.grid(column=2,row=2)
        self.foreground_colour_entry.grid(column=3,row=1)
        self.background_colour_entry.grid(column=3,row=2)
        self.width_entry.grid(column=4,row=2)
        self.row_entry.grid(column=1,row=100)
        self.column_entry.grid(column=1,row=101)
        self.place.grid(column=1,row=102)
        self.config_update.grid(column=1,row=499)
        ttk.Button(self.new_window_cbe,text="Close",command=self.new_window_cbe.destroy,border=0,foreground="red",activeforeground="red").grid(column=1,row=500)


button_env=button_creation_env()
label_env=label_creation_env()
entry_env=entry_creation_env()

def creator_window_opener():
    global creator_window; creator_window= ttk.Toplevel(root)

    create_button=ttk.Button(creator_window,text="Button Creator.",command= lambda: creator_window_continue(1), font=("Arial", 20), state="normal", border=0, height=1, width=13,foreground="White", background="Light blue", activeforeground="Light Green", activebackground="Light blue",)
    create_button.grid(column=1,row=1,padx=10,pady=10)

    create_label=ttk.Button(creator_window,text="Label Creator.",command= lambda: creator_window_continue(2), font=("Arial", 20), state="normal", border=0, height=1, width=13,foreground="White", background="Light blue", activeforeground="Light Green", activebackground="Light blue",)
    create_label.grid(column=2,row=1,padx=10,pady=10)

    create_entry=ttk.Button(creator_window,text="Entry Creator.",command= lambda: creator_window_continue(3), font=("Arial", 20), state="normal", border=0, height=1, width=13,foreground="White", background="Light blue", activeforeground="Light Green", activebackground="Light blue",)
    create_entry.grid(column=3,row=1,padx=10,pady=10)

def creator_window_continue(id=0):
    creator_window.destroy()

    if id==0:
        print("You didnt fill in the id!!")
    elif id==1:
        button_env.create_button_env()
    elif id==2:
        label_env.create_label_env()
    elif id==3:
        entry_env.create_entry_env()

def remove_widget(row,column):
    def recall(button_call,button_text,top):
        button_call.configure(text=button_text)
        top.destroy()

    def remove(top,listed):
        stuff.remove(listed)
        button.destroy()
        top.destroy()

    for listed in stuff:
            if listed[1] == row.get() and listed[2] == column.get() and listed[3] != "HardCoded":
                button=listed[0]
                button.configure(text="DELETE?")
                top=ttk.Toplevel(root)
                delete=ttk.Button(top, command=lambda : remove(top,listed), foreground="Red", background="White", activeforeground="White", activebackground="Red", text="Confirm Delete?", font=("Arial", 15), state="normal", border=0, height=10, width=25)
                delete.pack()
                restore=ttk.Button(top, command=lambda: recall(button, listed[4], top), foreground="Green", background="White", activeforeground="White", activebackground="Light Green", text="Restore?", font=("Arial", 15), state="normal", border=1, height=10, width=25)
                restore.pack()
                break

def script_builder():
    window=ttk.Toplevel(root)
    script=ttk.StringVar(window,value="")
    script_label=ttk.Label(window, foreground="Black", background="Grey", textvariable=script, font=("Arial", 10), border=0)
    script_label.grid(row=1,column=2)
    def copier():
        root.clipboard_clear()
        root.clipboard_append(script.get())
    copy_button=ttk.Button(window,command=copier,border=0,text="Copy",foreground="White", background="Light Blue", activeforeground="Light Green", activebackground="Light blue")
    run=0
    for element in stuff:
        if element[3]!="HardCoded":
            run+=1
            script.set(script.get()+f"element{run} = "+element[3]+"\n"+f"element{run}.grid(row={element[1]},column={element[2]})\n")
    
    pass

create_window_button=ttk.Button(root,text="Add", foreground="White", background="Light Blue", activeforeground="Light Green", activebackground="Light blue",command=creator_window_opener,border=0)
create_window_button.grid(column=2,row=1111)

remove_config=ttk.Frame(root)
remove_config.grid(column=2,row=1113)

row_label=ttk.Label(remove_config,text="row",border=0)
row_label.grid(row=1,column=1)

column_label=ttk.Label(remove_config,text="column",border=0)
column_label.grid(row=2,column=1)

row_data=ttk.Entry(remove_config,text="",border=0)
row_data.grid(row=1,column=2)

column_data=ttk.Entry(remove_config,text="",border=0)
column_data.grid(row=2,column=2)

remove_button=ttk.Button(root,text="Remove", foreground="Red", background="Light Blue", activeforeground="Red", activebackground="Light blue",command=lambda: remove_widget(row_data,column_data),border=0)
remove_button.grid(column=2,row=1112)

welcome_text=ttk.Label(root, foreground="White", background="Light Blue", text="Welcome to a tkinter graphical designer", font=("Arial", 15), border=0, height=3, width=35)
welcome_text.grid(row=0,column=2)

full_script=ttk.Button(root,command=script_builder,foreground="White",background="Light Blue",activeforeground="Light Green",text="View code",border=0,activebackground="Light Blue")
full_script.grid(row=1114,column=2)

element_frame=ttk.Frame(root,border=0)
element_frame.grid(row=1,column=2)



global stuff; stuff=[[welcome_text,"0","2","HardCoded"],[create_window_button,"1111","2","HardCoded"],
                     [remove_button,"1112","2","HardCoded"],[remove_config,"1113","2","HardCoded"],[full_script,"1114","2","HardCoded"]]

root.mainloop()