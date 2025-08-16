class Cookie:
    def __init__(self, flavor):  # __init__ is the constructor; it initializes attributes for each new instance.
        self.flavor = flavor     # This assigns the flavor parameter to an instance attribute, allowing global use within the class.
    
    def getFlavor(self):         # We use "self" to access instance attributes like flavor, set up by the constructor.
        return f"It's a {self.flavor} cookie"  # Access the flavor attribute using "self.flavor".
    
    def setColor(self, color):   # This method takes a color parameter but does not store it; color is a local parameter.
        return f"Cookie looks nice, {color} & delicious\n"  # Local parameters like "color" are used only within this method.

# Creating instances and calling methods
chocolateCookie = Cookie("Chocolate")
print(chocolateCookie.getFlavor())        # Output: "It's a Chocolate cookie"
print(chocolateCookie.setColor("Brown"))  # Output: "Cookie looks nice, Brown & delicious\n"

pineappleCookie = Cookie("Pineapple")
print(pineappleCookie.getFlavor())        # Output: "It's a Pineapple cookie"
print(pineappleCookie.setColor("Light Yellow"))  # Output: "Cookie looks nice, Light Yellow & delicious\n"
