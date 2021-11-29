##############################################################################
#script to create virtual environment and install the dependent packages in it.
#created by Nitesh (23-10-2021)
##############################################################################

import subprocess
from tkinter import *
import tkinter.messagebox

packages_list = []

##############################################################
#creation of functions for different actions to be implemented
##############################################################

#creating the virtual environment
def create():
    if virtual_env_name.get() == '':
        tkinter.messagebox.showinfo("Invalid Request", "Please Enter A Valid Name ✘")
    else:
        virtualenv_name = virtual_env_name.get()
        command_to_create_virtualenv = f"cmd /c virtualenv C:/{virtualenv_name}"
        subprocess.run(command_to_create_virtualenv)
        tkinter.messagebox.showinfo("Success", "Virtual Environment Created Successfully ✓")    

#adding the package list
def addpackages():
    if packages_name.get() == '':
        tkinter.messagebox.showinfo("Invalid Request", "Please Enter A Valid Library Name ✘")
        Label(root,text='Invalid Input ✘',bg='#1c87d9',fg='#ff0505').grid(row=4,column=0,columnspan=2,sticky=EW,padx=8,pady=8)
    elif packages_name.get() in packages_list:
        tkinter.messagebox.showinfo("Invalid Request", "Library Already Exists ✘")
        Label(root,text='Library Alreay Exists !!!',bg='#1c87d9',fg='yellow').grid(row=4,column=0,columnspan=2,sticky=EW,padx=8,pady=8)
    else:
        package_name = packages_name.get()  
        packages_list.append(package_name)
        Label(root,text='Library Added Successfully ✓',bg='#1c87d9',fg='#51ff00').grid(row=4,column=0,columnspan=2,sticky=EW,padx=8,pady=8)

#creation of requirements file
def create_requirement_file():
    if packages_list == []:
        tkinter.messagebox.showinfo("Invalid Request", "Library List Is Empty ✘")
        Label(root,text='Invalid Input ✘',bg='#1c87d9',fg='#ff0505').grid(row=4,column=0,columnspan=2,sticky=EW,padx=8,pady=8)
    else:
        new_list = packages_list 
        with open('C:/Users/nites/requirements.txt','w') as f:
            for item in new_list:
                f.write(item)
                f.write('\n')
        tkinter.messagebox.showinfo("Success","Library List Created Successfully ✓")
        Label(root,text='Requirement Created Successfully ✓',bg='#1c87d9',fg='#51ff00').grid(row=4,column=0,columnspan=2,sticky=EW,padx=8,pady=8)
        
#installing the package dependencies w.r.t to requirements.txt file
def installpackages():
    if virtual_env_name.get() == '':
        tkinter.messagebox.showinfo("Invalid Request", "Create A Virtual Environment To Install Libraries ✘")
        Label(root,text='Invalid Request ✘',bg='#1c87d9',fg='#ff0505').grid(row=6,column=0,columnspan=2,sticky=EW,padx=8,pady=8)
    else:
        virtualenv_name = virtual_env_name.get() 
        activation_command = f"cmd /c cd C:/{virtualenv_name}/Scripts && activate && pip install -r C:/Users/nites/requirements.txt"
        subprocess.run(activation_command)
        tkinter.messagebox.showinfo("Success","All Libraries Are Installed Successfully ✓")
        Label(root,text='Libraries Installed Successfully ✓',bg='#1c87d9',fg='#51ff00').grid(row=6,column=0,columnspan=2,sticky=EW,padx=8,pady=8)

#action to exit the application
def exit():
    root.destroy()

####################################
#creating the GUI of the Application
####################################

root = Tk()
root.title('Virtual Environment Utility Tool')
root.geometry("535x325")
root.configure(bg='#1c87d9')

virtual_env_name = StringVar()
packages_name = StringVar()

#gui for creation of virtual environment
Label(root,text='Create Virtual Environment',bg = "black",fg='white',padx=5).grid(row=0,sticky=EW,columnspan=3,pady=8,padx=8)
Label(root,text='VirtualEnv:').grid(row=1,column=0,padx=8,pady=8)
Entry(root, bd=5,textvariable=virtual_env_name,width=35).grid(row=1,column=1,pady=8,padx=8)
Button(root,text='Create',width=25,command=create).grid(row=1,column=2,padx=8,pady=8)

#gui for creation of requirement file
Label(root,text='Create Requirement File',bg = "black",fg='white',padx=5).grid(row=2,sticky=EW,columnspan=3,pady=8,padx=8)
Label(root,text='Add Libraries:').grid(row=3,column=0,padx=8,pady=8)
Entry(root,bd=5,textvariable=packages_name,width=35).grid(row=3,column=1,pady=8,padx=8)
Button(root,text='Add Library',width=25,command=addpackages).grid(row=3,column=2,pady=8,padx=8)
Button(root,text='Create File',width=25,command=create_requirement_file).grid(row=4,column=2,pady=8,padx=8)

#gui for creation of installing the libraries from the requirement file
Label(root,text='Install Libraries',bg = "black",fg='white',padx=5).grid(row=5,sticky=EW,columnspan=3,pady=8,padx=8)
Button(root,text='Install',width=25,command=installpackages).grid(row=6,column=2,pady=8,padx=8)

Button(root,text='Exit',width=25,command=exit).grid(row=7,column=2,pady=8,padx=8)

root.mainloop()