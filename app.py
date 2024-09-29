from flask import Flask, jsonify, request
import google.generativeai as genai
import time

app = Flask(__name__)

api_key_google = "AIzaSyDQSTmWlMkGUTTKhjsdU4SIKw02zKyG9Cg"
genai.configure(api_key=api_key_google)
model = genai.GenerativeModel("gemini-1.5-pro-latest")


@app.route('/<nome_do_anime>')
def index(nome_do_anime):
    prompt = f"Me faça um resumo de 200 palavras do personagem {nome_do_anime} do Harry Potter"
    response = model.generate_content(prompt)
    time.sleep(1)
    return response.text


if __name__ == '__main__':
    app.run(debug=True)
