from itertools import permutations

def solve_send_more_money():
    letters = "SENDMORY"
    for digits in permutations(range(10), len(letters)):
        m = dict(zip(letters, digits))
        if m["S"] == 0 or m["M"] == 0:
            continue
        send = 1000*m["S"] + 100*m["E"] + 10*m["N"] + m["D"]
        more = 1000*m["M"] + 100*m["O"] + 10*m["R"] + m["E"]
        money = 10000*m["M"] + 1000*m["O"] + 100*m["N"] + 10*m["E"] + m["Y"]
        if send + more == money:
            return send, more, money, m

if __name__ == "__main__":
    result = solve_send_more_money()
    if result:
        print(f"{result[0]} + {result[1]} = {result[2]}")
        print("Mapping:", result[3])
    else:
        print("No solution found")
