from openai import OpenAI

client = OpenAI()

def get_sentiment(text: list) -> list:
    """
   Takes in a list of review strings and returns a list of sentiment labels 
   ("postive", "neutral", "negative", or "irrelevant")

   Returns error message if wrong input 
    """

    if not isinstance(text, list):
        return "Wrong input. text must be an array of strings."

    if not text or any(not isinstance(t, str) for t in text):
        return "Wrong input. text must be an array of strings."

    reviews = "\n".join([f"Review: \"{review}\"" for review in text])
    
    system_prompt = """
    You are an expert in interpreting human sentiment across cultures. 
Label the following product reviews based on sentiment. 

Use ONLY these four labels:
- positive
- neutral
- negative
- irrelevant

Respond with only a single label per review. Do not include any explanation or additional words. Each label must be on its own line and must match the number of input reviews.

Examples:
Review: "I love this ring, I use it all the time when working out."
Label: positive

Review: "It's an ok ring. Some features could be better but for the price it's fine."
Label: neutral

Review: "Absolutely terrible ring. The green light that the ring emitted kept attracting mosquitos."
Label: negative

Review: "I like strawberry ice cream because it's the best."
Label: irrelevant
    
    """

    prompt = f"""
    For each line of text in the string below, please categorize the review
    as either positive, neutral, negative, or irrelevant.

    Use only a one-word response per line. Do not include any numbers.
    {reviews}
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature = 0,
        max_tokens = 50,
    )

    output = response.choices[0].message.content.strip()
    labels = [line.strip() for line in output.split("\n") if line.strip()]
    return labels

