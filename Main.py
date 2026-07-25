import os
from google import genai
from flask import Flask, jsonify

app = Flask(__name__)

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)

tools = [
    {
        'type': 'google_search',
    },
]

generation_config = {
    'temperature': 2,
    'max_output_tokens': 65536,
    'top_p': 0.95,
    'thinking_level': 'high',
}

@app.route('/')
def home():
    try:
        interaction = client.interactions.create(
            model='models/gemini-3-flash-preview',
            input='Hola',
            tools=tools,
            generation_config=generation_config,
        )
        return jsonify({"respuesta": str(interaction.steps[-1])})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
