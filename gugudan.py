def print_gugudan(a):
    for dan in range(1,9):
        print("<{} 단>-----------------------".format(dan))
        for num in range(1,10):
            print(dan," X ",num," = ",dan*num)
    print("--------------------------------")

print_gugudan(8) #argument 8을 9로 바꿔줍니다
