from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from agent import run_skillbridge_agent

load_dotenv()
app = Flask(__name__)
CORS(app)  # Allows the frontend HTML file to call this API


@app.route('/health', methods=['GET'])
def health():
    """Quick check that the server is running"""
    return jsonify({
        "status": "SkillBridge running",
        "version": "1.0.0",
        "model": os.getenv("AZURE_OPENAI_DEPLOYMENT", "not set")
    })


@app.route('/analyze', methods=['POST'])
def analyze():
    """Main endpoint — receives profile, returns career analysis"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON body sent"}), 400

        # Validate required fields
        required = ['name', 'skills', 'education', 'location', 'target_role']
        for field in required:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        # Handle skills as either a string or list
        if isinstance(data['skills'], str):
            data['skills'] = [s.strip() for s in data['skills'].split(',') if s.strip()]

        if len(data['skills']) == 0:
            return jsonify({"error": "Please provide at least one skill"}), 400

        # Run the agent
        result = run_skillbridge_agent(data)
        return jsonify({"success": True, "result": result})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == '__main__':
    print("Starting SkillBridge API server...")
    print("Health check: http://localhost:5000/health")
    app.run(debug=True, host='0.0.0.0', port=5000)