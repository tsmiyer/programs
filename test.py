stack = []
 
stack.append(1)
stack.append(2)
stack.append(3)
 
print('Initial stack')
print(stack)
 
print('\nElements poped out from the stack :')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
if stack == []:
    print ("Stack empty")
else :
    print("Stack not empty")

print('\nStack after elements are poped out :')
print(stack)