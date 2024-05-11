# put your python code here
def count_to_100():
    def rec(x):
        if x <= 100:
            print(x)
            rec(x + 1)
    rec(1)
    
count_to_100()