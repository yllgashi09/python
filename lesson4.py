names = ["Blerta","Erosi", "Driloni", "brikena", "YLLI"]

for name in names:
    print(name)



sentence = "hello world"

for character in sentence:
    if character.isalpha():
        print(character)


for number in range(1,6):
    print(number)


numbers = [12,45,6,72,21,8,94,57]

maximum  = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
    print("the maximum value in the list is: ", maximum)


count = 1

while count <= 5:
    print("interation", count)
    count +=1


while True:
    user_input = input("enter a pozitive number: ")

    if user_input.isnumeric():
        number = int(user_input)

        if number > 0:
            break


            print("invalid input please try again")
        print("You have entered a valid pozitive number:", number)

    list = [1,2,3,4,5,6,7]
    target =4

    for number in list:
        print(number)
        if number == target:
            print("Target found")
            break