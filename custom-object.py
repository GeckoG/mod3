class Purchase(object):
    def __init__(self, amount):
        self.amount = amount
    def calculateTax(self, taxPercent):
        return self.amount * taxPercent/100.0
    def calculateTip(self, taxPercent):
        return self.amount * tipPercent/100.0
    def calculateTotal(self, taxPercent, tipPercent):
        return self.amount * (1 + taxPercent/100.0 + tipPercent/100.0)

fancyDinner = Purchase(52.97)
print("You bought a fancy dinner for $52.97. Let's see what that will really cost you.")

taxPercent = 7.5
tipPercent = 20.0

tax = round(fancyDinner.calculateTax(taxPercent), 2)
tip = round(fancyDinner.calculateTip(tipPercent), 2)
total = round(fancyDinner.calculateTotal(taxPercent, tipPercent), 2)

print("Tax: ", tax)
print("Tip: ", tip)
print("Total: ", total)
