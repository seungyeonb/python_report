total = 0
counter = 1
while counter <= 10:
    grade = int(input ("Enter grade: "))
    total=grade+total
    counter=counter+1 
average = total / 10
print(average)

print("3개의 값을 입력하시오")
x=int(input("Enter the x: "))
y=int(input("Enter the y: "))
z=int(input("Enter the z: "))
x=x+1
y=y+1
z=z+1
print("변경된 값:",x,y,z)

a=10
b=8750
c=a*b
print(c)

pay_rate+8750
hours_worked=int(input"일을 한 전체 시간입력하세요!:"))
monthly_pay=hours_worked*pay_rate
print(monthly_pay)

won=100000
usd=won*1130
print(usd)

exchange_rate=int(input("현재 환율입력:"))
won=100000
usd=won*exchange_rate
print(usd)

fahrenheit=100
celsius=fahrenheit-32
celsius=celsius*5
celsius=celsius/9
print(celsius)

x=0
y=0
x=int(input("정수 x를 입력하시오:"))
y=int(input("정수 y를 입력하시오:"))
sum=x+y
print(sum)

price=int(input("상품의 가격을 입력하시오: "))
vat=price*0.1
print(vat)

age=int(input("현재 나이를 입력하시오: "))
age=age+10
print("10년후면",age, "세가 되시는 군요")

print("########################")
print("# 배송료 계산 프로그램 #")
print("########################")
price= int(input("상품의 가격을 입력하세요: "))
if price > 2000:
     shipping_cost = 0
else:
     shipping_cost = 3000
print(shipping_cost)

print("########################")
print("# 합격 불합격 프로그램 #")
print("########################")


grade = int(input("성적을 입력하시오: "))
if grade >= 60 :
     print("합격")
else :
     print("불합격") 

print("근무 시간을 입력하시오")
work_hour=int(input("근무시간 입력:  "))


if work_hour > 72 :
   print("초과근무 하셨습니다.")
else:
     priint("정상근무하셨습니다.") 

print("########################")
print("# 짝수와 홀수 판별 앱 #")
print("########################")


x = int(input("x값 정수를 입력하시오: ")
if (x % 2) !=  0 :
     print("홀수입니다.")
else:
     print("짝수입니다.")  
print("정수를 입력하시오.")
x= int(input("정수값 x를 입력하시오.:  "))
y= int(input("정수값 y를 입력하시오.:  "))
if x > y :
     print(x)
else:
     print(y)     

print("########################")
print("# 이름, 나이, 답변 앱  #")
print("########################")


yu_name = str(input("이름: "))
yu_age = int(input("나이: "))


if yu_age <= 25 :
     print("와우!!! 프로그래밍을 완벽하게 배울수 있는 나이입니다.!")
else:
     print("포기하기에는 아직 늦지 않았습니다.")
print("\n")          

price = int(inpur("상품의 가격을 입력하세요.: "))


if price > 100000:
       shipping_cost = 0
else:
      if price > 2000:
         shipping_cost = 3000
      else:
         shipping_cost = 5000


print("배송료는", shipping_cost, "입니다.")  
