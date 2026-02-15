import os
from prompt import *
from google import genai
from google.genai import types
from datetime import datetime

def actualizar_lista_mensajes(path_archivo):
    with open("mensajes.txt", "a", encoding="utf-8") as file:
        file.write(f"{path_archivo}\n")
        
def actualizar_index(path_archivo):
    # to bottom of index.md, add a link to the latest response file
    with open("index.md", "a", encoding="utf-8") as file:
        file.write(f"\n- [{os.path.basename(path_archivo)}]({path_archivo})")

def save_response_to_file(response, filename="response.txt"):
    if response:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(response.text)
        print(f"Response saved to {filename}")
    else:
        print("No response received from the API. Nothing to save.")

def read_response_from_file(filename="response.txt"):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    else:
        print(f"No file named {filename} found.")
    return None

def send_prompt_to_api(prompt_text):
    if not prompt_text:
        raise ValueError("Prompt text is empty. Please provide a valid prompt.")
    api_key = os.environ.get("GOOGLE_AI_KEY")
    if not api_key:
        raise ValueError("GOOGLE_AI_KEY environment variable not set.")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt_text,
        config=types.GenerateContentConfig(
            tools=[types.Tool(google_search=types.GoogleSearch())]
        )
    )
    return response
    # print(response.text)

def main(read_from_file=False):
    if read_from_file:
        text = read_response_from_file()
        if text:
            print(text)
        else:
            print("No response to display.")
    else:
        
        todays_date = datetime.now().strftime("%Y-%m-%d")
        tema = elegir_tema(datetime.now().weekday())
        prompt_text = generar_prompt(todays_date, tema)
        print(f"Generated Prompt: {prompt_text}")
        response = send_prompt_to_api(prompt_text)
        path_archivo = f"mensajes/response_{todays_date}.txt"
        save_response_to_file(response, path_archivo)
        actualizar_index(path_archivo)
        actualizar_lista_mensajes(path_archivo)

if __name__ == "__main__":
    read_from_file = False
    main(read_from_file)