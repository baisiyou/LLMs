Rubing Zhang: # LLM Judge Exploitation Competition

## Overview
This competition challenges participants to identify exploits for an **LLM-as-a-judge** system designed to evaluate essay quality. The goal is to **maximize disagreement** between the three LLM judges while ensuring:

- The essay is written in **English**.
- The content is **non-repetitive**.
- The essay follows the given **topic**.

Your work will contribute to a better understanding of the limitations of LLM-based subjective evaluation systems.

---

## 🏆 Competition Objective
The primary objective is to create essays that cause **maximum disagreement** between the three LLM judges. Each essay submission will be evaluated using the following criteria:

- **Quality Score (avg_q)**: The average quality score assigned by the three LLM judges, ranging from **0 to 9**.
- **Horizontal Variance (avg_h)**: Measures the variance between the scores given by the three judges **for a single essay**.
- **Vertical Variance (min_v)**: The minimum variance across all essays, measuring how much a single judge varies across multiple essays.
- **English Confidence Score (avg_e)**: A float value between **0 and 1**, penalizing non-English essays.
- **Sequence Similarity Score (avg_s)**: A float value between **0 and 1**, penalizing repetitive approaches. This score has a lower bound of **0.2**.

The **final score** is calculated as follows:

```
avg_q = avg([avg_quality_scores])
avg_h = avg([horizontal_stdevs])
min_v = min([vertical_stdevs])
avg_s = max(avg_s, 0.2)
```

---

## 📌 Implementation Details
This repository contains a Python script `main.py` that generates submission essays based on the given competition criteria.

### **Files in this repository:**
- `main.py`: The main script for generating essays based on given topics.
- `test.csv`: The input file containing essay topics.
- `submission.csv`: The output file containing generated essays.

### **Essay Generation Approach**
The script generates an essay for each given topic by:
- Constructing **varied sentence structures**.
- Introducing **random elements** to increase LLM judge disagreement.
- Avoiding **repetition** to maximize the **sequence similarity score** penalty.

Example function to generate an essay:

```python
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
```

---

## 🔄 Submission Process
The script processes a **test.csv** file containing topics and generates **submission.csv** with essays.

1. **Ensure** you have a `test.csv` file with at least one column:
   ```
   id,topic
   1,Artificial Intelligence and Society
   2,Impact of Climate Change
   ```

2. **Run the script**:
   ```bash
   python main.py
   ```

3. **Check** the generated `submission.csv`:
   ```
   id,essay
   1,"This essay will delve into the complexities of Artificial Intelligence and Society..."
   2,"The importance of Climate Change cannot be overstated in today's society..."
   ```

4. **Submit** `submission.csv` to the competition platform.

---

## 🔧 Troubleshooting
If the script fails due to a missing `test.csv`, check the current directory:

```python
import os
print("Current directory:", os.getcwd())
print("Files in directory:", os.listdir())
```

If `test.csv` is missing, ensure it is placed in the same directory as `main.py` before running the script.

---

## 📜 Acknowledgments
This work is based on competition guidelines and leverages **randomization techniques** to exploit potential weaknesses in LLM judgment models.

For more details, refer to the **official competition page**.

---

## 📩 Contact
For any issues or questions, feel free to reach out via the competition discussion forum.

Happy competing! 🚀

