from capture import capture_screen
from response import get_response

if __name__ =="__main__":
    print("Capturing screen")
    screenshot = capture_screen()
    question = input("What do you want to ask?")
    response = get_response(screenshot,question)
    
