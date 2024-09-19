name= input("Enter your name ").upper()
print("Welcome",name,"to the Adventure Game \n")
print("You have entered a Jungle and you have to make strong decisions to not to 'DIE'")


answer = input("You have come to a bridge .Do you want to cross it or stay there and try fishing for a while?\n Type Cross to cross the bridge or Fishing to fish ").lower()

if answer=="cross":
    print("You didnt think about the need of food in a Jungle ,thus this means you lost at the beginning due to lack of critical thinking") 
    quit()
elif answer=="fish":
    print("Now you have to make a Fishing rod to fish")
else:
    print("Enter a valid answer")
