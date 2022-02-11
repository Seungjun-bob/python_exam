def createList(*args, type=1):
    if type==1:
        print([i for i in args])
    elif type==2:
        print([i for i in args if i%2==0])
    elif type==3:
        print([i for i in args if i%2!=0])
    elif type==4:
        print([i for i in args if i>10])

createList(1,2,3,4,5,6,7,8,9,10,15,25,30)
createList(1,2,3,4,5,6,7,8,9,10,15,25,30, type=1)
createList(1,2,3,4,5,6,7,8,9,10,15,25,30, type=2)
createList(1,2,3,4,5,6,7,8,9,10,15,25,30, type=3)
createList(1,2,3,4,5,6,7,8,9,10,15,25,30, type=4)