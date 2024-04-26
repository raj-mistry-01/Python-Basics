# hiding money at a specified position.
list_=[["😊","😊","😊"],["😊","😊","😊"],["😊","😊","😊"]]
print("Enter the locaion where you want to hide your money in the form of row column : ")
x,y=(input().split(" "))
list_[int(x)-1][int(y)-1]="😑"
print("The matrix form : ")
print(f"{list_[0]}\n{list_[1]}\n{list_[2]}")