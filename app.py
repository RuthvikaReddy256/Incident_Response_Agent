import os
from flask import Flask, jsonify, render_template, request
from dotenv import load_dotenv

from backend.agent import analyze_incident, process_resolution
from backend.memory_service import init_hindsight

load_dotenv()

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

init_hindsight()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/investigate", methods=["POST"])
def investigate():
    data = request.json or {}
    service = data.get("service")
    symptoms = data.get("symptoms")
    error_logs = data.get("error_logs", "")

    if not service or not symptoms:
        return jsonify({
            "status": "error",
            "message": "Missing required fields: 'service' and 'symptoms'."
        }), 400

    try:
        analysis_result = analyze_incident(
            service=service, 
            symptoms=symptoms, 
            error_logs=error_logs
        )
        return jsonify({"status": "success", "data": analysis_result}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/api/resolve", methods=["POST"])
def resolve():
    data = request.json or {}
    incident_id = data.get("incident_id")

    if not incident_id:
        return jsonify({
            "status": "error",
            "message": "Incident ID is required to store memory."
        }), 400

    try:
        retention_result = process_resolution(data)
        return jsonify({
            "status": "success",
            "message": "Incident successfully resolved and learned by Hindsight memory.",
            "data": retention_result
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)