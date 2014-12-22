# coding: utf-8
def bmi(w, h):
    b = w / h**2
    return b
myweight = 75
myheight = 1.79
mybmi = bmi(myweight, myheight)
print "我的 BMI 是 " + str(mybmi)
