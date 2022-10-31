
net_amount = 0

while True:
	
	str = input ("Enter transaction: ")

	transaction = str.split(" ")

	
	type = transaction [0]
	amount = int (transaction [1])

	if type=="D" or type=="d":
		net_amount += amount
	elif type=="W" or type=="w":
		net_amount -= amount
	else:
		pass

	 
	str = input ("want to continue (Y for yes,N for No) : ")
	if not (str[0] =="Y" or str[0] =="y") :
		
		break

if net_amount>0:
    print ("Net amount: ", net_amount)
else:
    print("Insufficient Balance")
