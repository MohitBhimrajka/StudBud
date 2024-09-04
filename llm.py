from langchain_community.llms import Ollama

ollama = Ollama(model="studbud", base_url="http://localhost:11434", verbose=True)

def get_generated_text(query, solution_context):
    prompt = f"""
You are an assistant for the placement cell of ATLAS SkillTech University. Always maintain a professional demeanor in your conversations. Your role is to assist students and employers with placement-related queries and processes.

Solution Context:
{solution_context}

User Query: {query}

Your response:
"""
    try:
        response = ollama.invoke(prompt)
        return response if isinstance(response, str) else response.get('text', '')
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage
if __name__ == "__main__":
    query = "What are the steps to apply for placements?"
    context = "The placement season starts in September."
    result = get_generated_text(query, context)
    print(result)