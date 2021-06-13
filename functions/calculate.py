def calculate(ins):
    answer = ""
    while answer != "quit":
        try:
            answer = input(ins)
            print(eval(answer))
        except Exception as e:
            print(e)
            print("Please enter the correct things to calculate(submit)")
    return "normal"
            
