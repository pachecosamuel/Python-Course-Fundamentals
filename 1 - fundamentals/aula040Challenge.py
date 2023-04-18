# num = input("Enter a number: ")  # Get input from user
#
# # Convert each digit in the input to an integer and sum them
# digit_sum = sum(int(digit) for digit in num)
#
# # Print the result
# print("The sum of the digits is:", digit_sum)
number = input("type a number: ");
sum = 0;

for digit in number:
    sum += int(digit);

print(f"The value is: {sum}")