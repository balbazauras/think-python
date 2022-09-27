

def eval_loop():
    user_input=''
    while True:
        user_input=input("Please enter value to evaluate: ")
        if(user_input =='done'):
            break
        print("your value evluated: "+str(eval(user_input)))

eval_loop()
    