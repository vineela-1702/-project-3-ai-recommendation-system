# AI Recommendation Logic Project 3

print("=" * 50)
print("      AI RECOMMENDATION SYSTEM")
print("=" * 50)

recommendations = {
    "Movies": [
        "Avengers",
        "Interstellar",
        "Inception",
        "The Dark Knight",
        "Titanic"
    ],
    "Books": [
        "Atomic Habits",
        "Harry Potter",
        "Rich Dad Poor Dad",
        "The Alchemist",
        "Think and Grow Rich"
    ],
    "Sports": [
        "Cricket",
        "Football",
        "Badminton",
        "Basketball",
        "Tennis"
    ],
    "Music": [
        "Pop Music",
        "Rock Music",
        "Classical Music",
        "Jazz Music",
        "Hip Hop Music"
    ],
    "Technology": [
        "Artificial Intelligence",
        "Machine Learning",
        "Cyber Security",
        "Web Development",
        "Cloud Computing"
    ]
}

while True:

    print("\nAvailable Categories:")
    for category in recommendations:
        print("•", category)

    user_choice = input("\nEnter your interest category: ").title()

    if user_choice in recommendations:

        print("\nRecommended Items For You")
        print("-" * 30)

        count = 1
        for item in recommendations[user_choice]:
            print(f"{count}. {item}")
            count += 1

        print("\nTotal Recommendations:",
              len(recommendations[user_choice]))

    else:
        print("\nSorry! No recommendations found.")
        print("Please select a valid category.")

    again = input("\nDo you want another recommendation? (yes/no): ").lower()

    if again != "yes":
        print("\nThank you for using AI Recommendation System!")
        print("Project 3 Completed Successfully.")
        break
