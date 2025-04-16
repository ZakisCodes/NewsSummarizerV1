import os
from src.models import Summary
import instructor
from groq import Groq
from dotenv import load_dotenv
from src.schemas import Prompt

load_dotenv()


class GroqService:
    def analyze_news(self, Input: Prompt, personality: str = "friendly") -> Summary:
        api_key = os.getenv("GROQ_API")
        if not api_key:
            raise ValueError("GROQ_API environment variable is not set.")

        client = Groq(api_key=api_key)
        client = instructor.from_groq(client)
        try:
            completion = client.chat.completions.create(
                model="meta-llama/llama-4-maverick-17b-128e-instruct",
                messages=[
                    {
                        "role": "assistant",
                        "content": f"""Extract structred information from the following News content and format is as specified
                        
                                    1. Headline
                                        - Create a concise, informative headline that captures the main point of the news
                                        - Use active voice and present tense when possible
                                        - maximum 15 words
                                    2. Topic
                                        - The category this news content belongs to: Select one from ["Politics", "Business", "Science", "Technology", "Health", "Environment", "Entertainment", "Sports", "World Affairs", "Education"]
                                        - if applicable: Select up to two additional relevant categories
                                    3. Summary
                                        Write the summary in two clearly separated paragraphs.
                                        - First paragraph (40-60 words): Provide the core news - who, what, when, where, why, summarizing the main event or announcement.
                                        - Second paragraph (40-60 words): Add context, significance, or key implications, highlighting why the news matters, its potential impact, or what it signifies in a broader context.
                                         Example Use Case:
                                          User input: 
                                            GreenGrid Launches Solar Microgrid Project to Power Remote Villages in Nepal
                                            Kathmandu, Nepal – April 15, 2025
                                            GreenGrid Energy, a renewable energy startup based in Singapore, has officially launched a $15 million solar microgrid project aimed at electrifying 25 remote villages in Nepal’s Himalayan region...
                                            
                                            Sample Summary (Output)
                                            GreenGrid Energy, a Singapore-based startup, has launched a $15 million solar microgrid project to electrify 25 remote villages in Nepal. The initiative, announced in Kathmandu, will use solar panels and battery storage to power homes, schools, and clinics, aiming for full installation by mid-2026.
                                            The project supports Nepal’s 2030 goal for universal electricity access and has been praised for reducing reliance on diesel while empowering local communities. It may also serve as a blueprint for clean energy rollouts in other hard-to-reach regions globally.

                                             In the example output:
                                             1. The first paragraph concisely summarizes the main news: GreenGrid Energy is launching a $15 million project in Nepal to electrify 25 remote villages using solar microgrids, with an expected completion by mid-2026.
                                             2. The second paragraph adds context and significance: The project aligns with Nepal's goal for universal electricity access by 2030, has the potential to reduce diesel reliance, and could be a model for other regions.
                                    4. Readability
                                        - Score on scale of 1.0 to 5.0 (with onw decimal place)
                                        - Format as [score] / 5.0 (eg: 4.5 / 5.0)
                                    5. Star
                                        - Visual representation: Convert Readability Score to stars (★ for each full point, ☆ for half point
                                        - Example: 3.5 = ★★★☆☆
                                     
                                     Your personality is {personality}""",
                    },
                    {"role": "user", "content": Input.news},
                ],
                response_model=Summary,
            )
            return completion
        except Exception as e:
            raise RuntimeError(f"Runtime error during ai call: {e}")
