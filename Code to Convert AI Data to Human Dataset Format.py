import json
import re

def parse_human_data(file_path):
    """Parse the human dataset from the text file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split the content by JSON lines
    json_lines = [line for line in content.split('\n') if line.strip() and line.strip().startswith('{')]
    
    # Parse each JSON line
    posts = []
    for line in json_lines:
        try:
            post = json.loads(line)
            posts.append(post)
        except json.JSONDecodeError:
            print(f"Error parsing line: {line[:50]}...")
    
    return posts

def parse_ai_data(file_path):
    """Parse the AI-generated data from the text file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all instruction-input-output triplets
    pattern = r'{"instruction": "Generate a funny music-related joke", "input": "Generate a music-related joke with the following title: (.*?)\\n\\nJoke:", "output": "(.*?)"}'
    matches = re.findall(pattern, content, re.DOTALL)
    
    return matches

def convert_ai_to_human_format(ai_data, human_data_sample):
    """Convert AI data to match the format of human data."""
    formatted_data = []
    
    for title, joke_text in ai_data:
        # Create a new post based on the structure of human data
        new_post = {
            "type": "post",
            "id": f"ai_{len(formatted_data)}",  # Generate a unique ID
            "subreddit.id": "2qh72",  # Same as human data
            "subreddit.name": "jokes",
            "subreddit.nsfw": False,
            "created_utc": 0,  # Placeholder timestamp
            "permalink": f"https://example.com/r/Jokes/ai_{len(formatted_data)}/",
            "domain": "self.jokes",
            "url": None,
            "selftext": joke_text,
            "title": title,
            "score": 0  # Default score
        }
        
        formatted_data.append(new_post)
    
    return formatted_data

def save_formatted_data(data, output_file):
    """Save the formatted data as JSON lines."""
    with open(output_file, 'w', encoding='utf-8') as f:
        for post in data:
            f.write(json.dumps(post) + '\n')

def main():
    # File paths
    human_data_file = "reddit_music_jokes.jsonl"  
    ai_data_file = "llama_training_data.jsonl"        
    output_file = "formatted_ai_data.jsnol"
    
    # Parse the data
    human_data = parse_human_data(human_data_file)
    ai_matches = parse_ai_data(ai_data_file)
    
    # Convert AI data to human format
    formatted_ai_data = convert_ai_to_human_format(ai_matches, human_data[:1])
    
    # Save the formatted data
    save_formatted_data(formatted_ai_data, output_file)
    
    print(f"Processed {len(ai_matches)} AI jokes and saved to {output_file}")

if __name__ == "__main__":
    main()