num1 = int(input("عدد اول را وارد کنید: "))
num2 = int(input("عدد دوم را وارد کنید: "))

common_factors = []
for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        common_factors.append(i)

common_factors.sort(reverse=True)
print("مقسوم‌علیه‌های مشترک به صورت نزولی:", common_factors)
