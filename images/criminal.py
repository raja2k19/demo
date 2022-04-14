from msilib.schema import tables
import plistlib
from tkinter import*
from tkinter import ttk
from tkinter.tix import COLUMN
from turtle import width
from xml.etree.ElementTree import PI
from PIL import Image,ImageTk


class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1600x900+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')



        #create head (Lable for the the heading............)

        lbl_title=Label(self.root,text='CHILDREN CRIMINAL MANAGEMENT SYSTEM',font=('comic sans ms bold',40,'bold'),bg='black',fg='teal')
        lbl_title.place(x=0,y=0,width=1600,height=80)



        #crete logo(set a logo for the heading ,height for the upper part and width for the heading.............)

        img_logo=Image.open('images/toplogo.jpg')
        img_logo=img_logo.resize((60,60),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=120,y=0,width=40,height=60)


        #img_frame

        img_frame=Frame(self.root,bd=4,relief=RIDGE,bg='Green')
        img_frame.place(x=0,y=70,width=1600,height=160)


        #img1

        img_1=Image.open('images/img1.jpg')
        img_1=img_1.resize((540,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img_1)

        self.img_A=Label(img_frame,image=self.photo1)
        self.img_A.place(x=0,y=0,width=540,height=160)

        #img2
        img2=Image.open('images/img2.jpg')
        img2=img2.resize((540,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)

        self.img_A=Label(img_frame,image=self.photo2)
        self.img_A.place(x=540,y=0,width=540,height=160)

        #img3
        img3=Image.open('images/img3.jpg')
        img3=img3.resize((540,160),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img3)

        self.img_A=Label(img_frame,image=self.photo3)
        self.img_A.place(x=1080,y=0,width=540,height=160)


        #main frame

        Main_frame=Frame(self.root,bd=4,relief=RIDGE,bg='light blue')
        Main_frame.place(x=10,y=215,width=1590,height=570)
    


        #upper frame

        upper_frame=LabelFrame(Main_frame,bd=4,relief=RIDGE,text='CRIMINAL INFORMATION',font=('comic sans ms bold',11,'bold'),bg='white',fg='red')
        upper_frame.place(x=10,y=10,width=1540,height=280)

        ##Labels Entry


        ##case id

        case_id=Label(upper_frame,font=('times new roman',12,'bold'),text='Case id:',bg='white')
        case_id.grid(row=0,column=0,sticky=W,padx=2,pady=7,)

        caseentry=ttk.Entry(upper_frame,width=22,font=('arial',11,"bold"))
        caseentry.grid(row=0,column=1,padx=2,pady=7,sticky=W)


        ##Criminal No:(form)

        lbl_criminal_no=Label(upper_frame,font=('times new roman',12,'bold'),text='Criminal no:',bg='white')
        lbl_criminal_no.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_criminal=ttk.Entry(upper_frame,width=22,font=('arial',11,"bold"))
        txt_criminal.grid(row=0,column=3,padx=2,sticky=W,pady=7)


        ##criminal name:
        lbl_name=Label(upper_frame,font=("times new roman'",12,"bold"),text="Name:",bg="white")
        lbl_name.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_name=ttk.Entry(upper_frame,width=22,font=("arial",11,"bold"))
        txt_name.grid(row=1,column=1,sticky=W,padx=2,pady=7)


        ##criminal nick name:
        lbl_nickname=Label(upper_frame,font=("times new roman'",12,"bold"),text="Nick name:",bg="white")
        lbl_nickname.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_nickname=ttk.Entry(upper_frame,width=22,font=("arial",11,"bold"))
        txt_nickname.grid(row=1,column=3,padx=2,pady=7)


        ##Arrest Date:
        lbl_arrest=Label(upper_frame,font=("times new roman'",12,"bold"),text="Arrest date:",bg="white")
        lbl_arrest.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_arrest=ttk.Entry(upper_frame,width=22,font=("arial",11,"bold"))
        txt_arrest.grid(row=2,column=1,padx=2,pady=7)


        ##date of crime:
        lbl_datecrime=Label(upper_frame,font=("times new roman'",12,"bold"),text="Date of crime:",bg="white")
        lbl_datecrime.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        txt_datecrime=ttk.Entry(upper_frame,width=22,font=("arial",11,"bold"))
        txt_datecrime.grid(row=2,column=3,padx=2,pady=7)


        ##address:
        lbl_address=Label(upper_frame,font=("times new roman'",12,"bold"),text="Address:",bg="white")
        lbl_address.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_address=ttk.Entry(upper_frame,width=22,font=("arial",11,"bold"))
        txt_address.grid(row=3,column=1,padx=2,pady=7)


        ##age:
        lbl_age=Label(upper_frame,font=("times new roman'",12,"bold"),text="Age:",bg="white")
        lbl_age.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_age=ttk.Entry(upper_frame,width=22,font=("arial",11,"bold"))
        txt_age.grid(row=3,column=3,padx=2,pady=7)



        ##accupution:
        lbl_accupation=Label(upper_frame,font=("times new roman'",12,"bold"),text="Accupution:",bg="white")
        lbl_accupation.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_accupation=ttk.Entry(upper_frame,width=22,font=("arial",11,"bold"))
        txt_accupation.grid(row=4,column=1,padx=2,pady=7)



        ##birthmark:
        lbl_birthmark=Label(upper_frame,font=("times new roman'",12,"bold"),text="Birthmark:",bg="white")
        lbl_birthmark.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        txt_birthmark=ttk.Entry(upper_frame,width=22,font=("arial",11,"bold"))
        txt_birthmark.grid(row=4,column=3,padx=2,pady=7)



        ##crime type:
        lbl_crimetype=Label(upper_frame,font=("times new roman'",12,"bold"),text="crime type:",bg="white")
        lbl_crimetype.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_crimetype=ttk.Entry(upper_frame,width=22,font=("arial",11,"bold"))
        txt_crimetype.grid(row=0,column=5,padx=2,pady=7)



        ##father name:
        lbl_father=Label(upper_frame,font=("times new roman'",12,"bold"),text="father name:",bg="white")
        lbl_father.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_father=ttk.Entry(upper_frame,width=22,font=("arial",11,"bold"))
        txt_father.grid(row=1,column=5,padx=2,pady=7)



        ##Gender:    
        frame_gender=Label(upper_frame,font=("times new roman'",12,"bold"),text="Gender",bg="white")
        frame_gender.grid(row=2,column=4,sticky=W,padx=2,pady=7)

        ###Radio Button Gender
        radio_frame_gender=Frame(upper_frame,bd=3,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=700,y=90,width=190,height=28)

        male=Radiobutton(radio_frame_gender,text="male",value="male",font=("times new roman'",8,"bold"),bg="white")
        male.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        female=Radiobutton(radio_frame_gender,text="female",value="female",font=("times new roman'",8,"bold"),bg="white")
        female.grid(row=0,column=1,pady=2,padx=5,sticky=W)



     
        ##wanted:
        frame_wanted=Label(upper_frame,font=("arial",12,"bold"),text="most wanted",bg="white")
        frame_wanted.grid(row=3,column=4,sticky=W,padx=2,pady=7)

        ###Radio Button wanted

        radio_frame_wanted=Frame(upper_frame,bd=3,relief=RIDGE,bg='white')
        radio_frame_wanted.place(x=700,y=120,width=190,height=28)

        yes=Radiobutton(radio_frame_wanted,text="yes",value="yes",font=("times new roman'",8,"bold"),bg="white")
        yes.grid(row=0,column=0,pady=2,padx=5,sticky=W)
        no=Radiobutton(radio_frame_wanted,text="no",value="no",font=("times new roman'",8,"bold"),bg="white")
        no.grid(row=0,column=1,pady=2,padx=5,sticky=W)




        #Buttons
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=5,y=200,width=630,height=50)
        
        ##add button
        button_add=Button(button_frame,text="Record Save",font=("arial'",13,"bold"),bg="light blue",fg='white',width=14)
        button_add.grid(row=0,column=0,padx=3,pady=5)


        ##update add button
        button_update=Button(button_frame,text="update",font=("arial'",13,"bold"),bg="green",fg='white',width=14)
        button_update.grid(row=0,column=1,padx=3,pady=5)

        ##Delete add button
        button_delete=Button(button_frame,text="Delete",font=("arial'",13,"bold"),bg="red",fg='white',width=14)
        button_delete.grid(row=0,column=2,padx=3,pady=5)

        ##clear button
        button_clear=Button(button_frame,text="clear",font=("arial'",13,"bold"),bg="teal",fg='white',width=14)
        button_clear.grid(row=0,column=3,padx=3,pady=5)


        #background right side image:
        img_4=Image.open('images/img4.jpg')
        img_4=img_4.resize((480,255),Image.ANTIALIAS)
        self.photo4=ImageTk.PhotoImage(img_4)

        self.img_D=Label(Main_frame,image=self.photo4)
        self.img_D.place(x=1000,y=30,width=440,height=240)



    

        #down frame
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='CRIMINAL INFORMATION TABLE',font=('comic sans ms bold',11,'bold'),bg='GRAY',fg='magenta')
        down_frame.place(x=10,y=300,width=1540,height=270)

        #search_frame_frame
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='SEARCH CRIMIANAL RECORD',font=('arial',11,'bold'),bg='white',fg='red')
        search_frame.place(x=0,y=0,width=1470,height=50)

        search_by=Label(search_frame,font=('arial',11,'bold'),text='SEARCH BY',bg='GREEN',fg='red')
        search_by.grid(row=0,column=0,padx=5,sticky=W)

        #combobox create

        
        combo_search_box=ttk.Combobox(search_frame,font=("arial",11,"bold"),width=18,state='read')
        combo_search_box['value']=('Select Option','Case_id','Criminal_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)

        search_txt=ttk.Entry(search_frame,width=18,font=("arial",11,"bold"))
        search_txt.grid(row=0,column=2,padx=5,sticky=W)
        



if __name__=="__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()

      