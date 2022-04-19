from tkinter import *
from tkinter import messagebox

# Variables 
invDough = 0.0
invSauce = 0.0
invCheese = 0.0
invPepperoni = 0.0
fdSales = 0.0
fdExpenses = 0.0

# Define collections
cheesePizza = list()
pepperoniPizza = list()

# Function to update inventory outputs
def fnUpdateInventoryOutput():
    lblDoughOutput.config(text=invDough)
    lblSauceOutput.config(text=invSauce)
    lblCheeseOutput.config(text=invCheese)
    lblPepperoniOutput.config(text=invPepperoni)

# Function to update financial data 
def fnUpdateFinancialData():
    lblSales.config(text=fdSales)
    lblExpenses.config(text=fdExpenses)
    lblProfits.config(text=fdSales-fdExpenses)

# Function to add dough to inventory
def fnAddDough():
    global invDough, fdExpenses
    invDough += 100
    fdExpenses += 20
    fnUpdateInventoryOutput()
    fnUpdateFinancialData()

# Function to add sauce to inventory
def fnAddSauce():
    global invSauce, fdExpenses
    invSauce += 100
    fdExpenses += 10
    fnUpdateInventoryOutput()
    fnUpdateFinancialData()

# Function to add cheese to inventory
def fnAddCheese():
    global invCheese, fdExpenses
    invCheese += 100
    fdExpenses += 25
    fnUpdateInventoryOutput()
    fnUpdateFinancialData()

# Function to add pepperoni to inventory
def fnAddPepperoni():
    global invPepperoni, fdExpenses
    invPepperoni += 100
    fdExpenses += 40
    fnUpdateInventoryOutput()
    fnUpdateFinancialData()

# Execute add to inventory button
def cmdAddtoInventory():
    print("Add to Inventory was called")
    if varDough.get() == 1:
        print("Add Dough was checked")
        fnAddDough()
    if varSauce.get() == 1:
        print("Add Sauce was checked")
        fnAddSauce()
    if varCheese.get() == 1:
        print("Add Cheese was checked")
        fnAddCheese()
    if varPepperoni.get() == 1:
        print("Add Pepperoni was checked")
        fnAddPepperoni()
    
# Function to add order to review order
def cmdAddtoOrder():
    print("Add to Order was called")
    try:
        quantity = int(entQuantity.get())
        print("Quantity Data Type: ", type(quantity))
        print("Quantity entered: " + str(quantity))
        if quantity < 1:
            messagebox.showerror("Error", "Quantity must be greater than 0. Please try again.")
    except ValueError:
        messagebox.showerror("Error", "Invalid entry. Please enter a valid numeric quantity.")
    else:
        if selection.get() == 0 and quantity >= 1:
            print("Cheese Pizza was selected")
            lstReviewOrder.insert(END, str(quantity) + " Cheese Pizza(s)")
            cheesePizza.append(quantity)
        if selection.get() == 1 and quantity >= 1:
            print("Pepperoni Pizza was selected")
            lstReviewOrder.insert(END, str(quantity) + " Pepperoni Pizza(s)")
            pepperoniPizza.append(quantity)
        print("Cheese Pizzas: ", cheesePizza)
        print("Pepperoni Pizzas: ", pepperoniPizza)

# Function to execute place order
def cmdPlaceOrder():
    print("Place Order was called")
    global invDough, invSauce, invCheese, invPepperoni, fdSales
    sumCheesePizza = sum(cheesePizza)
    print("Total Cheese Pizzas Ordered: ", sumCheesePizza)
    sumPepperoniPizza = sum(pepperoniPizza)
    print("Total Pepperoni Pizzas Ordered: ", sumPepperoniPizza)
    qty = sumCheesePizza + sumPepperoniPizza
    print("Total number of pizzas ordered: ", qty)
    
    # Update Inventory for Pizzas
    invDough -= 6 * qty
    print("Dough: ", invDough)
    invSauce -= 7 * qty
    print("Sauce: ", invSauce)
    invCheese -= 16 * qty
    print("Cheese: ", invCheese)
    invPepperoni -= 4 * sumPepperoniPizza
    print("Pepperoni: ", invPepperoni)
    # Update Sales for Pizzas
    fdSales += 15 * qty
    print("Sales: ", fdSales)

    # Determine if there is enough inventory for number of pizzas ordered
    if invDough >= 0 and invSauce >= 0 and invCheese >= 0 and invPepperoni >= 0:
        fnUpdateInventoryOutput()
        fnUpdateFinancialData()
        messagebox.showinfo("Confirmation", "Order has been placed.")
    else:
        messagebox.showerror("Error", "Insufficent inventory to complete order.")
        invDough += 6 * qty
        print("Dough: ", invDough)
        invSauce += 7 * qty
        print("Sauce: ", invSauce)
        invCheese += 16 * qty
        print("Cheese: ", invCheese)
        invPepperoni += 4 * sumPepperoniPizza
        print("Pepperoni: ", invPepperoni)
        fdSales -= 15 * qty
        print("Sales: ", fdSales)
    # Reset the listbox and quantities 
    cmdCancelOrder()

# Function to execute cancel order
def cmdCancelOrder():
    print("Cancel Order was called")
    lstReviewOrder.delete(0, END)
    cheesePizza.clear()
    print("Cheese Pizzas: ", cheesePizza)
    pepperoniPizza.clear()
    print("Pepperoni Pizzas: ", pepperoniPizza)

# Create the window
root = Tk()
root.title("Project 3")
root.geometry("850x600")

# Labels for inventory (column 0)
Label(root, text="INVENTORY").grid(row=0, column=0, columnspan=2, sticky=EW, padx=30)
Label(root, text="Dough: ").grid(row=1, column=0, sticky=W)
Label(root, text="Sauce: ").grid(row=2, column=0, sticky=W)
Label(root, text="Cheese: ").grid(row=3, column=0, sticky=W)
Label(root, text="Pepperoni: ").grid(row=4, column=0, sticky=W)

# Inventory outputs (column 1)
lblDoughOutput = Label(root, text="-")
lblDoughOutput.grid(row=1,column=1, sticky=W)

lblSauceOutput = Label(root, text="-")
lblSauceOutput.grid(row=2, column=1, sticky=W)

lblCheeseOutput = Label(root, text="-")
lblCheeseOutput.grid(row=3, column=1, sticky=W)

lblPepperoniOutput = Label(root, text="-")
lblPepperoniOutput.grid(row=4, column=1, sticky=W)

# Label for Add to Inventory (column 2)
Label(root, text="ADD TO INVENTORY").grid(row=0, column=2, sticky=W, padx=20)

# Add to Inventory checkboxes 
varDough = IntVar()
chkDough = Checkbutton(root, text="Add Dough", variable=varDough)
chkDough.grid(row=1, column=2, sticky=W, padx=30)

varSauce = IntVar()
chkSauce = Checkbutton(root, text="Add Sauce", variable=varSauce)
chkSauce.grid(row=2, column=2, sticky=W, padx=30)

varCheese = IntVar()
chkCheese = Checkbutton(root, text="Add Cheese", variable=varCheese)
chkCheese.grid(row=3, column=2, sticky=W, padx=30)

varPepperoni = IntVar()
chkPepperoni = Checkbutton(root, text="Add Pepperoni", variable=varPepperoni)
chkPepperoni.grid(row=4, column=2, sticky=W, padx=30)

# Create add to inventory button
btnAddInv = Button(root, text="Add To Inventory", command=cmdAddtoInventory)
btnAddInv.grid(row=5, column=2, sticky=W, padx=30)

#Labels for Order form (column 3)
Label(root, text="ORDER FORM").grid(row=0, column=3, columnspan=2, sticky=EW, pady=5)
Label(root, text="Quantity: ").grid(row=1, column=3, sticky=W)

# Entry for order form quantity
entQuantity = Entry(root)
entQuantity.grid(row=1, column=4, sticky=W)

# Radio buttons for order form
selection = IntVar()
rdCheese = Radiobutton(root, text="Cheese Pizza", variable=selection, value=0)
rdCheese.grid(row=2, column=3, columnspan=2, sticky=W)
rdCheese.select()
rdPepperoni = Radiobutton(root, text="Cheese & Pepperoni Pizza", variable=selection, value=1)
rdPepperoni.grid(row=3, column=3, columnspan=2, sticky=W)

# Add to order, order form button
btnAddOrder = Button(root, text="Add To Order", command=cmdAddtoOrder)
btnAddOrder.grid(row=4, column=3, columnspan=2, sticky=W)

# Review order label
Label(root, text="     ").grid(row=5, column=3)
Label(root, text="REVIEW ORDER").grid(row=6, column=3, columnspan=2, pady=10)

# Create frame for listbox and scrollbar 
frmReviewOrder = Frame(root)
frmReviewOrder.grid(row=7, column=3, columnspan=2, sticky=W)

scrReviewOrder = Scrollbar(frmReviewOrder)
scrReviewOrder.grid(row=0, column=1, sticky=N+S+W)

lstReviewOrder = Listbox(frmReviewOrder, height=6, width=30, yscrollcommand=scrReviewOrder.set)
lstReviewOrder.grid(row=0, column=0)

scrReviewOrder.config(command=lstReviewOrder.yview)

# Order review buttons
btnPlace = Button(root, text="Place Order", command=cmdPlaceOrder)
btnPlace.grid(row=8, column=3, sticky=W)

btnCancel = Button(root, text="Cancel Order", command=cmdCancelOrder)
btnCancel.grid(row=8, column=4, sticky=W, padx=30)

# Financial Data Column Labels
Label(root, text="     ").grid(row=1, column=5)
Label(root, text="FINANCIAL DATA").grid(row=0, column=6, columnspan=3, sticky=EW)
Label(root, text="Sales:").grid(row=1, column=6, sticky=W)
Label(root, text="$").grid(row=1, column=7, sticky=W)
Label(root, text="Expenses:").grid(row=2, column=6, sticky=W)
Label(root, text="$").grid(row=2, column=7, sticky=W)
Label(root, text="Profits:").grid(row=3, column=6, sticky=W)
Label(root, text="$").grid(row=3, column=7, sticky=W)

# Financial data outputs
lblSales = Label(root, text="-")
lblSales.grid(row=1, column=8, sticky=W)

lblExpenses = Label(root, text="-")
lblExpenses.grid(row=2, column=8, sticky=W)

lblProfits = Label(root, text="-")
lblProfits.grid(row=3, column=8, sticky=W)

# Past Orders header, listbox and button
Label(root, text="     ").grid(row=9, column=3)
Label(root, text="PAST ORDERS").grid(row=10, column=0, columnspan=3, sticky=W, pady=10, padx=90)

frmPastOrders = Frame(root)
frmPastOrders.grid(row=11, column=0, columnspan=3, sticky=W)
scrPastOrders = Scrollbar(frmPastOrders)
scrPastOrders.grid(row=0, column=1, sticky=N+S+W)
lstPastOrders = Listbox(frmPastOrders, height=6, width=30, yscrollcommand=scrPastOrders.set)
lstPastOrders.grid(row=0, column=0)
scrPastOrders.config(command=lstPastOrders.yview)

btnOrderDetails = Button(root, text="Show Order Details")
btnOrderDetails.grid(row=12, column=0, columnspan=3, sticky=W, padx=60)

# Past order details header and listbox
Label(root, text="PAST ORDER DETAILS").grid(row=10, column=3, columnspan=2, pady=10)

frmOrderDetails = Frame(root)
frmOrderDetails.grid(row=11, column=3, columnspan=3, sticky=W)
scrOrderDetails = Scrollbar(frmOrderDetails)
scrOrderDetails.grid(row=0, column=1, sticky=N+S+W)
lstOrderDetails = Listbox(frmOrderDetails, height=6, width=30, yscrollcommand=scrOrderDetails.set)
lstOrderDetails.grid(row=0, column=0)
scrOrderDetails.config(command=lstOrderDetails.yview)

# Display window
root.mainloop()

