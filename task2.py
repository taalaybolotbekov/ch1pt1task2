def square_number(number):
    return number ** 2
number = int(input("vvedite chislo: "))
print("квадрат числа {} - {} .". format (number, square_number(number)))

# #DO NOT remove lines below here, this is designed to test your code. 

def test_square_number():
    assert square_number(2) == 4 
    assert square_number(8) == 64 
    assert square_number(10) == 100
print("YOUR CODE IS CORRECT!")

test_square_number
