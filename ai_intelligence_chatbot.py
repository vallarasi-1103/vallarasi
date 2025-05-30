# -*- coding: utf-8 -*-
"""AI intelligence chatbot

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11MPI8d6GyON9924DN7aWNZ3m3tRA0ksi
"""



# Simple AI Travel Chatbot (no external datasets)

print("🌍 Welcome to the AI Travel Assistant!")
print("Type 'help' to see available commands.\n")

# Sample in-memory data
cab_data = {
    "mumbai": ["Ola Sedan - Available", "Uber Mini - 5 mins away"],
    "new york": ["Yellow Cab - Available", "Lyft - 3 mins away"],
    "delhi": ["Uber Auto - 2 mins away"],
}

hotel_data = {
    "mumbai": ["Taj Palace", "Hotel Sea View"],
    "new york": ["Marriott Times Square", "The Plaza Hotel"],
    "delhi": ["The Lalit", "Radisson Blu"],
}

travel_tips = {
    "general": "Always carry valid ID proof and check weather forecasts before traveling.",
    "mumbai": "Try local street food like Vada Pav!",
    "new york": "Use the subway to avoid traffic.",
    "delhi": "Visit monuments early to avoid crowds.",
}

# Help menu
def show_help():
    print("\n📘 Available Commands:")
    print("- cab status in <city>      → Shows available cabs in the city")
    print("- hotel in <city>           → Shows hotel suggestions in the city")
    print("- travel tips for <city>    → Gives travel advice for the city")
    print("- help                      → Shows this help message")
    print("- exit                      → Exits the chatbot\n")

# Main loop
while True:
    user_input = input("You: ").strip().lower()

    if user_input == "exit":
        print("👋 Goodbye! Have a safe journey!")
        break

    elif user_input == "help":
        show_help()

    elif user_input.startswith("cab status in"):
        city = user_input.replace("cab status in", "").strip()
        cabs = cab_data.get(city)
        if cabs:
            print(f"🚗 Available cabs in {city.title()}:")
            for cab in cabs:
                print(f" - {cab}")
        else:
            print(f"🚫 No cab data found for {city.title()}.")

    elif user_input.startswith("hotel in"):
        city = user_input.replace("hotel in", "").strip()
        hotels = hotel_data.get(city)
        if hotels:
            print(f"🏨 Hotels in {city.title()}:")
            for hotel in hotels:
                print(f" - {hotel}")
        else:
            print(f"🚫 No hotel suggestions available for {city.title()}.")

    elif user_input.startswith("travel tips for"):
        city = user_input.replace("travel tips for", "").strip()
        tip = travel_tips.get(city, travel_tips["general"])
        print(f"✈️ Travel Tip for {city.title()}: {tip}")

    else:
        print("❓ Sorry, I didn't understand that. Type 'help' to see what I can do.")