import random

def monty_hall(does_switch:bool) -> bool:

    # Step 1, make an array with 2 goats and a car, placed randomly.
    base_doors = ['car', 'goat', 'goat']
    doors = base_doors
    random.shuffle(doors)

    # Step 2, the contestant makes a choice, at random.
    contestant_choice = random.randint(0,2)

    # Step 3, the host reveals a goat from the remaining doors.
    remaining_doors = [i for i in range(3) if i != contestant_choice and doors[i] == 'goat']
    host_opens = random.choice(remaining_doors)

    # Step 4, contestant decides to switch or stay.
    if does_switch:
        contestant_choice = [i for i in range(3) if i != contestant_choice and i != host_opens][0]

    # Step 5, door is opened, we reveal 
    return True if doors[contestant_choice] == 'car' else False

def run_simulation(repeats:int):
    switch_wins = 0
    stay_wins = 0

    for _ in range(repeats):
        # Run the simulation where the contestant switches
        if monty_hall(does_switch=True):
            switch_wins += 1

        # Run the simulation where the contestant does not switch
        if monty_hall(does_switch=False):
            stay_wins += 1

    # Print the results
    print(f"Out of {repeats} simulations:")
    print(f"  Wins when switching: {switch_wins}")
    print(f"  Wins when staying: {stay_wins}")


# Example usage
repeats = int(input("Enter the number of simulations to run: "))
run_simulation(repeats)
