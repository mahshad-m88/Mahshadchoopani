import math

num1 = int(input("عدد اول را وارد کنید: "))
num2 = int(input("عدد دوم را وارد کنید: "))

lcm = abs(num1 * num2) // math.gcd(num1, num2)

print(f"کوچکترین مقسوم علیه مشترک {num1} و {num2} برابر است با: {lcm}")
