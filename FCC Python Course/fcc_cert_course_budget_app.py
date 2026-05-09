import math
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return sum(entry["amount"] for entry in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": -amount, "description": f"Transfer to {category.name}"})
            category.ledger.append({"amount": amount, "description": f"Transfer from {self.name}"})
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        lines = []
        lines.append(self.name.center(30, "*"))
        for entry in self.ledger:
            amount = entry["amount"]
            description = entry["description"]
            lines.append(f"{description[:23]:<23}{amount:>7.2f}")
        lines.append(f"Total: {self.get_balance():.2f}")
        return "\n".join(lines)


def create_spend_chart(categories):
    title = "Percentage spent by category"

    total_spent = []
    for category in categories:
        category_total_spent = sum(entry["amount"] for entry in category.ledger if entry["amount"] < 0)
        total_spent.append(category_total_spent)
    overall_total = sum(total_spent)

    percentages = []
    for spent in total_spent:
        pct = math.floor((abs(spent)/ abs(overall_total)) * 100 / 10) * 10
        percentages.append(pct)

    lines = []
    lines.append(title)
    for i in range(100, -1, -10):
        row = f"{i:>3}|"
        for pct in percentages:
            if pct >= i:
                row += " o "
            else:
                row += "   "
        row += " "
        lines.append(row)
    lines.append("    " + "-" * (len(categories) * 3 + 1))
    print(total_spent)
    print(overall_total)
    print(percentages)

    max_len = max(len(category.name) for category in categories)
    for i in range(max_len):
        row = "     "
        for category in categories:
            if i < len(category.name):
                row += category.name[i] + "  "
            else:
                row += "   "
        lines.append(row)
    return '\n'.join(lines)


food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
auto = Category('Auto')
auto.deposit(1000)
auto.withdraw(33.40, 'fuel')
auto.withdraw(100, 'repairs')
print(create_spend_chart([food, clothing, auto]))

