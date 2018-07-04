
try:
    p =10
    q = 5

    p = q/0

    f = open("abc.txt")


# except Exception as e:              #prints exception message as type
#     print(type(e))
#
#
# except Exception as e:              #prints exception message
#     print(e)

except ZeroDivisionError:
    print("Where is my Destiny.!")
except FileNotFoundError as e:
    print("No such file or directory:", e.filename)

except (FileNotFoundError, ZeroDivisionError):
    print("Kitne error krega bhai.!!")

