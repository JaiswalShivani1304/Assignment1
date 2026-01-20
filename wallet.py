class Wallet:
  def __init__(self,owner_name:str,balance:int):
    self.owner_name = owner_name
    self.balance = balance
    if balance<0:
      self.balance=0
    else:
      self.balance=balance  

  def add_money(self,amount):
    self.balance= self.balance+amount
    print(f"{self.owner_name} your total balance is now {self.balance}")

  def spend_money(self,amount):
    if(self.balance>=amount):
      self.balance=self.balance - amount
      print(f"{self.owner_name} total balance in your wallet is {self.balance}")
    else:
      print(f"Not enough money!, total balance in your wallet is {self.balance}") 

  def __add__(self,other):
    combinedWallet=Wallet("Combined Wallet",self.balance+other.balance)
    return (combinedWallet.owner_name,combinedWallet.balance)
  
  def __gt__(self,other):
    return self.balance > other.balance
  
  def __lt__(self,other):
    return self.balance < other.balance
  
  def __eq__(self,other):
    return self.balance == other.balance
  
  # optional

  def weekly_allowance(self,amount):
    self.balance=self.balance+amount
    return self.balance
  
  def saving_goal(self,savingAmount):
    return self.balance >= savingAmount

  def coupan(self,amount, discount):
    discount = amount * (discount/100)
    finalAmount = amount - discount

    if(finalAmount<= self.balance):
      self.balance -= finalAmount
      return f"After applying discount, decreased {finalAmount} from your wallet. Now your current balance is {self.balance}"
    else:
      return "Insufficient balance"


w1=Wallet("Shivani",5000)
print(w1.owner_name,w1.balance)
w1.add_money(6000)
w1.spend_money(2000)
w1.add_money(2000)
print(w1.saving_goal(2000))
print(w1.coupan(100,10))

w2= Wallet("Amit",100)
print(w2.owner_name,w2.balance)
w2.add_money(500)
w2.spend_money(300)
w2.add_money(100)

w3= w1+w2
print(w3)

print(w1>w2)
print(w1<w2)
print(w1==w2)

