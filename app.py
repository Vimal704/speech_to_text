from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

openai.api_key = "YOUR_API_KEY"  # Replace with your OpenAI API key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'})

    audio_file = request.files['audio']

    if audio_file.filename == '':
        return jsonify({'error': 'No selected file'})

    audio_data = audio_file.read()

    try:
        response = openai.Transcription.create(
            audio=audio_data,
            model="whisper",
            language="en-US"
        )

        text = response['text']
        return jsonify({'text': text})
    except Exception as e:
        return jsonify({'error': f"Error: {e}"})

if __name__ == '__main__':
    app.run(debug=True)
