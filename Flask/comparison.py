from sklearn.metrics import precision_score, recall_score, f1_score

def tokenize(text):
    return text.split()  # Simple word tokenization

def calculate_scores(predicted, expected):
    predicted_tokens = tokenize(predicted)
    expected_tokens = tokenize(expected)
    
    # Create sets for matching
    predicted_set = set(predicted_tokens)
    expected_set = set(expected_tokens)
    
    # Find intersection
    matches = predicted_set.intersection(expected_set)
    
    # Calculate Precision, Recall, F1 Score
    precision = len(matches) / len(predicted_set) if predicted_set else 0
    recall = len(matches) / len(expected_set) if expected_set else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) else 0
    
    # Exact Match Score
    exact_match_score = len(matches) / len(expected_set) if expected_set else 0
    
    return {
        'precision': precision,
        'recall': recall,
        'f1_score': f1,
        'exact_match_score': exact_match_score
    }

# Example usage
predicted_output = "module adder(input a, b, output sum);"
expected_output = "module adder(input a, b, output sum); endmodule"
scores = calculate_scores(predicted_output, expected_output)

print(scores)
