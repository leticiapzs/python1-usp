valores=input("Entre com dois inteiros positivos: ").split()
x= int(valores[0])
y= int(valores[1])
op = input("Informe o operador (+,-,*,/ ou **): ")
if op=="+":
    resultado = x+y
elif op=="-":
    resultado = x-y
elif op=="*":
    resultado = x*y
elif op=="/":
    resultado= x/y
elif op =="**":
    resultado = x**y
    print(x,op,y, "=", resultado)