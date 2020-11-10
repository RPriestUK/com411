import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
import basics.output.ascii_art as ascii_art
import basics.output.escape_characters as escape_characters

def run_block_a():
    # Ask user which program they want to run
    print("\nWhich program in 'Block A: Basics' do you wish to run?")
    print("[a] Run 'Simple Message'")
    print("[b] Run 'Multiline Message'")
    print("[c] Run 'ASCII art'")
    print("[d] Run 'Escape Characters'")
    print("[exit] Return to Main Menu")
    response = str(input())
    # Use user's choice to open program or return to main menu
    if (response.lower() == "a"):
        simple_message.run()
    elif (response.lower() == "b"):
        multiline_message.run()
    elif (response.lower() == "c"):
        ascii_art.run()
    elif (response.lower() == "d"):
        escape_characters.run()
    elif (response.lower() == "exit"):
        main_menu(True)
    else: 
        main_menu(True)

def main_menu(is_running):
  while(is_running):
      # Ask user what they'd like to do
      print("\nWhat would you like to do?")
      print("[a] Run 'Block A: Basics' programs")
      print("[q] Quit")
      response = str(input())
      # Use user's choice to open Block A or quit
      if (response.lower() == "a"):
        run_block_a()
      elif (response.lower() == "q"):
        break
      else:
        print("Please choose a valid option.")

def run():
    is_running = True

    # Launch the main menu
    main_menu(is_running)
    
# Start the program
# run()
