from flask import Flask, jsonify, request
import random
import math

app = Flask(__name__)

@app.route('/health')
def health_check():
    return 'OK', 200


@app.route("/api/consultation/start", methods=["POST"])
def start_consultation():
    # Simulate consultation start
    consultation_id = random.randint(1000, 9999)
    doctor_id = random.choice([1, 2, 3, 4])  # Example doctor IDs
    patient_id = random.choice([100, 101, 102, 103])  # Example patient IDs
    return jsonify({
        "message": "Consultation started successfully",
        "consultation_id": consultation_id,
        "doctor_id": doctor_id,
        "patient_id": patient_id
    }), 200

@app.route("/api/patient/records", methods=["GET"])
def get_patient_records():
    # Simulate fetching patient records
    patient_id = request.args.get('patient_id', default=random.choice([100, 101, 102, 103]))
    records = {
        "patient_id": patient_id,
        "record_1": "Prescription: Paracetamol",
        "record_2": "Diagnosis: Fever",
        "record_3": "Next appointment: 2024-12-15"
    }
    return jsonify(records), 200

@app.route("/api/consultation/end", methods=["POST"])
def end_consultation():
    # Simulate ending consultation
    consultation_id = request.json.get('consultation_id')
    return jsonify({
        "message": f"Consultation {consultation_id} ended successfully"
    }), 200

if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=5000)
