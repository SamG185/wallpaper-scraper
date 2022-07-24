import PySimpleGUI as sg


def window_input():
    
    # Define the window's contents
    layout = [[sg.Text("What type of wallpaper do you want?")],
            [sg.Listbox(values = ["Animal", "Anime", "Background", "Brand", "Car", "Cartoon", "Color", "Device", "Disney", "Fantasy", "Flower", "Gaming", "Holiday", "Horror", "Movie", "Music", "Nature", "Others", "religious", "Space", "Sports", "Superhero", "Travel", "Tv Shows"], size = (40, 5))],
            [sg.Text("", key = "below_list")],
            [sg.Button('Ok'), sg.Button('Quit')]]

    # Create the window
    window = sg.Window(title = "Web Scraper", layout = layout, size = (1280, 500))

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        # Output a message to the window
        if event == 'Ok':
            try:
                wallpaper_type = values[0][0]
                window["below_list"].update(value = "Changing desktop background to something " + wallpaper_type + " themed.")
                return wallpaper_type
            except:
                window["below_list"].update(value = "Please select an option from the list")

            
    # Finish up by removing from the screen
    window.close()