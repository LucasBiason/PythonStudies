
def corrigir_numero(n):
    if n < 0:
        return 0
    if n < 10:
        return 1
    return 2

if __name__ == '__main__':
    numbers, n = [], 0

    while n <2:
        number = input("Entre com um número: ")
        
        if  number.replace('-','').isdigit():
            numbers.append(
                corrigir_numero(int(number))
            )
            
            n += 1
        
    for number in numbers:
        print("> ", number)
        
        