import tkinter as tk

 

def submit_entry():

    name = name_entry.get()

    player_tag = tag_entry.get()

    character = character_entry.get()

 

    #add more validation and processing logic here

    if character == "Mario":
        
        
        print(f"You picked {character}, great choice!")
        
    if character == "Donkey Kong":
        
        
        print(f"You picked {character}, nice one!")

    if character == "Link":
        
        
        print(f"{character}, He rules!")

    if name == "":

        print(f"No entry")



    # print the entered information

    print(f"Name: {name}")

    print(f"Player Tag: {player_tag}")

    print(f"Character: {character}")

    print("Entry submitted!")

 

# create the main window

root = tk.Tk()

root.title("Super Smash Bros Ultimate Tournament Sign-Up")

# window configuration
root.geometry('300x350')

 

# create and place widgets

label_name = tk.Label(root, text="Name:")

label_name.pack(pady=10)

 

name_entry = tk.Entry(root)

name_entry.pack(pady=10)

 

label_tag = tk.Label(root, text="Player Tag:")

label_tag.pack(pady=10)

 

tag_entry = tk.Entry(root)

tag_entry.pack(pady=10)



label_character = tk.Label(root, text="Main Character:")

label_character.pack(pady=10)


character_entry = tk.Entry(root)

character_entry.pack(pady=10)

 

submit_button = tk.Button(root, text="Submit Entry", command=submit_entry)

submit_button.pack(pady=20)

 

# start the GUI event loop

root.mainloop()
