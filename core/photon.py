import speech_recognition as sr
import pyttsx3
import asyncio
import cohere
import os

CO_API_KEY = "" # Your Cohere API key goes here (Get it from https://cohere.com/)
co = cohere.ClientV2(CO_API_KEY)


class Photon:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        
    async def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    async def listen(self):
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio)
                print(text)
                return text
            except sr.UnknownValueError:
                return ""
            except sr.RequestError as e:
                await self.speak("System ran into a network error!")
                return ""

        
    async def get_response(self, prompt):
        response = co.chat(
            model="command-r-plus-08-2024",
            messages=[{"role": "user", "content": f"You are Photon, a personal personal AI assisstant created by Flame. Your work is to perform several tasks given by the user in the minimal but most informative way within 300 words. You have to help user with {prompt}"}]
        )
        return response.message.content[0].text



    async def connect(self):
        await self.speak("Connecting to the System...")
        await self.speak("Welcome to the System. Photon is online!")
        await asyncio.sleep(1)
        while True:
            query = await self.listen()
            if query.lower().startswith("hey photon"):
                response = await self.get_response(query.strip("hey photon"))
                print(response)
                await self.speak(response)