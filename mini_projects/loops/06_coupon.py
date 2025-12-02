users = [
    {'id':1,'name':'Vamsi','coupon':'P20','total':100},
    {'id':2,'name':'Chakri','coupon':'F10','total':150},
    {'id':3,'name':'Rani','coupon':'F50','total':80}
]

discounts = {
    "P20":(0.2,0),
    "F10":(0.1,0),
    "P50":(0,10)
}

for user in users:
    percent,fixed = discounts.get(user["coupon"],(0,0))
    discount = user["total"] * percent + fixed
    print(f"{user['name']} has a total of {user['total']} and got a discount of {discount}")
