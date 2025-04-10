import random

# Part 1: Single turn that stops at 20 or when rolling a 1
def single_turn():
    total = 0
    while total < 20:
        roll = random.randint(1, 6)
        print("Roll:", roll)
        if roll == 1:
            total = 0
            break
        total += roll
    print("Turn total:", total)
    return total

# Part 2: Simulate many turns and show score probabilities
def simulate_turns(num_tries):
    scores = {0:0, 20:0, 21:0, 22:0, 23:0, 24:0, 25:0}
    
    for _ in range(num_tries):
        score = single_turn()
        if score > 25:  # Just in case
            score = 25
        scores[score] += 1
    
    print("Score", "\t", "Chance")
    for score in sorted(scores):
        chance = scores[score] / num_tries
        print(score, "\t", round(chance, 5))

# Part 3: Let user choose when to hold
def custom_hold(hold_value):
    total = 0
    while total < hold_value:
        roll = random.randint(1, 6)
        print("Roll:", roll)
        if roll == 1:
            total = 0
            break
        total += roll
    print("Turn total:", total)
    return total

# Part 4: Play until reaching goal score
def play_game():
    score = 0
    while score < 100:
        print("\nCurrent score:", score)
        turn_total = single_turn()
        score += turn_total
    print("You won with", score, "points!")

# Example usage:
print("Part 1: Single turn example")
single_turn()

print("\nPart 2: Probabilities for hold-at-20")
simulate_turns(100000)

print("\nPart 3: Custom hold value (try 25)")
custom_hold(25)

print("\nPart 4: Full game to 100 points")
play_game()