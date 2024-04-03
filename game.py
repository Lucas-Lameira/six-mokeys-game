import random

SCENARIO_SIZE = 6
# keep_playing = True

forward_monkeys = ['m1', 'm2', 'm3']
backward_monkeys = ['c3', 'c2','c1']

OBJECTIVE = ['c3', 'c2','c1', None, 'm1', 'm2', 'm3']

def find_empty_spot(scenario: list) -> int:
    for i in range(len(scenario)):
        if scenario[i] == None:
            return i

def create_scenario(): 
    scenario = ['m1', 'm2', 'm3', None, 'c3', 'c2','c1']
    print('Cena: ', scenario)
    return scenario

def create_possibilities(scenario):
    print('create poss: ', scenario)

    possible_scenarios = list()
    empty_spot_index = find_empty_spot(scenario)
    
    # array index
    monkey_behind_none_index = empty_spot_index - 1
    second_monkey_behind_none_index = empty_spot_index - 2

    monkey_after_none_index = empty_spot_index + 1
    second_monkey_after_none_index = empty_spot_index + 2

    # behind none
    if monkey_behind_none_index >= 0:
        print('monkey_behind_none_index: ', monkey_behind_none_index)
        monkey_behind_none = scenario[monkey_behind_none_index]
        if monkey_behind_none in forward_monkeys:
            new_scenario = scenario.copy()
            new_scenario[empty_spot_index] = monkey_behind_none
            new_scenario[monkey_behind_none_index] = None
            possible_scenarios.append(new_scenario)
    
    if second_monkey_behind_none_index >= 0:
        print('second_monkey_behind_none_index: ', second_monkey_behind_none_index)
        second_monkey_behind_none = scenario[second_monkey_behind_none_index]
        
        if second_monkey_behind_none in forward_monkeys: 
            new_scenario = scenario.copy()
            new_scenario[empty_spot_index] = second_monkey_behind_none
            new_scenario[second_monkey_behind_none_index] = None
            possible_scenarios.append(new_scenario)


    # after none
    if monkey_after_none_index <= SCENARIO_SIZE:
        print('monkey_after_none_index: ', monkey_after_none_index)
        monkey_after_none = scenario[monkey_after_none_index]
        
        if monkey_after_none in backward_monkeys: 
            new_scenario = scenario.copy()
            new_scenario[empty_spot_index] = monkey_after_none
            new_scenario[monkey_after_none_index] = None
            possible_scenarios.append(new_scenario)


    if second_monkey_after_none_index <= SCENARIO_SIZE:
        print('second_monkey_after_none_index: ', second_monkey_after_none_index)
        second_monkey_after_none = scenario[second_monkey_after_none_index]
        
        if second_monkey_after_none in backward_monkeys: 
            new_scenario = scenario.copy()
            new_scenario[empty_spot_index] = second_monkey_after_none
            new_scenario[second_monkey_after_none_index] = None
            possible_scenarios.append(new_scenario)

    return possible_scenarios

def make_a_choice(possible_scenarios: list) -> list:
    range = len(possible_scenarios)
    print('range', range)
    index_choice = random.randrange(0, range)
    print('index_choice: ', index_choice)
    return possible_scenarios[index_choice]

def has_won(scenario: list) -> bool: 
    return scenario == OBJECTIVE
    
def game_over():
    print('Game Over!')
    print('Reiniciando cena...')

def has_possible_choices(possible_choices: list) -> int:
    return len(possible_choices)

def main():
    keep_playing = True
    scenario = create_scenario()
    
    while keep_playing:
        choices = create_possibilities(scenario)

        if not has_possible_choices(choices):
            game_over()
            scenario = create_scenario()
            #keep_playing = False
            continue

        print('Possibilidades: ', choices)

        scenario = make_a_choice(choices)

        print('Escolha: ', scenario)

        if has_won(scenario):
            print('GG: ', scenario)
            keep_playing = False
        else:
            print('Próxima rodada!')
            print('==========================')
main()