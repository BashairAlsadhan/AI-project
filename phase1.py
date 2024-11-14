

import random



categories = {
    'top': [
        {"item": "T-shirt", "price": 0.0, "dress_code": "Casual", "color": "Bright", "comfort": 5},
        {"item": "Formal Shirt", "price": 120.0, "dress_code": "Business", "color": "Dark", "comfort": 3},
        {"item": "Polo Shirt", "price": 80.0, "dress_code": "Sportswear", "color": "Bright", "comfort": 4},
        {"item": "Evening Blouse", "price": 150.0, "dress_code": "Evening", "color": "Dark", "comfort": 3},
        {"item": "Sweater", "price": 0.0, "dress_code": "Casual", "color": "Dark", "comfort": 5},
        {"item": "Hoodie", "price": 60.0, "dress_code": "Casual", "color": "Bright", "comfort": 4},
        {"item": "Tank Top", "price": 0.0, "dress_code": "Sportswear", "color": "Bright", "comfort": 4},
        {"item": "Silk Blouse", "price": 200.0, "dress_code": "Evening", "color": "Dark", "comfort": 3}
    ],
    'bottom': [
        {"item": "Jeans", "price": 0.0, "dress_code": "Casual", "color": "Dark", "comfort": 4},
        {"item": "Formal Trousers", "price": 150.0, "dress_code": "Business", "color": "Dark", "comfort": 3},
        {"item": "Sports Shorts", "price": 0.0, "dress_code": "Sportswear", "color": "Bright", "comfort": 5},
        {"item": "Skirt", "price": 100.0, "dress_code": "Evening", "color": "Bright", "comfort": 3},
        {"item": "Chinos", "price": 90.0, "dress_code": "Business", "color": "Dark", "comfort": 4},
        {"item": "Leggings", "price": 60.0, "dress_code": "Casual", "color": "Dark", "comfort": 5},
        {"item": "Athletic Pants", "price": 80.0, "dress_code": "Sportswear", "color": "Bright", "comfort": 5},
        {"item": "Evening Gown Bottom", "price": 250.0, "dress_code": "Evening", "color": "Dark", "comfort": 1}
    ],
    'shoes': [
        {"item": "Sneakers", "price": 0.0, "dress_code": "Sportswear", "color": "Bright", "comfort": 5},
        {"item": "Leather Shoes", "price": 180.0, "dress_code": "Business", "color": "Dark", "comfort": 2},
        {"item": "Running Shoes", "price": 120.0, "dress_code": "Sportswear", "color": "Bright", "comfort": 5},
        {"item": "Ballet Flats", "price": 90.0, "dress_code": "Casual", "color": "Dark", "comfort": 4},
        {"item": "High Heels", "price": 250.0, "dress_code": "Evening", "color": "Dark", "comfort": 2},
        {"item": "Sandals", "price": 0.0, "dress_code": "Casual", "color": "Bright", "comfort": 5},
        {"item": "Loafers", "price": 150.0, "dress_code": "Business", "color": "Dark", "comfort": 3},
        {"item": "Evening Pumps", "price": 220.0, "dress_code": "Evening", "color": "Bright", "comfort": 2}
    ],
    'neck': [
        {"item": "Silk Scarf", "price": 70.0, "dress_code": "Business", "color": "Dark", "comfort": 3},
        {"item": "Sports Scarf", "price": 0.0, "dress_code": "Sportswear", "color": "Bright", "comfort": 4},
        {"item": "Necklace", "price": 220.0, "dress_code": "Evening", "color": "Dark", "comfort": 3},
        {"item": "Casual Scarf", "price": 0.0, "dress_code": "Casual", "color": "Bright", "comfort": 5},
        {"item": "Bow Tie", "price": 80.0, "dress_code": "Evening", "color": "Dark", "comfort": 3},
        {"item": "Athletic Headband", "price": 50.0, "dress_code": "Sportswear", "color": "Bright", "comfort": 5},
        {"item": "Diamond Necklace", "price": 750.0, "dress_code": "Evening", "color": "Bright", "comfort": 3},
        {"item": "Choker", "price": 0.0, "dress_code": "Evening", "color": "Dark", "comfort": 4}
    ],
    'purse': [
        {"item": "Clutch Bag", "price": 100.0, "dress_code": "Evening", "color": "Dark", "comfort": 3},
        {"item": "Canvas Bag", "price": 0.0, "dress_code": "Casual", "color": "Bright", "comfort": 5},
        {"item": "Leather Briefcase", "price": 180.0, "dress_code": "Business", "color": "Dark", "comfort": 1},
        {"item": "Sports Backpack", "price": 80.0, "dress_code": "Sportswear", "color": "Bright", "comfort": 5},
        {"item": "Tote Bag", "price": 0.0, "dress_code": "Casual", "color": "Bright", "comfort": 4},
        {"item": "Wristlet", "price": 150.0, "dress_code": "Evening", "color": "Dark", "comfort": 3},
        {"item": "Fanny Pack", "price": 50.0, "dress_code": "Sportswear", "color": "Bright", "comfort": 4},
        {"item": "Elegant Handbag", "price": 250.0, "dress_code": "Evening", "color": "Dark", "comfort": 3}
    ]
}



#------------------------------------------------------------------------------------------------

def create_individual():
    # create_individual is a function that does not take any paramters and return a chromosome

    #for the team: i add this function just to help me create outfits (part of create pop function), felt more organized
    return {
        "top": random.choice(categories['top']),
        "bottom": random.choice(categories['bottom']),
        "shoes": random.choice(categories['shoes']),
        "neck": random.choice(categories['neck']),
        "purse": random.choice(categories['purse'])
    }


#------------------------------------------------------------------------------------------------




def create_initial_population(pop_size):

    # create_individual is a function that takes the population size and return initial population (set of chromosomes/individuals)
    return [create_individual() for _ in range(pop_size)]




#------------------------------------------------------------------------------------------------



def calculate_fitness(individual, target_dress_code, target_color, budget, comfort_level):
    # calculate_fitness in a function that takes the following parameters :individual, target_dress_code, target_color, budget, comfort_level,
    # and return the fitness score for the individual
    dress_code_score = 1 if all([item["dress_code"] == target_dress_code for item in individual.values()]) else 0
    color_score = 1 if all([item["color"] == target_color for item in individual.values()]) else 0
    total_price = sum([item["price"] for item in individual.values()])
    budget_score = 1 if total_price <= budget else 0
    avg_comfort = sum([item["comfort"] for item in individual.values()]) / 5.0
    comfort_score = 1 if comfort_level <= avg_comfort else 0

    # Weighted sum approach (the max sum will be 1 as 0.25+0.25+0.25+0.25 = 1 ) 
    # For the team : we may adjust the weights also to 0.25 for each على حسب شرحهم حسيت كذا منطقي اكثر 
    fitness = 0.25 * dress_code_score + 0.25 * budget_score + 0.25 * color_score + 0.25 * comfort_score
    return fitness


#------------------------------------------------------------------------------------------------


def binary_tournament_selection(population, fitnesses):
    def select_one():
        # randomly select two individuals (a and b)
        a = random.choice(range(len(population)))
        b = random.choice(range(len(population)))
        
        # if fitness values are equal then pick one randomly
        if fitnesses[a] == fitnesses[b]:
            return population[random.choice([a, b])] 
        
        # otherwise select the one with the higher fitness
        return population[a] if fitnesses[a] > fitnesses[b] else population[b]
    
    # select two parents using the select_one function, i put this function inside the binary selection as it will use its parameters 
    parent1 = select_one()
    parent2 = select_one()
    
    return parent1, parent2



#------------------------------------------------------------------------------------------------

# all the following functions for validation EXTRA 

def get_valid_dress_code():
    valid_dress_codes = ["Casual", "Sportswear", "Business", "Evening"]
    while True:
        target_dress_code = input("Enter your preferred dress code (Casual, Sportswear, Business, Evening): ").capitalize()
        if target_dress_code in valid_dress_codes:
            return target_dress_code
        else:
            print("Invalid dress code. Please enter one of the following: Casual, Sportswear, Business, Evening.")

def get_valid_color_palette():
    valid_color_palettes = ["Bright", "Dark"]
    while True:
        target_color = input("Enter your preferred color palette (Bright, Dark): ").capitalize()
        if target_color in valid_color_palettes:
            return target_color
        else:
            print("Invalid color palette. Please enter 'Bright' or 'Dark'.")

def get_valid_budget():
    while True:
        try:
            budget = float(input("Enter your budget (SAR): "))
            if budget >= 0:
                return budget
            else:
                print("Budget must be a non-negative number. Please enter a valid budget.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for the budget.")

def get_valid_comfort_level():
    while True:
        try:
            comfort_level = int(input("Enter your preferred comfort level (1-5): "))
            if 1 <= comfort_level <= 5:
                return comfort_level
            else:
                print("Comfort level must be an integer between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 5.")



#------------------------------------------------------------------------------------------------

def two_point_crossover(parent1, parent2):

    # turn parents into lists for crossover
    keys = list(parent1.keys())
    child1, child2 = parent1.copy(), parent2.copy()

    # random two crossover points from 1,5(length of the chromosome)
    point1, point2 = sorted(random.sample(range(1,len(keys)), 2))
    # print(" point 1 is : \n", point1)
    # print(" ponit 2 is : \n", point2) just checking 



    # swap genes between the two points
    for i in range(point1, point2):
        child1[keys[i]], child2[keys[i]] = parent2[keys[i]], parent1[keys[i]]

    return child1, child2


#------------------------------------------------------------------------------------------------

def mutate(individual, mutation_rate=0.1):
    # go through each gene in the chromosome, generate random probability for gene,
    # if less than mutation rate(0.1) then replace gene with a random choice from the catagories
    for key in individual:
        if random.random() < mutation_rate:
            individual[key] = random.choice(categories[key])
            # print("there has been a mutation in key"+key) just checking 
    return individual

#------------------------------------------------------------------------------------------------

def evolve_population(pop_size, max_generations, target_dress_code, target_color, budget, comfort_level, mutation_rate=0.1):
    # Initialize population
    population = create_initial_population(pop_size)
    generation = 0
    
    while generation < max_generations :
        # Calculate fitness for each individual
        fitnesses = [calculate_fitness(ind, target_dress_code, target_color, budget, comfort_level) for ind in population]
        best_fitness = max(fitnesses)
        
        # Selection and next generation creation
        new_population = []
        for _ in range(pop_size // 2):  # Generate the new population
            parent1, parent2 = binary_tournament_selection(population, fitnesses)
            child1, child2 = two_point_crossover(parent1, parent2)
            new_population.extend([mutate(child1, mutation_rate), mutate(child2, mutation_rate)])
        
        population = new_population
        generation += 1

    # Return the best individual and its fitness from the final generation
    best_individual = max(population, key=lambda ind: calculate_fitness(ind, target_dress_code, target_color, budget, comfort_level))
    return calculate_fitness(best_individual, target_dress_code, target_color, budget, comfort_level), generation


#------------------------------------------------------------------------------------------------

def main():
    print("Welcome to PerfectFit!")
    
    # Get user inputs
    target_dress_code = get_valid_dress_code()
    target_color = get_valid_color_palette()
    budget = get_valid_budget()
    comfort_level = get_valid_comfort_level()

    # Experiment settings
    pop_size = 10
    max_generations = 20000  
    num_runs = 20
    
    population = create_initial_population(pop_size)

    #checking 
    #print(population)

    # Calculate fitness for each individual
    fitnesses = [calculate_fitness(individual, target_dress_code, target_color, budget, comfort_level) for individual in population]
    
    #checking
    #print(fitnesses)

    # Selection
    new_population = []
    for _ in range(5): #replacing whole population once
        parent1, parent2 = binary_tournament_selection(population, fitnesses)
        child1, child2= two_point_crossover(parent1,parent2)
        child1, child2= mutate(child1),mutate(child2)
        new_population.append(child1)
        new_population.append(child2)


    print(" parent 1 is : \n", parent1)
    print("------------------------------------------------------------------")
    print("parent 2 is : \n", parent2)
    print("------------------------------------------------------------------")
    
    # just checking 
    # print("child 1 is : \n", child1)
    # print("------------------------------------------------------------------")
    # print("child 2 is : \n", child2)
    # print("------------------------------------------------------------------")
    # for item in new_population:
    #     print(item)

    # Termination Condition
    total_fitness = 0
    for run in range(num_runs):
        final_fitness, generations = evolve_population(pop_size, max_generations, target_dress_code, target_color, budget, comfort_level)
        total_fitness += final_fitness
        print(f"Run {run + 1}: Final fitness = {final_fitness:.4f} after {generations} generations")

    # Calculate and report the average fitness
    average_fitness = total_fitness / num_runs
    print(f"\nAverage fitness over {num_runs} runs: {average_fitness:.4f}")

if __name__ == "__main__":
    main()



