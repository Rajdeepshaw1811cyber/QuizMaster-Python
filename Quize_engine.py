
sports_questions = [
    ["Which country hosted the men's FIH Hockey World Cup in 2023, where India finished in the joint ninth position?",
     ["A. Australia", "B. India", "C. Netherlands", "D. Belgium"], "B"],

    ["In international badminton, which Indian player won the bronze medal at the 2012 London Olympics?",
     ["A. P. V. Sindhu", "B. Saina Nehwal", "C. Jwala Gutta", "D. Ashwini Ponnappa"], "B"],

    ["How many players make up a single active team on the mat during a Pro Kabaddi League match?",
     ["A. 5", "B. 6", "C. 7", "D. 9"], "C"],

    ["Which Indian cricketer holds the record for highest individual score in Men's ODI (264 runs)?",
     ["A. Sachin Tendulkar", "B. Virat Kohli", "C. Rohit Sharma", "D. Virender Sehwag"], "C"],

    ["At which Olympic Games did Karnam Malleswari become the first Indian woman to win an Olympic medal?",
     ["A. 1996 Atlanta", "B. 2000 Sydney", "C. 2004 Athens", "D. 2008 Beijing"], "B"],

    ["Which Indian chess grandmaster became the youngest player ever to defeat reigning World Champion Magnus Carlsen in 2022?",
     ["A. Viswanathan Anand", "B. Vidit Gujrathi", "C. Rameshbabu Praggnanandhaa", "D. Pentala Harikrishna"], "C"],

    ["In cricket, what term is used when a batter is dismissed without scoring a single run after facing a delivery?",
     ["A. Clean bowled", "B. Duck", "C. Stumped", "D. Nightwatchman"], "B"],

    ["Which Indian javelin thrower won historic gold at the World Athletics Championships in 2023?",
     ["A. Kishore Jena", "B. Devendra Jhajharia", "C. Neeraj Chopra", "D. D. P. Manu"], "C"],

    ["In field hockey, how many standard quarters are there in an official international match?",
     ["A. 2 halves (45 minutes each)", "B. 3 periods (20 minutes each)", "C. 4 quarters (15 minutes each)", "D. 4 quarters (20 minutes each)"], "C"],

    ["Which tennis doubles pairing became the first Indian pair to win a Grand Slam title together (2012 Australian Open mixed doubles)?",
     ["A. Leander Paes and Sania Mirza", "B. Mahesh Bhupathi and Sania Mirza", "C. Rohan Bopanna and Sania Mirza", "D. Leander Paes and Martina Navratilova"], "B"]
]

science_questions = [
    ["What is the SI unit of electric resistance?",
     ["A. Ampere", "B. Volt", "C. Ohm", "D. Watt"], "C"],

    ["Which part of the human eye regulates the amount of light entering?",
     ["A. Cornea", "B. Retina", "C. Iris", "D. Crystalline lens"], "C"],

    ["Which plant tissue is responsible for transporting water and minerals from roots to leaves?",
     ["A. Phloem", "B. Xylem", "C. Cambium", "D. Cortex"], "B"],

    ["Which mirror is commonly used as a vehicle rear-view mirror for a wider field of view?",
     ["A. Concave", "B. Convex", "C. Plane", "D. Parabolic"], "B"],

    ["What is the pH of a neutral aqueous solution at room temperature?",
     ["A. 0", "B. 7", "C. 14", "D. 1"], "B"],

    ["Which hormone is responsible for lowering blood sugar?",
     ["A. Thyroxine", "B. Adrenaline", "C. Insulin", "D. Growth hormone"], "C"],

    ["What is the nature of the magnetic field inside a long straight current-carrying solenoid?",
     ["A. Zero everywhere", "B. Uniform", "C. Stronger near ends than middle", "D. Non-uniform"], "B"],

    ["Which metal is liquid at room temperature?",
     ["A. Sodium", "B. Mercury", "C. Aluminum", "D. Copper"], "B"],

    ["Who is known as the Father of Genetics?",
     ["A. Charles Darwin", "B. Gregor Mendel", "C. Jean-Baptiste Lamarck", "D. Robert Hooke"], "B"],

    ["What is the medical term for farsightedness, where distant objects are clear but nearby objects are blurred?",
     ["A. Myopia", "B. Hypermetropia", "C. Astigmatism", "D. Cataract"], "B"]
]



gk_questions = [
    ["Which is the largest planet in the solar system?",
     ["A. Earth", "B. Saturn", "C. Jupiter", "D. Neptune"], "C"],

    ["Who wrote the Indian national anthem Jana Gana Mana?",
     ["A. Bankim Chandra Chatterjee", "B. Rabindranath Tagore", "C. Sarojini Naidu", "D. Subhas Chandra Bose"], "B"],

    ["Which is the longest river in the world?",
     ["A. Amazon", "B. Yangtze", "C. Nile", "D. Mississippi"], "C"],

    ["What is the capital of Australia?",
     ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Perth"], "C"],

    ["Which gas do plants primarily absorb during photosynthesis?",
     ["A. Oxygen", "B. Nitrogen", "C. Carbon dioxide", "D. Hydrogen"], "C"],

    ["Who was the first woman Prime Minister of India?",
     ["A. Pratibha Patil", "B. Indira Gandhi", "C. Sarojini Naidu", "D. Sushma Swaraj"], "B"],

    ["On which continent is the Sahara Desert located?",
     ["A. Asia", "B. South America", "C. Africa", "D. Australia"], "C"],

    ["How many bones are there in an average adult human body?",
     ["A. 196", "B. 206", "C. 216", "D. 226"], "B"],

    ["What is the official currency used in Japan?",
     ["A. Yuan", "B. Won", "C. Yen", "D. Baht"], "C"],

    ["Who is widely credited with inventing the telephone?",
     ["A. Thomas Edison", "B. Nikola Tesla", "C. Alexander Graham Bell", "D. Guglielmo Marconi"], "C"]
]

Name=input("Enter your name:")


game_running = True

while game_running:

    print("\n================================")
    print("       WELCOME TO QUIZ ENGINE")
    print("================================")

    print("\nChoose Your Subject:")
    print("1. Sports")
    print("2. Science")
    print("3. General Knowledge")

    choice = input("\nEnter your choice (1-3): ")

    if choice == "1":
        selected_questions = sports_questions
        subject_name = "Sports"

    elif choice == "2":
        selected_questions = science_questions
        subject_name = "Science"

    elif choice == "3":
        selected_questions = gk_questions
        subject_name = "General Knowledge"

    else:
        print("\nInvalid choice! Please select 1, 2 or 3.")
        continue

    score = 0
    correct = 0
    wrong = 0
    question_number = 1

    print("\n================================")
    print("Starting", subject_name, "Quiz")
    print("================================")

    for question in selected_questions:

        print("\n--------------------------------")
        print("Question", question_number)
        print(question[0])

        # DISPLAY OPTIONS
        for option in question[1]:
            print(option)

        # TAKE ANSWER
        answer = input("\nEnter your answer (A/B/C/D): ")
        answer = answer.upper()

        # VALIDATE ANSWER
        while answer not in ["A", "B", "C", "D"]:
            print("Invalid answer! Please enter A, B, C or D.")
            answer = input("Enter your answer: ")
            answer = answer.upper()

        # CHECK ANSWER
        if answer == question[2]:
            print("Correct Answer!")
            score = score + 1
            correct = correct + 1

        else:
            print("Wrong Answer!")
            print("Correct answer:", question[2])
            wrong = wrong + 1

        question_number = question_number + 1


    percentage = (score / 10) * 100

    print("\n================================")
    print(Name," QUIZ RESULT")
    print("================================")

    print("Subject:", subject_name)
    print("Total Questions: 10")
    print("Correct Answers:", correct)
    print("Wrong Answers:", wrong)
    print("Final Score:", score, "/ 10")
    print("Percentage:", percentage, "%")

    # PERFORMANCE MESSAGE
    if score >= 9:
        print("Performance: Excellent!")

    elif score >= 7:
        print("Performance: Very Good!")

    elif score >= 5:
        print("Performance: Good!")

    else:
        print("Performance: Keep Practicing!")


    while True:

        play_again = input("\nDo you want to play another subject? (yes/no): ")
        play_again = play_again.lower()

        if play_again == "yes":
            break

        elif play_again == "no":
            game_running = False
            break

        else:
            print("Invalid input! Please enter yes or no.")

print("\nThank you",Name,"for playing Quiz Engine!")
print("Goodbye!")
