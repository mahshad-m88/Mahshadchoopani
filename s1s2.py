char = input("لطفاً یک حرف وارد کنید: ")

vowels = 'aeiou'

if char.lower() in vowels:
    print(f"حرف {char} صدادار است.")
else:
    print(f"حرف {char} صدادار نیست.")
