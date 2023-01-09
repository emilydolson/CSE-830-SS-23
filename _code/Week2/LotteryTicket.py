import random

def generate_ticket(n):
    ticket = list(range(n))
    random.shuffle(ticket)
    return ticket

def static_strategy(n):
    ticket = generate_ticket(n)

    wins = 0

    for person in range(n):
        final_position = person + int((n/2))
        if final_position < n:
            choices = ticket[person:final_position]
        else:
            choices = ticket[person:] + ticket[:final_position % n]
        if person in choices:
            wins += 1

    if wins == n:
        return True
    return False

def optimal_strategy(n):
    ticket = generate_ticket(n)

    wins = 0
    for person in range(n):
        current = ticket[person]
        scratches = 1

        while current != person and scratches < 50:
            current = ticket[current]
            scratches += 1

        if current == person:
            wins += 1

    if wins == n:
        return True
    return False

def test(n):
    wins = 0
    for i in range(100):
        if optimal_strategy(n):
            wins += 1

    print("Optimal strategy:", wins/100)

    wins = 0
    for i in range(100):
        if static_strategy(n):
            wins += 1

    print("Static strategy:", wins/100)

if __name__ == "__main__":
    test(100)
