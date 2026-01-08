login = {
  "jeymsBond": "agent007",
  "tony_stark": "ironman101",
   "piterParker": "spider.12.12",
  "sherlok": "sher.l04"
}
username = input("login kiriting: ")
parol = input("parol kiriting: ")
for a, b in login.items():
    if a == username:
        if b == parol:
            print("Login va Parol togri")
            break
else:
    print("xato")


