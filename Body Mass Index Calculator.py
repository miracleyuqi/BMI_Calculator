# Body Mass Index Loop Program 
# Name: Yuqi Zhou 
# 
# Description 
#   This application is to calculate a person's body mass index and determine the category of it. 
# We will prompt the user to enter height and weight, 
# then check if those values are numeric, and if they are in the valid range. 
# When the input are valid, we will calculate the BMI 
# and then determine its category depending on the value of BMI. 
# At this point, we will ask the user if they want to enter a new set of height and weight. 
# We will validate the answer. If it's neither yes nor no, we will notify the user to enter a valid choice. 
# If the answer is yes, the whole calculation process will start over again. 
# If the answer is no, the application will be ended. 

# Declaration 
# Initialize a Boolean variable to store the determination of 
# if the user want to enter a new set of values. 
enter_another = True 
# Declare three constants for value validation 
MIN_HEIGHT = 24.0 
MAX_HEIGHT = 120.0 
MIN_WEIGHT = 25.0 

# This function is to check if the input of height is numeric. 
# If not, prompt the user to enter a numeric value. 
def Valid_Height(user_entry): 
    try: 
        input_check = float(user_entry) 
        return True
    except: 
        print("Please enter the height as a numeric value.") 
        return False 

# This function is to check if the input is in valid range. 
# If not, prompt the user to enter a value in valid range. 
def Height_Range(user_entry): 
    if MIN_HEIGHT <= float(user_entry) <= MAX_HEIGHT: 
        return True 
    else: 
        print("Please enter the height between 24 and 120 inches.")
        return False 

# This function is to check if the input of weight is numeric. 
# If not, prompt the user to enter a numeric value. 
def Valid_Weight(user_entry): 
    try: 
        input_check = float(user_entry) 
        return True
    except: 
        print("Please enter the weight as a numeric value.") 
        return False 

# This function is to check if the input is in valid range. 
# If not, prompt the user to enter a value in valid range. 
def Weight_Range(user_entry): 
    if MIN_WEIGHT <= float(user_entry): 
        return True 
    else: 
        print("Please enter a weight of at least 25 pounds.") 
        return False 

# A while loop, condition is met when the user is willing to enter a new set.  
while enter_another == True: 
    # Input 
    # Prompt the user to enter value of height, and check if the input is valid. 
    # If not, ask the user to enter again. 
    height = input("Please enter the person's height in inches: ") 
    while Valid_Height(height) == False or Height_Range(height) == False: 
        height = input("Please enter the person's height in inches: ") 
    
    # Prompt the user to enter value of weight, and check if the input is valid. 
    # If not, ask the user to enter again. 
    weight = input("Please enter the person's weight in pounds: ") 
    while Valid_Weight(weight) == False or Weight_Range(weight) == False: 
        weight = input("Please enter the person's weight in pounds: ") 
    
    # Initialize a Boolean variable to store True or False value 
    # of checking if new weight is less than 85% of original weight. 
    weight_check = True 
    # Declare a float variable to store renewed weight value. The first one is equal to the original. 
    weight_new = float(weight) 
    # Declare a float variable to store the limit we set as an exit point. 
    weight_limit = float(weight)*0.85 
    # Initialize a string variable to store the category of BMI. 
    category_bmi = "" 
    # Set up a constant for conversion factor. 
    CONVERSION_FACTOR = 703 
    # Set up 4 constants to set the range of categories of BMI. 
    BMI_SEVERELY_UNDER = 16 
    BMI_UNDER = 18.5 
    BMI_HEALTY = 25 
    BMI_OVER = 30 
    
    # A while loop to calculate BMI and determine the category of BMI, 
    # when new weight is less than 85% of original weight. 
    while weight_check == True: 
        bmi = (float(weight_new)/float(height)**2)*CONVERSION_FACTOR 
        if bmi < BMI_SEVERELY_UNDER: 
            category_bmi = "severely underweight" 
        elif BMI_SEVERELY_UNDER <= bmi < BMI_UNDER: 
            category_bmi = "underweight" 
        elif BMI_UNDER <= bmi < BMI_HEALTY: 
            category_bmi = "healthy" 
        elif BMI_HEALTY <= bmi < BMI_OVER: 
            category_bmi = "overweight" 
        else: 
            category_bmi = "obese" 
                
        # Print out height, weight, result of BMI and its category altogether as a string.   
        print('The BMI for a ' + str(height) + '" tall person who weighs ' + str(weight_new) + ' lb. is ' + str(round(bmi,1)) + ', which is categorized as ' + str(category_bmi) + '.') 

        # Set the increment of weight change as a constant.             
        WEIGHT_INCREMENT = -5 
        # Calculate new weight. 
        weight_new = weight_new + WEIGHT_INCREMENT 
        # Check if new weight is less than 85% of original weight. If yes, end the loop. 
        if weight_new < weight_limit: 
            weight_check = False 
    
    # Ask the user if they want to enter a new set of data. 
    new_input = input("Would you like to enter data for another person? (yes/no): ") 
    
    # If the answer is 'yes', start a new validation and calculation process. 
    # If the answer is 'no', end the application. 
    # If the answer is neither 'yes' nor 'no', prompt the user to enter 'yes' or 'no'. 
    while new_input.strip().lower() != 'yes' and new_input.strip().lower() != 'no': 
        new_input = input("Please enter 'yes' or 'no'. Would you like enter data for another person?: ") 
    if new_input.strip().lower() == "no": 
        enter_another = False 
    else: 
        enter_another = True 
    