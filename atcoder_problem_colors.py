import requests
import math
import json
from typing import Dict, List, Any

# API endpoints from AtCoder Problems
PROBLEMS_URL = "https://kenkoooo.com/atcoder/resources/problems.json"
PROBLEM_MODELS_URL = "https://kenkoooo.com/atcoder/resources/problem-models.json"
MERGED_PROBLEMS_URL = "https://kenkoooo.com/atcoder/resources/merged-problems.json"

def clip_difficulty(difficulty: float) -> int:
    """
    Clips the difficulty value using the same algorithm as in the frontend code.
    """
    if difficulty >= 400:
        return round(difficulty)
    else:
        return round(400 / math.exp(1.0 - difficulty / 400))

def get_rating_color(rating: int) -> str:
    """
    Returns the color name based on the rating value.
    """
    if rating < 400:
        return "grey"
    elif rating < 800:
        return "brown"
    elif rating < 1200:
        return "green"
    elif rating < 1600:
        return "cyan"
    elif rating < 2000:
        return "blue"
    elif rating < 2400:
        return "yellow"
    elif rating < 2800:
        return "orange"
    else:
        return "red"

def fetch_problems() -> List[Dict[str, Any]]:
    """
    Fetches problem data from the API.
    """
    response = requests.get(PROBLEMS_URL)
    return response.json()

def fetch_problem_models() -> Dict[str, Dict[str, Any]]:
    """
    Fetches problem models with difficulty ratings.
    """
    response = requests.get(PROBLEM_MODELS_URL)
    return response.json()

def fetch_merged_problems() -> List[Dict[str, Any]]:
    """
    Fetches merged problems data which includes point values.
    """
    response = requests.get(MERGED_PROBLEMS_URL)
    return response.json()

def main():
    # Fetch data from APIs
    print("Fetching problem data...")
    problems = fetch_problems()
    print(f"Found {len(problems)} problems")
    
    print("Fetching problem models with difficulty ratings...")
    problem_models = fetch_problem_models()
    print(f"Found {len(problem_models)} problem models")
    
    print("Fetching merged problems data with point values...")
    merged_problems = fetch_merged_problems()
    merged_problems_dict = {p['id']: p for p in merged_problems}
    print(f"Found {len(merged_problems)} merged problems")
    
    # Combine problem data with difficulty, color, and point
    enriched_problems = []
    for problem in problems:
        problem_id = problem['id']
        model = problem_models.get(problem_id, {})
        merged_data = merged_problems_dict.get(problem_id, {})
        
        difficulty = model.get('difficulty')
        point = merged_data.get('point')
        
        if difficulty is not None:
            # Clip the difficulty rating
            clipped_difficulty = clip_difficulty(difficulty)
            
            # Get the color based on difficulty
            color = get_rating_color(clipped_difficulty)
            
            enriched_problem = {
                **problem,
                'difficulty': difficulty,
                'clipped_difficulty': clipped_difficulty,
                'color': color,
                'point': point
            }
            enriched_problems.append(enriched_problem)
    
    print(f"Processed {len(enriched_problems)} problems with difficulty ratings")
    
    # Sort by difficulty
    enriched_problems.sort(key=lambda p: p.get('clipped_difficulty', 0))
    
    # Save to file
    with open('atcoder_problems_with_colors.json', 'w') as f:
        json.dump(enriched_problems, f, indent=2)
    
    # Print first 5 problems with their colors and points
    print("\nSample of problems with their colors and points:")
    for problem in enriched_problems[:5]:
        print(f"Problem: {problem['name']}, Difficulty: {problem.get('clipped_difficulty')}, Color: {problem.get('color')}, Point: {problem.get('point')}")

if __name__ == "__main__":
    main()