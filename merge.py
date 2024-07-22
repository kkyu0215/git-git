# merge.py
def greet():
print("Hello from the main branch") 
#이부분에서 충돌이 발
#것이므로 gildong부분에 자기 이름 넣어주시면 됩니다.
def add(a, b):
return a + b
def subtract(a, b):
return a - b
def multiply(a, b):
return a * b
def divide(a, b):
if b == 0:
return "Cannot divide by zero"
return a / b
def main():
print("This is the main function")
greet()
result_add = add(10, 5)
result_sub = subtract(10, 5)
result_mul = multiply(10, 5)

Git 협업 과제 8

result_div = divide(10, 5)
print(f"Add: {result_add}, Subtract: {result_sub}, Multipl
if __name__ == "__main__":
main()
