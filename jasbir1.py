
shoppingCart = {}


def mainMenu():
    print("WELCOME TO THE AMANDO SHOPPING SITE")
    print("A. Add product to the cart.")
    print("B. Search the product.")
    print("C. Delete the product from the cart.")
    print("D. Quit.")

def addProduct():
    if len(shoppingCart) >= 5:
        print("Cart is full")
        return
    productName = input("Enter the product name: ")
    productBrand = input("Enter the product brand: ")
    shoppingCart[productName] = productBrand
    print("Product added to cart")


def searchProduct():
    productName = input("Enter the product name: ")
    if productName in shoppingCart:
        print(f"{productName} is found in cart, with brand: {shoppingCart[productName]}")
    else:
        print("No product exists with this name")


def deleteProduct():
    if len(shoppingCart) == 0:
        print("Cart is empty, no item is found")
        return
    productName = input("Enter the product name: ")
    if productName in shoppingCart:
        del shoppingCart[productName]
        print("Product deleted from cart")
    else:
        print("No product exists with this name")


while True:
    mainMenu()
    choice = input("Enter your choice: ")
    if choice == "A" or choice == "a":
        addProduct()
    elif choice == "B" or choice == "b":
        searchProduct()
    elif choice == "C" or choice == "c":
        deleteProduct()
    elif choice == "D" or choice == "d":
        break
    else:
        print("Invalid choice, please try again")
