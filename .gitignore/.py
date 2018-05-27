from tkinter import *
import datetime
#This is just importing libraries that I need for my code

root = Tk()
root.title("Ordering List and Profit Calculator")
root.configure(background="white")
root.geometry("1440x900")
#Setting up the GUI

order_num = 0
profit_inr = 0
order_format_1 = StringVar()
order_format_1.set("")

order_format_2 = StringVar()
order_format_2.set("")

order_format_3 = StringVar()
order_format_3.set("")

order_format_4 = StringVar()
order_format_4.set("")

order_format_5 = StringVar()
order_format_5.set("")

profit_amount = StringVar()
profit_amount.set(0)
#All of this is setting variables as strings so that they display on the GUI when you change them

def order():
    global profit_inr
    global order_num
    global order_format_1
    global order_format_2
    global order_format_3
    global order_format_4
    global order_format_5
    #All of this is making variables global so that it can access variables that are not in this function

    order_num = order_num + 1
    date = datetime.date.today()

    retail = int(retail_price_entry.get())
    shipping = int(shipping_costs_entry.get())
    sales = int(sales_price_entry.get())
    #Making more variables

    order_list.append(date)
    order_list.append(amount_ordered_entry.get())
    order_list.append(product_entry.get())
    order_list.append(retail_price_entry.get())
    order_list.append(shipping_costs_entry.get())
    order_list.append(sales_price_entry.get())
    #Appending values from different entries to my list

    profit_inr = profit_inr + sales - (shipping + retail)
    profit_amount.set(profit_inr)
    #Setting the value of profit

    product_entry.delete(0, END)
    amount_ordered_entry.delete(0, END)
    retail_price_entry.delete(0, END)
    shipping_costs_entry.delete(0, END)
    sales_price_entry.delete(0, END)
    #Deleting all the numbers/words on the entries

    if order_num % 5 == 1:
        format = order_list[0], ": ", order_list[1], order_list[2], "Total cost:", int(order_list[3])+int(order_list[4]), "Sale Price:", order_list[5]
        order_format_1.set(format)
    if order_num % 5 == 2:
        format = order_list[6], ": ", order_list[7], order_list[8], "Total cost:", int(order_list[9])+int(order_list[10]), "Sale Price:", order_list[11]
        order_format_2.set(format)
    if order_num % 5 == 3:
        format = order_list[12], ": ", order_list[13], order_list[14], "Total cost:", int(order_list[15])+int(order_list[16]), "Sale Price:", order_list[17]
        order_format_3.set(format)
    if order_num % 5 == 4:
        format = order_list[18], ": ", order_list[19], order_list[20], "Total cost:", int(order_list[21])+int(order_list[22]), "Sale Price:", order_list[23]
        order_format_4.set(format)
    if order_num % 5 == 0:
        format = order_list[24], ": ", order_list[25], order_list[26], "Total cost:", int(order_list[27])+int(order_list[28]), "Sale Price:", order_list[29]
        order_format_5.set(format)
    #Keeping 5 orders at max at a time

order_list = []

product_name = Label(root, text="Product Name:", font="Sans 18")
product_name.place(x=0, y=80)

product_entry = Entry(root, width=20, font="Sans 15")
product_entry.place(x=0, y=120)

amount_ordered = Label(root, text="Number of items ordered:", font="Sans 18")
amount_ordered.place(x=0, y=180)

amount_ordered_entry = Entry(root, width=20, font="Sans 15")
amount_ordered_entry.place(x=0, y=220)

retail_price = Label(root, text="Retail Price (Rupees):", font="Sans 18")
retail_price.place(x=0, y=280)

retail_price_entry = Entry(root, width=20, font="Sans 15")
retail_price_entry.place(x=0, y=320)

shipping_costs = Label(root, text="Shipping Costs (Rupees):", font="Sans 18")
shipping_costs.place(x=0, y=380)

shipping_costs_entry = Entry(root, width=20, font="Sans 15")
shipping_costs_entry.place(x=0, y=420)

sales_price = Label(root, text="Selling Price:", font="Sans 18")
sales_price.place(x=0, y=480)

sales_price_entry = Entry(root, width=20, font="Sans 15")
sales_price_entry.place(x=0, y=520)

order_history = Label(root, text="Order History:", font="Sans 18")
order_history.place(x=1000, y=80)

order_1 = Label(root, textvariable=order_format_1, font="Sans 18")
order_1.place(x=800, y=130)

order_2 = Label(root, textvariable=order_format_2, font="Sans 18")
order_2.place(x=800, y=180)

order_3 = Label(root, textvariable=order_format_3, font="Sans 18")
order_3.place(x=800, y=230)

order_4 = Label(root, textvariable=order_format_4, font="Sans 18")
order_4.place(x=800, y=280)

order_5 = Label(root, textvariable=order_format_5, font="Sans 18")
order_5.place(x=800, y=330)

profit = Label(root, text="Total Profit (INR):", font="Sans 18")
profit.place(x=0, y=680)

profit_value = Label(root, textvariable=profit_amount, font="Sans 18")
profit_value.place(x=0, y=730)

order_button = Button(root, text="Order", font="Sans 18", width=10, command=order)
order_button.place(x=0, y=630)

quit = Button(root, text="Quit", font="Sans 18", width=10, command=quit)
quit.place(x=210, y=630)
#The rest of the code is making the entries, buttons, and labels

root.mainloop()
