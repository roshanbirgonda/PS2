# upscaling.py
import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


global match_ratio 


def extract_keywords(prompt):
    print("Extracting kywords!!")
    stop_words = {'give', 'me', 'a', 'with', 'the', 'to', 'is', 'as', 'an', 'in'}
    prompt = re.sub(r'[^\w\s]', '', prompt)
    words = prompt.lower().split()
    keywords = [word for word in words if word not in stop_words]
    return keywords

def jaccard_similarity(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    return float(len(s1.intersection(s2)) / len(s1.union(s2)))

def find_best_match(keywords, descriptions):
    best_match = None
    highest_ratio = 0
    for description in descriptions:
        description_keywords = description.lower().split()
        match_ratio = jaccard_similarity(keywords, description_keywords)
        if match_ratio > highest_ratio:
            highest_ratio = match_ratio
            best_match = description
    return best_match

def create_system_prompt(best_match, description):
    print("Creating system prompt")
    if match_ratio < 0.2:
        system_prompt = (
        "### System Prompt: I want you to act as an IC designer, and implement the following in Verilog.### "
        f"Instruction: Generate a Verilog module with the following description: "
        f"Matching Module: {best_match}"
        )
    system_prompt = (
        "### System Prompt: I want you to act as an IC designer, and implement the following in Verilog.### "
        f"Instruction: Generate a Verilog module with the following description: {description} "
        f"Matching Module: {best_match}"
    )
    return system_prompt

def load_modules_from_excel(file_path):
    df = pd.read_excel(file_path)
    module_names = df['module'].tolist()
    # print(module_names)
    descriptions = df['description'].tolist()
    print("Loading modules")
    return df, module_names, descriptions

def generate_system_prompt(user_prompt, file_path='temp_dataset.xlsx'):
    print("recieved the user_prompt")
    df, module_names, descriptions = load_modules_from_excel(file_path)
    print(descriptions)
    keywords = extract_keywords(user_prompt)
    best_match = find_best_match(keywords, descriptions)

    if best_match:
        system_prompt = create_system_prompt(best_match, best_match)
        return system_prompt
    else:
        system_prompt = "I want you to act as an IC designer, and implement the following in Verilog."
        description = "Generate a Verilog module with the following description: FIFO module with simple read and write functionality"
        return system_prompt + " " + description +" " + user_prompt
