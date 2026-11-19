mood = input("How are you feeling today? (mood): ")
weather = input("What is the current weather: ")

if mood == "Happy" or mood == "happy" and weather == "Sunny" or weather == "sunny":
    playlist = "Pop hits"
elif mood == "Happy" or mood == "happy" and weather != "Sunny" or weather != "sunny":
    playlist = "Top charts"
elif mood == "Sad" or mood == "sad" and weather == "Rainy" or weather == "Rainy":
    playlist = "Sad Acoustic"
elif mood == "Sad" or mood == "sad" and weather != "Rainy" or weather != "Rainy":
    playlist = "Top Charts"
elif mood == "Relaxed":
    playlist = "Chill Vibes"
else:
    playlist = "Top Charts"
    
print(f"Playlist suggestion: {playlist}")