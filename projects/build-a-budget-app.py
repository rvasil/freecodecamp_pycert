"""A Budget App for https://www.freecodecamp.org/learn/python-v9/lab-budget-app/build-a-budget-app"""


class Category:
    _amount_fmt = ">7.2f"

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def _ledger_tran_to_str(self, tran):
        desc = tran["description"][:23]
        return f"{desc:<23}{tran['amount']:{Category._amount_fmt}}"

    def __str__(self):
        result = f"{self.name:*^30}"
        for tran in self.ledger:
            result += "\n" + self._ledger_tran_to_str(tran)
        result += f"\nTotal: {self.get_balance():>.2f}"
        return result

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def deposit(self, amount, description=""):
        tran = {"amount": amount, "description": description}
        self.ledger.append(tran)

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            tran = {"amount": -amount, "description": description}
            self.ledger.append(tran)
            return True
        else:
            return False

    def get_balance(self):
        balance = sum([tran["amount"] for tran in self.ledger])
        return balance

    def transfer(self, amount, to):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {to.name}")
            to.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False


def _cat_chart_listing(spendings):
    lines = []
    total = 0
    for cat, spent in spendings.items():
        total += spent

    for r in range(100, -10, -10):
        line = f"{r:>3}|"
        for cat, spent in spendings.items():
            pct = int(spent * 10 / total) * 10
            line += " o " if pct >= r else " " * 3
        lines.append(line + " " * 1)
    return lines


def _cat_names_listing(spendings):
    max_cat_name_length = max([len(cat) for cat in spendings.keys()])
    lines = []
    for i in range(max_cat_name_length):
        line = " " * 4
        for cat in spendings.keys():
            line += f" {cat[i]} " if len(cat) > i else " " * 3
        lines.append(line + " " * 1)
    return lines


def create_spend_chart(categories):
    spendings = {}
    for cat in categories:
        spendings[cat.name] = -sum(
            [trans["amount"] for trans in cat.ledger if trans["amount"] < 0]
        )

    title = "Percentage spent by category"
    cat_chart = _cat_chart_listing(spendings)
    dashed_line = " " * 4 + "-" * 3 * len(spendings) + "-"
    cat_legend = _cat_names_listing(spendings)

    # for c in cat_chart:
    #     print(len(c))
    # print(len(dashed_line))
    # for c in cat_legend:
    #     print(len(c))

    result = [title, *cat_chart, dashed_line, *cat_legend]
    return "\n".join(result)


# food = Category('entertainment')
# food.deposit(1000, 'deposit')
# food.withdraw(10.15, 'groceries')
# food.withdraw(15.89, 'restaurant and more food for dessert')
# clothing = Category('Clothing')
# food.transfer(50, clothing)
# auto = Category('Auto')
# auto.deposit(1000, 'deposit')
# auto.withdraw(10.15, 'groceries')
# print(food)
# # # print(clothing)

# c = create_spend_chart([food, clothing, auto])
# print(c)
