import random

questions = [
    # Shekalim
    "Which parsha is the first of the Four Parshiot?",
    "When is Parshat Shekalim read?",
    "Which parsha is about the obligation of giving the Half-Shekel?",
    "Why do we read Parshat Shekalim?",

    # Zachor
    "Which parsha is the second of the Four Parshiot?",
    "When is Parshat Zachor read?",
    "Which parsha is about the mitzvah of remembering to wipe out Amalek?",
    "Why is Parshat Zachor read before Purim?",

    # Para
    "Which parsha is the third of the Four Parshiot?",
    "When is Parshat Para read?",
    "Which parsha is about the Para Adumah?",
    "Why do we read Parshat Para?",

    # HaChodesh
    "Which parsha is the fourth of the Four Parshiot?",
    "When is Parshat HaChodesh read?",
    "Which parsha is about the mitzvot of Rosh Chodesh and Korban Pesach?",
    "Why do we read Parshat HaChodesh before Pesach?"
]

asked = []

print("\n🎉 FOUR PARSHIOT RANDOM QUESTION GENERATOR 🎉\n")

while True:
    user_input = input("Press ENTER for a question (or type q to quit): ")

    if user_input.lower() == "q":
        print("\nGame Over!")
        break

    if len(asked) == len(questions):
        print("\nAll questions used! Resetting...\n")
        asked = []

    remaining = [q for q in questions if q not in asked]
    question = random.choice(remaining)
    asked.append(question)

    print("\n" + "=" * 70)
    print(question.upper())
    print("=" * 70 + "\n")
