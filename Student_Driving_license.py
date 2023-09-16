
from tkinter import *
root=Tk()
root.title=("Drivers Licence")
root.geometry("600x400")
root.configure(bg="white")
canvas=Canvas(root,width=400,height=250)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 400, 45, fill="#F6091E")


label_heading = canvas.create_text(200,20, font=('Times', '24', 'bold italic') ,text="Driving License", fill = "white")
label_id_tag = canvas.create_text(25,60, font=('Times', '14', 'bold') ,text="ID :")
label_name_tag = canvas.create_text(30,100, font=('Times', '12', 'bold') ,text="Name :")
label_dob_tag = canvas.create_text(52,120, font=('Times', '12', 'bold') ,text="Date of birth :")
label_pin_tag = canvas.create_text(32,140, font=('Times', '12', 'bold') ,text="Pin no. :")
label_address_tag = canvas.create_text(36,160, font=('Times', '12', 'bold') ,text="Address :")
label_vehicle_type_tag = canvas.create_text(155,180, font=('Times', '12', 'bold') ,text="Authorisation to drive the following vehicles :")

# Create all the labels required to be displayed
label_heading=Label(root)
label_id_tag=Label(root)
label_name_tag=Label(root)
label_dob_tag=Label(root)
label_pin_tag=Label(root)
label_address_tag=Label(root)
label_vehicle_type_tag=Label(root)
# Define the function
def variables():
    id_tag = complex("58CAF42654")
    print(type("id_tag"))
    name_tag = str("Surya Mandalapu")
    print(type("name_tag"))
    dob_tag = ("22 January 2010")
    print(type("dob_tag"))
    pin_tag("123456")
    print(type("pin_tag"))
    address_tag = ("Folsom, California, United States Of America, North America, Earth, Solar System, Milky Way")
    print(type("address_tag"))
    vehicle_type_tag = ("Four Wheeler, Two Wheeler")
    print(type("vehicle_type_tag"))
    label_id_tag["text"]=id_tag
    label_name_tag["text"]=name_tag
    label_dob_tag["text"]=id_dob_tag
    label_pin_tag["text"]=pin_tag
    label_address_tag["text"]=address_tag
    label_vehicle_type_tag["text"]=vehicle_type_tag
    

# Create a button
button1=Button(root, text="show", command="variables")
button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
button1_window = canvas.create_window(200, 235, anchor=CENTER, window=button1)
label_id_window = canvas.create_window(80, 60, anchor=CENTER, window=label_id_tag)
label_name_window = canvas.create_window(100, 100, anchor=CENTER, window=label_name_tag)
label_dob_window = canvas.create_window(140, 120, anchor=CENTER, window=label_dob_tag)
label_pin_window = canvas.create_window(85, 140, anchor=CENTER, window=label_pin_tag)
label_address_window = canvas.create_window(130, 160, anchor=CENTER, window=label_address_tag)
label_vehicle_no_window = canvas.create_window(335, 180, anchor=CENTER, window=label_vehicle_type_tag)
canvas.pack()
label_heading.pack()
label_id_tag.pack()
label_name_tag.pack()
label_dob_tag.pack()
label_pin_tag.pack()
label_address_tag.pack()
label_vehicle_type_tag.pack()
root.mainloop()
# tkinter basic template end statement
