from tkinter import *
from flask import Flask,redirect, url_for,render_template,request
import os

def d_dtcn():
	root = Tk()
	root.configure(background = "white")

	def function1(): 
		os.system("python video.py")
		exit()

	
		
	root.title("REAL TIME 3D POSE CLASSIFICATION ")
	Label(root, text="REAL TIME 3D POSE CLASSIFICATION",font=("times new roman",20),fg="black",bg="aqua",height=2).grid(row=2,rowspan=2,columnspan=5,sticky=N+E+W+S,padx=5,pady=10)
	Button(root,text="Run using web cam",font=("times new roman",20),bg="#0D47A1",fg='white',command=function1).grid(row=5,columnspan=5,sticky=W+E+N+S,padx=5,pady=5)
	
	root.mainloop()