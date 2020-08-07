try :
    file = open("love","r+")
except Exception as a:
        print("there is no love file")
        c = input("do you want creat a new file?")
        if c == "y":
            file = open("love","w")
        else:
            pass
else:
    file.write("I love xixi")
file.close()