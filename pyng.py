
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


from rembg import remove

root = Tk()
root.title("Pyng")
root.resizable(False,False)
#root.wm_iconbitmap("pyng.ico")
miFrame = Frame(root)
miFrame.config(width=1600,height=1300)
miFrame.pack()
inputPath = StringVar
outputPath = StringVar



inputPath = ""
outputPath = ""

def inputSelectFile():
    global inputPath
    inputPath = filedialog.askopenfilename(title="Open Photo", initialdir="/", filetypes=(("PNG FILE", "*.png"), ("JPG FILE", "*.jpg"), ("All files", "*.*")))
    inputSelectedLabel.config(text="✅")


def outputSelectFile():
    global outputPath
    outputPath = filedialog.asksaveasfilename(initialdir="/", title="Save as", filetypes=(("PNG FILE", "*.png"), ("All files", "*.*")))
    outputSelectedLabel.config(text="✅")

def start():
    global inputPath
    global outputPath
    if inputPath == "" or outputPath == "":
        messagebox.showwarning("Warning","Please select intput and output files properly")
        outputSelectedLabel.config(text="❌")
        inputSelectedLabel.config(text="❌")
        inputPath = ""
        outputPath= ""
        return
    else:
        try:
           
            outputPath +=".png"
            with open(inputPath,'rb') as i:
                with open(outputPath,'wb') as o:
                    input = i.read()
                    output = remove(input)
                    o.write(output)
            messagebox.showinfo("Succes","Work release, file correctly saved in")

            outputSelectedLabel.config(text="❌")
            inputSelectedLabel.config(text="❌")
            inputPath = ""
            outputPath= ""
        except:
            messagebox.showerror("Error","File formats are not properly!")
            root.destroy()


inputLabel = Label(miFrame)
inputLabel.config(text="Input image:")
outputLabel = Label(miFrame)
outputLabel.config(text="Output image:")
inputSelectedLabel = Label(miFrame)
outputSelectedLabel = Label(miFrame)



inputButton = Button(miFrame)
outputButton = Button(miFrame)
startButton = Button(miFrame)

inputLabel.grid(row=0,column=0)
outputLabel.grid(row=0,column=2)

inputButton.config(text="Select Input file",command=inputSelectFile)
outputButton.config(text="Select Output rute",command=outputSelectFile)
outputSelectedLabel.config(text="❌")
inputSelectedLabel.config(text="❌")
startButton.config(text="Start!",command=start, border=0.5)
inputButton.grid(row=2,column=0,pady=10,padx=10)
outputButton.grid(row=2,column=2,pady=10,padx=10)
startButton.grid(row=3,column=1,pady=10,padx=10)
inputSelectedLabel.grid(row=3,column=0,pady=10,padx=10)
outputSelectedLabel.grid(row=3,column=2,pady=10,padx=10)





'''
im = cv2.imread("imagen.jpg")
cv2.imwrite("imagen.png", im)


input_path = "test.png"
output_path = "output.png"

with open(input_path,'rb') as i:
    with open(output_path,'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)
'''
root.mainloop()
