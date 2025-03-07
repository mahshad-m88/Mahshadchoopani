usernames = []

while len(usernames) < 6:
    username = input("لطفاً نام کاربری را وارد کنید (برای پایان ورود داده‌ها عدد -1 را وارد کنید): ")
    
    if username == '-1':
        break
    
    usernames.append(username)

numeric_usernames = [username for username in usernames if username.isdigit()]

sorted_numeric_usernames = sorted(map(int, numeric_usernames))

print("نام کاربری های عددی به صورت صعودی:")
print(sorted_numeric_usernames)
