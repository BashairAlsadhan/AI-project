

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




def main():
    
    
    print ("Welcome to  PerfectFit!!!!!!")
    
    
    # Get user input
    target_dress_code = get_valid_dress_code()
    target_color = get_valid_color_palette()
    budget = get_valid_budget()
    comfort_level = get_valid_comfort_level()

    # just for checking 
    #print(target_dress_code)
    #print(target_color)
    #print(budget)
    #print(comfort_level)


    # i put 10 randomaly, as they didnt specify any number (maybe it will be changed in the next phase)
    pop_size = 10

    population = create_initial_population(pop_size)

    #checking 
    #print(population)

    # Calculate fitness for each individual
    fitnesses = [calculate_fitness(individual, target_dress_code, target_color, budget, comfort_level) for individual in population]
    
    #checking   
    #print(fitnesses)

    # Selection
    parent1, parent2 = binary_tournament_selection(population, fitnesses)

    print(" parent 1 is : \n", parent1)
    print("------------------------------------------------------------------")
    print("parent 2 is : \n", parent2)


    

if __name__ == "__main__":
    main()






