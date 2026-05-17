"""
Program to store monster cards for a card game
By Michael Chiu
Version 5, Component 4: Delete monster card function
17-5-26
"""

import easygui

# CONSTANTS v1
MIN_STAT = 1
MAX_STAT = 25


# catalogue dictionary v1
monster_catalogue = {
    "Stoneling" : {"Strength": 7, "Speed": 1, "Stealth": 25,"Cunning": 15},
    "Vexscream" : {"Strength": 1, "Speed": 6, "Stealth": 21,"Cunning": 19},
    "Dawnmirage" : {"Strength": 5, "Speed": 15, "Stealth": 18,"Cunning": 22},
    "Blazegolem" : {"Strength": 15, "Speed": 20, "Stealth": 23,"Cunning": 6},
    "Websnake" : {"Strength": 7, "Speed": 15, "Stealth": 10,"Cunning": 5},
    "Moldvine" : {"Strength": 21, "Speed": 18, "Stealth": 14,"Cunning": 5},
    "Vortexwing" : {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
    "Rotthing" : {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
    "Froststep" : {"Strength": 14, "Speed": 14, "Stealth": 17,"Cunning": 4},
    "Wispghoul" : {"Strength": 17, "Speed": 19, "Stealth": 3,"Cunning": 2},
}

# defining stats v1
STAT_CATEGORIES = ["Strength", "Speed", "Stealth", "Cunning"]

# functions

# add monster function v3
def add_monster():
    new_name = easygui.enterbox("Please enter the name of the new monster you wish to add:",
                                "New monster name")
    
    # in case user selected 'cancel'
    if not new_name:
        return
    
    # ensure new monster is not already in catalogue
    new_name = new_name.title().strip()
    if new_name in monster_catalogue:
        easygui.msgbox(f"It seems {new_name} is already in the monster catalogue.", "Error")
        return
    
    temporary_stats = {}
    # use for loop with STAT_CATEGORIES to loop through all 4 stats
    for stat in STAT_CATEGORIES:
        value = easygui.integerbox(f"Enter the {stat} value for {new_name}:"
                                   f"\n(Must be between {MIN_STAT}-{MAX_STAT})", 
                                  f"{stat} Input", 
                                  lowerbound = MIN_STAT, 
                                  upperbound = MAX_STAT)
    
    # in case user hit 'cancel'
        if value is None:
            easygui.msgbox("Monster creation cancelled.", "Cancelled")
            return
    
        temporary_stats[stat] = value

    # confirm new monster details
    summary = f"Statistics for {new_name}:\n"
    for stat, value in temporary_stats.items():
        summary += f"- {stat}: {value}\n"
    summary += "\nAre these details correct?"

    confirmation = easygui.buttonbox(summary, "Confirm Details", choices=["Confirm", "Discard"])

    if confirmation == "Confirm":
        # add "temporary stats" to actual catalogue
        monster_catalogue[new_name] = temporary_stats
        easygui.msgbox(f"{new_name} has been added to the catalogue!", "Success")
    else:
        easygui.msgbox("Monster data discarded.\nThe new monster has not been added.", "Discarded")


# search/edit monster card function v4
def search_edit_monster():
    searched_name = easygui.enterbox("Please enter the name of the monster you want " \
                                        "to search:", "Search monster").title().strip()
    
    # check to see if searched monster is in catalogue
    if searched_name in monster_catalogue:
        monster_data = monster_catalogue[searched_name]
        
        # summary of stats of searched monster
        stats_summary = f"Monster: {searched_name}\n"
        for stat, value in monster_data.items():
            stats_summary += f"- {stat}: {value}\n"

        # ask user if they wish to edit searched monster
        choice = easygui.buttonbox(f"Current Stats:\n{stats_summary}\nWhat would you like to do?", 
                                   "Monster Found", 
                                   choices=["Edit Stats", "Return to main menu"])
            
        if choice == "Edit Stats":
            # user inputs new values for each stat
            temp_stats = {}
            for stat in STAT_CATEGORIES:
                new_value = easygui.integerbox(f"Enter NEW {stat} value for {searched_name}:"
                                               f"\n(Must be between {MIN_STAT}-{MAX_STAT})", 
                                               f"Edit {stat}", 
                                               lowerbound=MIN_STAT, 
                                               upperbound=MAX_STAT)
                
                # if user selects cancel
                if new_value is None:
                    easygui.msgbox("Edit cancelled. No changes were saved.", "Cancelled")
                    return
                
                temp_stats[stat] = new_value
            
            # update dictionary
            monster_catalogue[searched_name] = temp_stats
            easygui.msgbox(f"All stats for '{searched_name}' have been successfully updated!", "Success")
    
    else:
        # if monster not found in catalogue
        easygui.msgbox(f"Sorry, '{searched_name}' was not found in the catalogue.", "Not Found")

# delete monster card function v5
def delete_monster():
    # gets list of all monster cards
    catalogue = list(monster_catalogue.keys())

    # allow user to select which monster card to delete from the catalogue
    monster_to_delete = easygui.choicebox("Please select the monster you wish to delete:",
                                          "Delete monster card", choices = catalogue)
    
    # ask user to confirm the delete
    if monster_to_delete:
        confirm = easygui.buttonbox(f"Are you sure you want to delete '{monster_to_delete}'?"
                                    "\nWARNING: This action cannot be undone!", 
                                    "Confirm Delete", 
                                    choices = ["Yes, Delete", "No, Cancel"])
        
        if confirm == "Yes, Delete":
            # removes the combo
            del monster_catalogue[monster_to_delete]
            easygui.msgbox(f"'{monster_to_delete}' has been removed from the monster catalogue.")
        else:
            easygui.msgbox("Delete cancelled.")
    

def print_catalogue():
    pass

# main program 
easygui.msgbox("Welcome to the Monster Card catalogue.\nMany monsters await to be unleashed!",
                "Welcome message")

# while loop v2
while True:
    option = easygui.buttonbox("What would you like to do?\n Please select from the options below:",
                                "Main menu",
                      choices = ["Add monster", "Search/Edit monster", "Delete monster", 
                                 "Print catalogue", "Exit program"])

    if option == "Add monster":
        add_monster()
        
    elif option == "Search/Edit monster":
        search_edit_monster()

    elif option == "Delete monster":
        delete_monster()

    elif option == "Print catalogue":
        # temporary code to view catalogue and ensure functions like add monster and 
        # search/edit monster works properly, will be replaced in v6 for actual print function
        easygui.msgbox(f"{monster_catalogue}") 

    else:
        break

easygui.msgbox("Thank you for using the Monster Catalogue Program. Goodbye!"
               , "Goodbye message")
    