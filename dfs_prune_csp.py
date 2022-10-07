ordering = ["H", "C", "D", "F", "E", "G", "A", "B"]
variable_list = {}
for var in ordering:
    variable_list[var] = 0
# variable_list = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0}

# The purpose of this variable is to find the next variable which is unfilled, 
# ie. still assigned 0
def find_next_variable(variable_list):
    for key, value in variable_list.items():
        if value == 0:
            return key
    return None

def is_valid(variable_list, variable, num):
    # A copy of the variables are copied to new_list
    # This new_list only contains the variables that have been assigned values so far
    new_list = {}
    for key, value in variable_list.items():
        if value != 0:
            new_list[key] = value
    new_list[variable] = num
    
    for key, value in new_list.items():
        # Does a constraint check for each key
        if key == "A":
            if "G" in new_list.keys():
                if new_list["A"] <= new_list["G"]:
                    return False
            if "H" in new_list.keys():
                if new_list["A"] > new_list["H"]:
                    return False
        if key == "B":
            if "F" in new_list.keys():
                if abs(new_list["F"] - new_list["B"]) != 1:
                    return False
        if key == "C":
            if "G" in new_list.keys():
                if abs(new_list["G"] - new_list["C"]) != 1:
                    return False
            if "H" in new_list.keys():
                if abs(new_list["H"] - new_list["C"])%2 == 1:
                    return False
            if "D" in new_list.keys():
                if new_list["C"] == new_list["D"]:
                    return False
            if "E" in new_list.keys():
                if new_list["C"] == new_list["E"]:
                    return False
            if "F" in new_list.keys():
                if new_list["C"] == new_list["F"]:
                    return False
        if key == "D":
            if new_list["D"] == new_list["C"]:
                return False
            if "H" in new_list.keys():
                if new_list["D"] == new_list["H"]:
                    return False
            if "E" in new_list.keys():
                if new_list["E"] >= (new_list["D"] - 1):
                    return False
            if "G" in new_list.keys():
                if new_list["D"] < new_list["G"]:
                    return False
            if "F" in new_list.keys():
                if new_list["D"] == (new_list["F"] - 1):
                    return False
        if key == "E":
            if "F" in new_list.keys():
                if abs(new_list["E"] - new_list["F"])%2 == 0:
                    return False
            if new_list["E"] == new_list["C"]:
                return False
            if new_list["E"] >= (new_list["D"] - 1):
                return False
            if "H" in new_list.keys():
                if new_list["E"] == (new_list["H"] - 2):
                    return False
        if key == "F":
            if "G" in new_list.keys():
                if new_list["F"] == new_list["G"]:
                    return False
            if "H" in new_list.keys():
                if new_list["F"] == new_list["H"]:
                    return False
            if abs(new_list["F"] - new_list["B"]) != 1:
                return False
            if new_list["C"] == new_list["F"]:
                return False
            if new_list["D"] == (new_list["F"] - 1):
                return False
        if key == "G":
            if abs(new_list["G"] - new_list["C"]) != 1:
                return False
            if new_list["G"] == new_list["F"]:
                return False
            if "H" in new_list.keys():
                if new_list["G"] >= new_list["H"]:
                    return False
            if new_list["D"] < new_list["G"]:
                return False
        if key == "H":
            if new_list["A"] > new_list["H"]:
                return False
            if abs(new_list["H"] - new_list["C"])%2 == 1:
                return False
            if new_list["F"] == new_list["H"]:
                return False
            if new_list["H"] == new_list["D"]:
                return False
            if new_list["G"] >= new_list["H"]:
                return False
            if new_list["E"] == (new_list["H"] - 2):
                return False
    return True

def print_list(variable_list, variable, num, TF):
    new_list = {}
    for key, value in variable_list.items():
        if value != 0:
            new_list[key] = value
    new_list[variable] = num
    
    if TF == True:
        print(str(new_list) + "--> Solution")
    else:
        print(str(new_list) + "--> Failure")
        
num_failed = 0
solutions = []
        
def dfs_prune(variable_list):
    global num_failed
    global solutions
    variable = find_next_variable(variable_list)
    # This is a base case: when all elements in variable_list is filled,
    # It means that a solution is found
    if variable is None:
        return True
    for num in range(1,5):
        # Checks if each given value in range(1,5) is valid for the given variable        
        if is_valid(variable_list, variable, num):
            variable_list[variable]=num
            print_list(variable_list, variable, num, True)
            # If base case is reached, add the solution to the global solutions variable
            if dfs_prune(variable_list):
                solution = variable_list.copy() 
                solutions.append(solution)
            variable_list[variable]=0
        else:
            num_failed += 1
            print_list(variable_list, variable, num, False)
    return False

dfs_prune(variable_list)
print("\n")
# print("Solution is: " + str(variable_list))
print("The solutions are:")
for solution in solutions:
    print(solution)
print("Number of failed branches: " + str(num_failed))
