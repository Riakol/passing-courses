# put your python code here
text = input()
keyboard = {1: [".", ",", "?", "!", ":"], 
            2: ["A", "B", "C"], 
            3: ["D", "E", "F"],
            4: ["G", "H", "I"],
            5: ["J", "K", "L"],
            6: ["M", "N", "O"],
            7: ["P", "Q", "R", "S"],
            8: ["T", "U", "V"],
            9: ["W", "X", "Y", "Z"],
            0: [" "]}

for sym in text:
    for key in keyboard:
        if sym.upper() in keyboard[key]:
            for j in range(0, keyboard[key].index(sym.upper()) + 1):
                print(key, end='')