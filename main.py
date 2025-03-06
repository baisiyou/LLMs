import pandas as pd
import random
import os  # Import the os module

def generate_essay(topic):
    """
    Generates a more complex essay based on the given topic.
    Adds random elements to increase the variance in LLM scores.
    """
    sentences = [
        f"This essay will delve into the complexities of {topic}.",
        f"{topic} is a multifaceted issue with far-reaching consequences.",
        f"A critical examination of {topic} reveals several key insights.",
        f"The importance of {topic} cannot be overstated in today's society.",
        f"Exploring the nuances of {topic} is essential for a comprehensive understanding."
    ]
    essay = ""
    for i in range(5):  # Generate 5 sentences
        essay += random.choice(sentences) + " "
        if random.random() < 0.3:  # Add a weird word with 30% probability
            essay += random.choice(["plucrareal", "flibbertigibbet", "gobbledygook"]) + " "
    essay += "In conclusion, further research into " + topic + " is warranted."
    words = essay.split()
    essay = " ".join(words[:100])  # Truncate to 100 words
    return essay

# Read the test.csv file
try:
    test_df = pd.read_csv("test.csv")
    print("test_df.head():\n", test_df.head())  # Print the first few rows of test_df
except FileNotFoundError:
    print("Error: test.csv file not found.")
    print(f"Current directory: {os.getcwd()}")  # Print the current working directory
    print(f"Files in directory: {os.listdir()}")  # Print the files in the directory
    exit()

# Create the submission.csv file
submission_data = []  # Use a list to build the submission data

# Process each row
for index, row in test_df.iterrows():
    id = row["id"]
    topic = row["topic"]
    essay = generate_essay(topic)
    print(f"Generated essay for id {id}: {essay}")  # Print the generated essay
    submission_data.append({"id": id, "essay": essay})

print("submission_data[:5]:\n", submission_data[:5])  # Print the first few elements of submission_data

submission_df = pd.DataFrame(submission_data)  # Create DataFrame from list of dictionaries
print("submission_df.head():\n", submission_df.head())  # Print the first few rows of submission_df

# Save to submission.csv
submission_df.to_csv("submission.csv", index=False)  # Use the default comma separator