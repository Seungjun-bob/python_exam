def mydict(**args):
    dict = {}
    if len(args) == 0:
        return print(dict)
    for key,value in args.items():
        dict['my'+key] = value
    return print(dict)

mydict()
mydict(a=1,b=3,c=7,d=11)
