import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

#from tkinter import *
window = tk.Tk()

window.title("Image painting")
window.geometry('1200x800')

#header
header = tk.Label(window, text="GET YOUR IMAGE PAINTED HERE!", bg="red", fg="black" ,font=("none bold",35), anchor="n") 
#anchor=n for top-central justification
header.place(x=300,y=1)
#header.pack()

#left frame
left_frame = tk.Frame(window, width=400, height=400, highlightbackground="black", highlightthickness=1)
left_frame.place(x=40,y=150)
left_frame.pack_propagate(0)


#left label
left_label = tk.Label(window, text="Input Image", font=("none Bold",20))
left_label.place(x=200,y=120)


#rigt_frame
rigt_frame = tk.Frame(window, width=400, height=400, highlightbackground="black", highlightthickness=1)
rigt_frame.place(x=760,y=150)
rigt_frame.pack_propagate(0)


#right label
right_label = tk.Label(window, text="Output Image", font=("none Bold",20))
right_label.place(x=930,y=120)



class variables:
    img = ""
    inp_img = ""
    out_img = ""

    #left image label
    inp_image = tk.Label(left_frame, text="Input Image", font=("none Bold",10))
    inp_image.pack()

    #right image label
    out_image = tk.Label(rigt_frame, text="Output Image", font=("none Bold",10))
    out_image.pack()

def working_design():
    #image selection button
    img_selection_btn = tk.Button(window, text="Select Image", fg="black", font=("none Bold",20) , command=open_file)
    img_selection_btn.place(x=520, y=100)
    #*--------------------------------
    # #Oil painting button
    img_sketching_btn = tk.Button(window, text="Oil Painting", fg="black", font=("none Bold",20) , command=Oil_painting)
    img_sketching_btn.place(x=520, y=200)
    #*--------------------------------
    # #Water colour button
    img_sketching_btn = tk.Button(window, text="Water Colour Painting", fg="black", font=("none Bold",20) , command=Water_colour_painting)
    img_sketching_btn.place(x=440, y=250)
    #*--------------------------------
    # #Pencil sketch button
    img_sketching_btn = tk.Button(window, text="Pencil Sketch", fg="black", font=("none Bold",20) , command=Pencil_sketch)
    img_sketching_btn.place(x=520, y=300)


def open_file(): 
    filename = filedialog.askopenfilename(filetypes=(("JPEG","*.jpg"),("PNG","*.png"),("All Files","*.*"))) 

    if filename!="" :
        variables.img = cv2.imread(filename)
        #resizing for image display
        variables.inp_img = resize_img(variables.img)
        #Rearranging the color channel
        b,g,r = cv2.split(variables.inp_img)
        img = cv2.merge((r,g,b))

        #convert image object into TkPhoto object
        im = Image.fromarray(img)
        img1 = ImageTk.PhotoImage(image=im)

        variables.inp_image.pack_forget()
        left_frame.update()

        variables.inp_image = tk.Label(left_frame, image=img1)
        variables.inp_image.image = img1
        variables.inp_image.pack()
        left_frame.update()

def resize_img(img):
    
    img1 = cv2.resize(img,(400,400)) #(a high-quality downsampling filter)       
    return img1

def Oil_painting():
    img_rgb = variables.img
    img = cv2.xphoto.oilPainting(img_rgb, 7, 1)

    #resizing for image display
    variables.out_img = resize_img(img)
    #Rearranging the color channel
    b,g,r = cv2.split(variables.out_img)
    img = cv2.merge((r,g,b))
    #convert image object into TkPhoto object
    im = Image.fromarray(img)
    img1 = ImageTk.PhotoImage(image=im)
    
    variables.out_image.pack_forget()
    rigt_frame.update()

    variables.out_image = tk.Label(rigt_frame, image=img1)
    variables.out_image.image = img1
    variables.out_image.pack()
    rigt_frame.update()

def Water_colour_painting():
    img_rgb = variables.img
    img = cv2.stylization(img_rgb, sigma_s=60, sigma_r=0.6)
    # sigma_s controls the size of the neighborhood. Range 1 - 200
    # # sigma_r controls the how dissimilar colors within the neighborhood will be averaged. 
    # A larger sigma_r results in large regions of constant color. Range 0 - 1

    #resizing for image display
    variables.out_img = resize_img(img)
    #Rearranging the color channel
    b,g,r = cv2.split(variables.out_img)
    img = cv2.merge((r,g,b))
    #convert image object into TkPhoto object
    im = Image.fromarray(img)
    img1 = ImageTk.PhotoImage(image=im)
    
    variables.out_image.pack_forget()
    rigt_frame.update()

    variables.out_image = tk.Label(rigt_frame, image=img1)
    variables.out_image.image = img1
    variables.out_image.pack()
    rigt_frame.update()

def Pencil_sketch():
    img_rgb = variables.img
    img, img1 = cv2.pencilSketch(img_rgb, sigma_s=60, sigma_r=0.07, shade_factor=0.05) 

    # sigma_s and sigma_r are the same as in stylization.
    # # shade_factor is a simple scaling of the output image intensity. 
    # The higher the value, the brighter is the result. Range 0 - 0.1

    #resizing for image display
    variables.out_img = resize_img(img)
    # #Rearranging the color channel
    # b,g,r = cv2.split(variables.out_img)
    # img = cv2.merge((r,g,b))
    #convert image object into TkPhoto object
    im = Image.fromarray(variables.out_img)
    img1 = ImageTk.PhotoImage(image=im)
    
    variables.out_image.pack_forget()
    rigt_frame.update()

    variables.out_image = tk.Label(rigt_frame, image=img1)
    variables.out_image.image = img1
    variables.out_image.pack()
    rigt_frame.update()


working_design()

window.mainloop()

