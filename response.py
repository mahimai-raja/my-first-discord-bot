from random import randint

def handle_response(message) -> str:
    p_message = message.lower()
    
    if p_message == 'hello':
        return 'hey there'

    if p_message == 'who are you':
        return 'I am virtual bot'   
    
    if p_message == 'when did you born':
        return 'I was programmed on 17th November 2022' 
    
    if p_message == 'ikurious bot' or p_message == 'ikuriousbot' :
        return 'My predefined commands are \n-> hello\n-> who are you\n-> when did you born\n-> roll'   

    if p_message == 'roll':
        return str(randint(1,6))

    if p_message == '!help':
        return f"How an I help you {message.author}"

