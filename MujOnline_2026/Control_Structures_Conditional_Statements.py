# Control structures dictate the flow of execution in a program, enabling decision-making and repetition.

#Types of Control structures in python are 1.Conditional and 2.
# Conditional_statements - if,if-else,if-elif-else,nested and composite expressions.
# Looping Structure/Iteration - While,For,Range function and nested.


# Conditional_statements;
## evaluate conditions and execute specific code blocks based on whether the outcome is True or False.

# Only if statement - executes a block of code only if a specified condition is met (True).
a = int(input("Enter value of a "))
if a>0:
  print("Yes a is positive") # inside if block
print("out of if block code") # out of if block

# if-else statement - Provides two alternative execution paths. One block runs if the condition is True, and the else block runs if it is False.
a = int(input("Enter value of a "))
if a>0:
  print("Yes a is positive")
else:
  print("No a is negative")

# Take input from user and check wthether it is positive negative or zero if-elif-else statement
# Short for "else if", this allows you to check multiple alternative conditions in sequence. Python stops at the first True condition it finds,
a = int(input("Enter value of a "))
if a>0:
  print("positive")
elif a<0:
  print("Negative")
else:
  print("zero")

# Nested if else - An if statement placed inside another if or else branch, allowing for more complex, multi-layered decision-making
a = int(input("Enter value of a "))
if a>=0:
  if a>0:
    print("positive")
  else:
    print("Zero")
else:
  print("Negative")

# task - Student Grade Classification Using Nested Conditionals
per= float(input("Enter percentage in 12th"))
if per>=40.0:
   if per>=75:
    print("Grade A")
   elif per>=60:
    print("Grade B")
   else:
    print("Grade C")
else:
  print("User failed")


