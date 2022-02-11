def mycompredict(**args):
    if len(args) == 0:
        return None
    return print({'my'+k : v for k, v in args.items()})

mycompredict()
mycompredict(a=1,b=3,c=7,d=11)
mycompredict(a=3,b=11,c=34,d=123)
mycompredict(a=0,b=2,c=-1,df=3)