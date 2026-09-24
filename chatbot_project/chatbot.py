print("Welcome! i am your role_based AI chatbot")
print("type 'bye','exit','quit',to leave ")

while True:
    user_input = input("you :").lower().strip()

    if user_input in ["hello","hi","hey"]:
     print("bot : hi how can i help you today?")

    elif user_input in ["how are you"]:
       print("bot : i am fine ")

    elif user_input in ["what is your name? "]:
       print("bot :my name is role_based AI chatbot")

    elif user_input in ["what do you do"]:
       print("bot: i can respond to questions") 

    elif user_input in ["what is your purpose?"]:
       print("bot: my purpose is to assist you with your queries")

    elif user_input in ["what is your favorite color?"]:
       print("bot: my favorite color is blue")

    elif user_input in ["what is your favorite food?"]:
       print("bot: my favorite food is pizza")

    elif user_input in ["what is your favorite movie?"]:
       print("bot: my favorite movie is Inception")
    elif user_input in ["what is AI"]:
       print("bot: AI stands for Artificial Intelligence, which is the simulation of human intelligence in machines that are programmed to think and learn like humans.")
    elif user_input in ["what is machine learning"]:
       print("bot: Machine learning is a subset of AI that involves training algorithms to learn patterns from data and make predictions or decisions without being explicitly programmed.")
    elif user_input in ["what is deep learning"]:
       print("bot: Deep learning is a subset of machine learning that uses artificial neural networks to model and solve complex problems, often involving large amounts of data.")
    elif user_input in ["thank you","thanks"]:
       print("bot: you're welcome! if you have any more questions, feel free to ask.")
    elif user_input in ["bye","exit","quit"]:
       print("good bye: have a great day")
       break
    else:
       print("bot: i don't understand")       

