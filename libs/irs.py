import google.generativeai as genai
from dotenv import load_dotenv
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
import time
import json

testing = False
load_dotenv()


class ItineraryResolver:
    def __init__(self):
        self._configure_model()
        self._data = {}

    def update_data(self, newdata):
        if self._data == {} or self._data["s1"] != newdata["s1"]:
            self._data = newdata
            for ques in self._data["s2"].keys():
                self._data["s2"][ques] = [
                    self._data["s2"][ques],
                ]

        elif self._data["s2"] != newdata["s2"]:
            for ques in newdata["s2"].keys():
                if newdata["s2"][ques] not in self._data["s2"][ques]:
                    self._data["s2"][ques].append(newdata["s2"][ques])

        else:
            pass

        print("New data:", json.dumps(self._data, indent=1), sep="\n")

    def _configure_model(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self._model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_prompt(self):

        def bulletize(response_list) -> str:
            if not response_list[-1]:
                res = "- User has not given a preference for this question."
            else:
                res = [f"- {a}" for a in response_list if a]
                res = "\n".join(res)
            return res

        s1txt = [f"q: {q} -> a: {self._data['s1'][q]}" for q in self._data["s1"].keys()]
        s1txt = "\n".join(s1txt)

        s2txt = [
            f"q: {q}:\n{bulletize(self._data['s2'][q])}"
            for q in self._data["s2"].keys()
        ]
        s2txt = "\n\n".join(s2txt)

        prompt = f"""
Your task is to create an itinerary based on the following question-answer patters:

Unchanging preferences:
{s1txt}

Changing preferences
{s2txt}

For changing preferences, consider the bullets as the user's order of input. The lower it is, the more recent it is.
Include the distance and travel time from the starting point to the first attraction if a starting point is provided.
Check Attraction Status: Fetch details about each attraction, such as whether it is open, closed, or under renovation, and adjust the itinerary accordingly.
Optimize Path Based on Budget: Generate an optimized path based on the user's budget. If the budget allows for taxis, identify which segments can use taxis and adjust the itinerary accordingly to minimize travel time and maximize convenience. Make sure that the prices are accurate and realistic.
""".strip()

        return prompt

    def ProcessPreference(self):
        prompt = self.generate_prompt()
        print(prompt)
        if testing:
            return "Yolo lol"
        response = self._model.generate_content(prompt)
        print(response)
        return response.text


iris = ItineraryResolver()
