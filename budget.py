class Category:
    DESCRIPTION = "description"

    name = ""
    ledger = list()
   
    def __init__(self, name):
        self.name = name
    
    def get_balance(self):
        amount_list = list()
        for i in self.ledger:
            amount = float(i["amount"])
            amount_list.append(amount)
        result = sum(amount_list)
        return result

    def deposit(self, amount, description=""):
        return self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        balance = self.check_funds(amount)
        if balance == True:
            self.ledger.append({"amount": -amount, "description": description})        
        return balance

    def check_funds(self, amount):
        current_balance = self.get_balance()
        if float(amount) > current_balance:
            return False
        else:
            return True

    def transfer(self, amount, category):
        description_to = "Transfer to " + category.name
        description_from = "Transfer from " + self.name
        if self.withdraw(amount, description_to) == True:
          category.deposit(amount, description_from)
          return True
        else:
          return False
            
    def __repr__(self):
        if self.name == "entertainment":
            first_line = '*' * 8 + self.name + '*' * 9
        else:
            first_line = '*' * int((30 - len(self.name))/2) + self.name + '*' * int((30 - len(self.name))/2)
        
        items_list = list()
        for i in self.ledger:
          amount = i.get('amount')
          amount = f"{amount:.2f}"
          description = i.get('description')
          second_line = description[:23] + ' ' * (30 - len(description[:23])- len((str(amount)))) + str(amount)
          items_list.append(second_line)
        items_string = '\n'.join(items_list)
        
        result = self.get_balance()
        total = "Total: " + str(result)
        text = first_line + "\n" + items_string + "\n" + total
        return text
        
    def get_total(self):
        total = 0.00
        for i in self.ledger:
            if i['amount'] < 0:
                total = total + float(i['amount'])
        return total

def round_down(num, divisor):
    result = num - (num % float(divisor))
    return result



def create_spend_chart(categories):
    
    # percentage spent by category:
  total_withdrawals = 0.00
  
  for category in categories:
      total_one_category = category.get_total()
      total_withdrawals += total_one_category
  
  lst_pct = list()
  for category in categories:
      pct = (category.get_total() / total_withdrawals) * 100
      new_pct = round(pct, 10)
      lst_pct.append(new_pct)
  
  
  headline = 'Percentage spent by category\n'
  items = ""
  x = 100
  while x >= 0:
      bar = " "
      for category_pct in lst_pct:
          if category_pct >= x:
              bar = bar + "o  "    
          else:
              bar = bar + "   "   
      items = items + str(x).rjust(3) + "|" + bar + "\n"
      x = x-10
  
  dashes = ' ' * 4 + '-' * ((len(categories)*3)+1) + "\n"

  name_lst = list()
  map(lambda category: name_lst.append(category), categories)
  
  longest_name = max(name_lst, key = len)
  row_final = list()
  for i in range(len(longest_name)):
    row = " " * 5
    for name in name_lst:
      if i >= len(name):
        row = row + " " * 3
      else:
        row = row + name[i] + " " * 2
    row_final.append(row)
  final_row = '\n'.join(row_final)
  
  result = headline + items + dashes + final_row
  return result
