from tkinter import *
import math,random,os
from tkinter import messagebox
class Bill_App:
	def __init__(self,root):
	   self.root=root
	   self.root.geometry("1350x700")
	   self.root.title("Billing Software")
	   title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,font=("Arial",30,"bold"),bg="Dark blue",fg="yellow",pady=2).pack(fill=X)

	   #==========Variables===============
	   #==========Cosmetics==============
	   self.soap=IntVar()
	   self.face_cream=IntVar()
	   self.face_wash=IntVar()
	   self.spray=IntVar()
	   self.gel=IntVar()
	   self.lotion=IntVar()
	   #===========Groceries============
	   self.rice=IntVar()
	   self.food_oil=IntVar()
	   self.pulses=IntVar()
	   self.flour=IntVar()
	   self.sugar=IntVar()
	   self.tea=IntVar()
	   #==========cold drinks===========
	   self.pepsi=IntVar()
	   self.dew=IntVar()
	   self.coke=IntVar()
	   self.limca=IntVar()
	   self.maaza=IntVar()
	   self.sprite=IntVar()
	   #===========total product price & tax vaiables====
	   self.cosmetic_price=StringVar()
	   self.grocery_price=StringVar()
	   self.cold_drink_price=StringVar()

	   self.cosmetic_tax=StringVar()
	   self.grocery_tax=StringVar()
	   self.cold_drink_tax=StringVar()

	   #=========Customer============
	   self.c_name=StringVar()
	   self.c_phon=StringVar()
	   self.bill_no=StringVar()
	   x=random.randint(1000,9999)
	   self.bill_no.set(str(x))
	   self.search_bill=StringVar()





	   #=======Customer details frame============


	   F1=LabelFrame(self.root,text="Customer Details",font=("times new roman",15,"bold"),bg="Dark blue",fg="yellow")
	   F1.place(x=0,y=80,relwidth=1)
	   

	   cname_lbl=Label(F1,text="Customer Name",bg="Dark blue",fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
	   cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="Arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

	   cphn_lbl=Label(F1,text="Phone No.",bg="Dark blue",fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
	   cphn_txt=Entry(F1,width=15,textvariable=self.c_phon,font="Arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

	   c_bill_lbl=Label(F1,text="Bill Number",bg="Dark blue",fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
	   c_bill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="Arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

	   bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="Arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

	   F2=LabelFrame(self.root,text="Cosmetics",bd=10,relief=GROOVE,font=("Arial",15,"bold"),bg="Dark blue",fg="yellow",pady=2)
	   F2.place(x=5,y=170,width=325,height=380)
	   bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg="Dark blue",fg="light green").grid(row=0,column=0,padx=10,pady=10)
	   bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

	   Face_cream_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg="Dark blue",fg="light green").grid(row=1,column=0,padx=10,pady=10)
	   Face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

	   Face_w_lbl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg="Dark blue",fg="light green").grid(row=2,column=0,padx=10,pady=10)
	   Face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

	   Hair_s_lbl=Label(F2,text="Hair Spray",font=("times new roman",16,"bold"),bg="Dark Blue",fg="light green").grid(row=3,column=0,padx=10,pady=10)
	   Hair_s_txt=Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

	   Hair_g_lbl=Label(F2,text="Hair Gel",font=("times new roman",16,"bold"),bg="Dark blue",fg="light green").grid(row=4,column=0,padx=10,pady=10)
	   Hair_g_txt=Entry(F2,width=10,textvariable=self.gel,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

	   Body_lbl=Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),bg="Dark blue",fg="light green").grid(row=5,column=0,padx=10,pady=10)
	   Body_txt=Entry(F2,width=10,textvariable=self.lotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

	   #===================Grocery Frame==============

	   F3=LabelFrame(self.root,text="Groceries",bd=10,relief=GROOVE,font=("Arial",15,"bold"),bg="Dark blue",fg="yellow",pady=2)
	   F3.place(x=340,y=170,width=325,height=380)

	   g1_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg="Dark blue",fg="light green").grid(row=0,column=0,padx=10,pady=10)
	   g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

	   g2_lbl=Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg="Dark blue",fg="light green").grid(row=1,column=0,padx=10,pady=10)
	   g2_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

	   g3_lbl=Label(F3,text="Pulses",font=("times new roman",16,"bold"),bg="Dark blue",fg="light green").grid(row=2,column=0,padx=10,pady=10)
	   g3_txt=Entry(F3,width=10,textvariable=self.pulses,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

	   g4_lbl=Label(F3,text="Flour",font=("times new roman",16,"bold"),bg="Dark blue",fg="light green").grid(row=3,column=0,padx=10,pady=10)
	   g4_txt=Entry(F3,width=10,textvariable=self.flour,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

	   g5_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg="Dark blue",fg="light green").grid(row=4,column=0,padx=10,pady=10)
	   g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

	   g6_lbl=Label(F3,text="Tea",font=("times new roman",16,"bold"),bg="Dark blue",fg="light green").grid(row=5,column=0,padx=10,pady=10)
	   g6_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

	   #===============Cold drink frame======

	   F4=LabelFrame(self.root,text="Cold Drinks",bd=10,relief=GROOVE,font=("Arial",15,"bold"),bg="Dark blue",fg="yellow",pady=2)
	   F4.place(x=670,y=170,width=325,height=380)

	   c1_lbl=Label(F4,text="Pepsi",font=("times new roman",16,"bold"),bg="Dark blue",fg="light green").grid(row=0,column=0,padx=10,pady=10)
	   c1_txt=Entry(F4,width=10,textvariable=self.pepsi,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

	   c2_lbl=Label(F4,text="Dew",font=("times new roman",16,"bold"),bg="Dark blue",fg="light green").grid(row=1,column=0,padx=10,pady=10)
	   c2_txt=Entry(F4,width=10,textvariable=self.dew,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

	   c3_lbl=Label(F4,text="Coke",font=("times new roman",16,"bold"),bg="Dark blue",fg="light green").grid(row=2,column=0,padx=10,pady=10)
	   c3_txt=Entry(F4,width=10,textvariable=self.coke,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

	   c4_lbl=Label(F4,text="Limca",font=("times new roman",16,"bold"),bg="Dark blue",fg="light green").grid(row=3,column=0,padx=10,pady=10)
	   c4_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

	   c5_lbl=Label(F4,text="Maaza",font=("times new roman",16,"bold"),bg="Dark blue",fg="light green").grid(row=4,column=0,padx=10,pady=10)
	   c5_txt=Entry(F4,width=10,textvariable=self.maaza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

	   c6_lbl=Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg="Dark blue",fg="light green").grid(row=5,column=0,padx=10,pady=10)
	   c6_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

	   #===========Bill Area===========
	   F5=Frame(self.root,bd=10,relief=GROOVE)
	   F5.place(x=1010,y=170,width=350,height=380)
	   bill_title=Label(F5,text="Bill Area",font="Arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
	   scrol_y=Scrollbar(F5,orient=VERTICAL)
	   self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
	   scrol_y.pack(side=RIGHT,fill=Y)
	   scrol_y.config(command=self.txtarea.yview)
	   self.txtarea.pack(fill=BOTH,expand=1)

	   #=======Button Frame==========

	   F6=LabelFrame(self.root,text="Bill Menu",bd=10,relief=GROOVE,font=("Arial",15,"bold"),bg="Dark Blue",fg="yellow",pady=2)
	   F6.place(x=0,y=560,relwidth=1,height=140)
	   m1=Label(F6,text="Total Cosmetics Price",bg="Dark blue",fg="yellow",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
	   m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="Arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

	   m2=Label(F6,text="Total Groceries Price",bg="Dark blue",fg="yellow",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
	   m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="Arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

	   m3=Label(F6,text="Total Cold Drinks Price",bg="Dark blue",fg="yellow",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
	   m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font="Arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

	   c1=Label(F6,text="Cosmetics Tax",bg="Dark blue",fg="yellow",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
	   c1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font="Arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

	   c2=Label(F6,text="Groceries Tax",bg="Dark blue",fg="yellow",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
	   c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font="Arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

	   c3=Label(F6,text="Cold Drinks Tax",bg="Dark blue",fg="yellow",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
	   c3_txt=Entry(F6,width=18,textvariable=self.cold_drink_tax,font="Arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)
	   btn_F=Frame(F6,bd=7,relief=GROOVE)
	   btn_F.place(x=750,width=580,height=105)

	   total_btn=Button(btn_F,command=self.total,text="Total",bg="cadet blue",fg="white",bd=2,pady=15,width=10,font="Arial 12 bold").grid(row=0,column=0,padx=5,pady=5)
	   GBill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadet blue",fg="white",bd=2,pady=15,width=11,font="Arial 12 bold").grid(row=0,column=1,padx=5,pady=5)
	   Clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadet blue",fg="white",bd=2,pady=15,width=11,font="Arial 12 bold").grid(row=0,column=2,padx=5,pady=5)
	   Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="cadet blue",fg="white",bd=2,pady=15,width=11,font="Arial 12 bold").grid(row=0,column=3,padx=5,pady=5)
	   self.welcome_bill()
       

	def total(self): 

		self.c_s_p=self.soap.get()*40
		self.c_fc_p=self.face_cream.get()*120
		self.c_fw_p=self.face_wash.get()*60
		self.c_hs_p=self.spray.get()*180
		self.c_hg_p=self.gel.get()*140
		self.c_bl_p=self.lotion.get()*180

		self.total_cosmetic_price=float(
			                        self.c_s_p+
                                    self.c_fc_p+
                                    self.c_fw_p+
                                    self.c_hs_p+
                                    self.c_hg_p+
                                    self.c_bl_p
                                    )
		self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
		self.c_tax=round((self.total_cosmetic_price*0.05),2)
		self.cosmetic_tax.set("Rs. "+str(self.c_tax))

		self.g_r_p=self.rice.get()*80
		self.g_f_p=self.food_oil.get()*120
		self.g_p_p=self.pulses.get()*60
		self.g_fl_p=self.flour.get()*200
		self.g_s_p=self.sugar.get()*40
		self.g_t_p=self.tea.get()*150

		self.total_grocery_price=float(
                                    self.g_r_p+
                                    self.g_f_p+
                                    self.g_p_p+
                                    self.g_fl_p+
                                    self.g_s_p+
                                    self.g_t_p
                                    )
		self.grocery_price.set("Rs. "+str(self.total_grocery_price))
		self.g_tax=round((self.total_grocery_price*0.1),2)
		self.grocery_tax.set("Rs. "+str(self.g_tax))

		self.d_p_p=self.pepsi.get()*40
		self.d_d_p=self.dew.get()*45
		self.d_c_p=self.coke.get()*50
		self.d_l_p=self.limca.get()*50
		self.d_m_p=self.maaza.get()*40
		self.d_s_p=self.sprite.get()*40

		self.total_cold_drink_price=float(
                                    self.d_p_p+
                                    self.d_d_p+
                                    self.d_c_p+
                                    self.d_l_p+
                                    self.d_m_p+
                                    self.d_s_p
                                    )
		self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
		self.d_tax=round((self.total_cold_drink_price*0.02),2)
		self.cold_drink_tax.set("Rs. "+str(self.d_tax))


		self.Total_bill=float(   
		                           self.total_cosmetic_price+
			                       self.total_grocery_price+
			                       self.total_cold_drink_price+
			                       self.c_tax+
			                       self.g_tax+
			                       self.d_tax
			                       )

	def welcome_bill(self):
		self.txtarea.delete('1.0',END)
		self.txtarea.insert(END,"\tWelcome to Saini's Retail\n")  
		self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
		self.txtarea.insert(END,f"\n Customer Name :{self.c_name.get()}")
		self.txtarea.insert(END,f"\n Phone Number :{self.c_phon.get()}")
		self.txtarea.insert(END,f"\n======================================")
		self.txtarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
		self.txtarea.insert(END,f"\n======================================")

	def	bill_area(self):
		if self.c_name.get()=="" or self.c_phon.get()=="":
		    messagebox.showerror("Error","Customer details are necessary")
		elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get() =="Rs. 0.0":
		    messagebox.showerror("Error","No Product Purchased")
		else:
			self.welcome_bill()
		#=========cosmetics============
		if self.soap.get()!=0:
			self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
		if self.face_cream.get()!=0:
			self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
		if self.face_wash.get()!=0:
			self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
		if self.spray.get()!=0:
			self.txtarea.insert(END,f"\n  Hair Spray\t\t{self.spray.get()}\t\t{self.c_hs_p}")
		if self.gel.get()!=0:
			self.txtarea.insert(END,f"\n  Hair Gel\t\t{self.gel.get()}\t\t{self.c_hg_p}")
		if self.lotion.get()!=0:
			self.txtarea.insert(END,f"\n Body Lotion\t\t{self.lotion.get()}\t\t{self.c_bl_p}")
		#==========grocery============
		if self.rice.get()!=0:
			self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
		if self.food_oil.get()!=0:
			self.txtarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_p}")
		if self.pulses.get()!=0:
			self.txtarea.insert(END,f"\n Pulses\t\t{self.pulses.get()}\t\t{self.g_p_p}")
		if self.flour.get()!=0:
			self.txtarea.insert(END,f"\n Flour\t\t{self.flour.get()}\t\t{self.g_fl_p}")
		if self.sugar.get()!=0:
			self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
		if self.tea.get()!=0:
			self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")
		#==========cold drink========
		if self.pepsi.get()!=0:
			self.txtarea.insert(END,f"\n Pepsi\t\t{self.pepsi.get()}\t\t{self.d_p_p}")
		if self.dew.get()!=0:
			self.txtarea.insert(END,f"\n Dew\t\t{self.dew.get()}\t\t{self.d_d_p}")
		if self.coke.get()!=0:
			self.txtarea.insert(END,f"\n Coke\t\t{self.coke.get()}\t\t{self.d_c_p}")
		if self.limca.get()!=0:
			self.txtarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t\t{self.d_l_p}")
		if self.maaza.get()!=0:
			self.txtarea.insert(END,f"\n Maaza\t\t{self.maaza.get()}\t\t{self.d_m_p}")
		if self.sprite.get()!=0:
			self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")

		self.txtarea.insert(END,f"\n-------------------------------------")
		if self.cosmetic_tax.get()!="Rs. 0.0":
			self.txtarea.insert(END,f"\n Cosmetics Tax\t\t\t{self.cosmetic_tax.get()}")
		if self.grocery_tax.get()!="Rs. 0.0":
			self.txtarea.insert(END,f"\n Groceries Tax\t\t\t{self.grocery_tax.get()}")
		if self.cold_drink_tax.get()!="Rs. 0.0":
			self.txtarea.insert(END,f"\n Cold Drinks Tax\t\t\t{self.cold_drink_tax.get()}")	

		self.txtarea.insert(END,f"\n Total Bill : \t\t\t Rs. {self.Total_bill}")
		self.txtarea.insert(END,f"\n-------------------------------------")	
		self.save_bill()

	def save_bill(self):
		op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
		if op>0:
			self.bill_data=self.txtarea.get('1.0',END)
			f1=open("bills/"+str(self.bill_no.get())+".txt","w")
			f1.write(self.bill_data)
			f1.close()
			messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} saved successfully")
		else:
			return


	def find_bill(self)	:
		present="no"
		for i in os.listdir("bills/"):
			if i.split('.')[0]==self.search_bill.get():
				f1=open(f"bills/{i}","r")
				self.txtarea.delete('1.0',END)
				for d in f1:
					self.txtarea.insert(END,d)
				f1.close()
				present="yes"
		if present=="no":
			messagebox.showerror("Error","Invalid Bill no.")

	def clear_data(self):	
		op=messagebox.askyesno("Clear","Do you really want to clear the data?")
		if op>0:
		#========cosmetics=============	
		    self.soap.set(0)
		self.face_cream.set(0)
		self.face_wash.set(0)
		self.spray.set(0)
		self.gel.set(0)
		self.lotion.set(0)
		#===========Groceries============
		self.rice.set(0)
		self.food_oil.set(0)
		self.pulses.set(0)
		self.flour.set(0)
		self.sugar.set(0)
		self.tea.set(0)
		#==========cold drinks===========
		self.pepsi.set(0)
		self.dew.set(0)
		self.coke.set(0)
		self.limca.set(0)
		self.maaza.set(0)
		self.sprite.set(0)
		#===========total product price & tax vaiables====
		self.cosmetic_price.set("")
		self.grocery_price.set("")
		self.cold_drink_price.set("")

		self.cosmetic_tax.set("")
		self.grocery_tax.set("")
		self.cold_drink_tax.set("")

		#=========Customer============
		self.c_name.set("")
		self.c_phon.set("")
		self.bill_no.set("")
		x=random.randint(1000,9999)
		self.bill_no.set(str(x))
		self.search_bill.set("")
		self.welcome_bill()

	def Exit_app(self):
		op=messagebox.askyesno("Exit","Do you really want to exit?")
		if op>0:
			self.root.destroy()

			

root=Tk()
obj=Bill_App(root)
root.mainloop()
