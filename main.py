import random

# A small mood-to-outfit dictionary
outfit_suggestions = {
    "happy": [
        "a bright Yellow t-shirt with comfy jeans 👕",
        "a fresh Green kurta with white pants ✨"
    ],
    "calm": [
        "a Blue shirt with black trousers 😌",
        "a White kurta for simple vibes 🕊️"
    ],
    "confident": [
        "a Red formal shirt with black pants 🔥",
        "a Black blazer with denim jeans 💼"
    ],
    "energetic": [
        "an Orange sports t-shirt with shorts 🏃",
        "a Yellow hoodie with joggers ⚡"
    ],
    "stressed": [
        "a Green casual outfit to relax 🌿",
        "a Blue kurta to feel at peace 🌊"
    ]
}

print("👗 Welcome to the Color Psychology Outfit Recommender! 👔\n")

# Ask the user about their mood
mood = input("How are you feeling today? (happy, calm, confident, energetic, stressed): ").lower()

# Check if we have an outfit for this mood
if mood in outfit_suggestions:
    choice = random.choice(outfit_suggestions[mood])
    print(f"\nYou're feeling {mood.capitalize()} today 🌟")
    print(f"My outfit suggestion: Try wearing {choice}")
else:
    print("\nOops! I don’t have suggestions for that mood yet 😅")
