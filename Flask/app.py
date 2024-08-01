# app.py
from flask import Flask, request, jsonify
from inference import predict 
from upscaling import generate_system_prompt

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_route():
    data = request.json
    user_input = data.get('input', '')
    if not user_input:
        return jsonify({"error": "No input provided"}), 400
    try:
        system_prompt = generate_system_prompt(user_input)
        print(system_prompt)
        output = predict(system_prompt)
        return jsonify({"generated_text": output})
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6000)

