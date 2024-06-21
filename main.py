import re
# testing change
def web():
    from bs4 import BeautifulSoup
    import requests
    while True:
        ans = "Exited from web"
        search = input("Enter your question for web search (Type exit to exit): ")
        if search.lower() == "exit":
            break
        response = requests.get("https://www.google.com/search", params={'q': search})
        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = soup.find_all('div', class_='BNeawe')
        if search_results:
            ans = search_results[0].text
            print(f"Chatbot:{ans}")
        else:
            ans = "Error during web search. Try again..."
    return ans
def chatbot_response(user_input):

    user_input = user_input.lower()
    
    if re.search(r'\bhello\b|\bhi\b|\bhey\b', user_input):
        return "Hello! How can I assist you today?"
    elif re.search(r'\bweb\b', user_input):
        return web()
    elif re.search(r'\bhow are you\b', user_input):
        return "I'm just a bunch of code, but I'm doing great! How about you?"
    elif re.search(r'\b(your name|who are you)\b', user_input):
        return "I am a simple chatbot created to assist you."
    elif re.search(r'\bwhat can you do\b', user_input):
        return "I can answer basic questions and have simple conversations. Try asking me something!"
    elif re.search(r'\b(capital of france|paris)\b', user_input):
        return "The capital of France is Paris."
    elif re.search(r'\bbye\b|\bgoodbye\b', user_input):
        return "Goodbye! Have a great day!"
    elif re.search(r'\btime\b', user_input):
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%I:%M%p')}."
    elif re.search(r'\bdate\b', user_input):
        from datetime import datetime
        return f"Today's date is {datetime.now().strftime('%d %B %Y')}."
    elif re.search(r'\bweather\b', user_input):
        return "I can't check the weather right now, but you can try a web search by typing 'web'"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase? [If you think this information is not available with me, try typing 'web']"

def main():
    print("Welcome to the Simple Chatbot! Type 'bye' to exit and 'web' to perform an internet search.")
    while True:
        user_input = input("You: ")
        if re.search(r'\bbye\b|\bgoodbye\b', user_input.lower()):
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
