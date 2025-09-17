import os
import json

from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel


class CreditCardReward(BaseModel):
    bank_name: str
    card_name: str
    benefit_plan: str
    store_name: str
    store_type_name: str
    reward_amount: float


class GeminiAnalyzer:
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY environment variable must be set")
            
    def analyze_transaction(self, input_text: str):        
        prompt = f"""
        Analyze the following text and extract credit card reward information. 
        
        Rules:
        - If information is not available, use null for that field
        - store_name should be exactly the same as in the text
        
        Text to analyze: {input_text}
        """
        print("Start Analyzing")
        client = genai.Client()
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": list[CreditCardReward],
            },
        )
        print(response.text)
        return json.loads(response.text)

def analyze_credit_card_text(input_text: str, api_key: str = None):
    analyzer = GeminiAnalyzer(api_key)
    return analyzer.analyze_transaction(input_text)


if __name__ == "__main__":
    load_dotenv()
    API_KEY = os.getenv('GEMINI_API_KEY')
    with open("tmp\\tmp", "r", encoding="utf-8") as f:
        text = f.read()

    try:
        reward_dict = analyze_credit_card_text(text, api_key=API_KEY)
        with open("result\\cube.json", "w+", encoding="utf-8") as f:
            json.dump(reward_dict, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error: {e}")