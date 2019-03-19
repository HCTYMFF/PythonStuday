for x in range(1,6):
    print("x=",x)
    for j in range(1,6):
        if(x==4):
            continue  #continue 会结束当前当次内循环，继续下一次内循环
        print(x,"*",j,"=",x*j,end=" ")
        if(x==j):
            print("\n")
            break# break只会退出内循环，不会退出第一层（外）循环


