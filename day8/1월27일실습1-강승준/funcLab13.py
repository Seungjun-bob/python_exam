def myprint(*p, deco="**", sep=","):
    if len(p) == 0:
        return print("Hello Python")
    # answer = []
    # for data in p:
    #     answer.append(data)
    # new_answer = [str(a) for a in answer]
    # print(deco, sep.join(new_answer), deco,sep="")
    print(deco, end=""); print(*p, sep=sep, end=""); print(deco)

myprint(10,20,30,deco="@",sep="-")
myprint("python","javascript","R",deco="$")
myprint("가","나","다")
myprint(100)
myprint(True,111,False,"abc",deco="&",sep="")
myprint()

