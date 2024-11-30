from locust import HttpUser, task, between
import random
import logging

class TelemedicineUser(HttpUser):
    wait_time = between(5, 15)

    def on_start(self):
        logging.info("Starting test simulation")

    @task(1)
    def start_consultation(self):
        logging.info("Starting consultation")
        response = self.client.post("/api/consultation/start")
        logging.debug(f"Start consultation response: {response.text}")
        if response.status_code == 200:
            logging.info(f"Started consultation: {response.json()}")
        else:
            logging.error(f"Failed to start consultation: {response.status_code} - {response.text}")

    @task(2)
    def get_patient_records(self):
        patient_id = random.choice([100, 101, 102, 103])
        logging.info(f"Fetching records for patient ID: {patient_id}")
        response = self.client.get(f"/api/patient/records?patient_id={patient_id}")
        logging.debug(f"Patient records response: {response.text}")
        if response.status_code == 200:
            logging.info(f"Fetched patient records for patient ID {patient_id}")
        else:
            logging.error(f"Failed to fetch records: {response.status_code} - {response.text}")

    @task(3)
    def end_consultation(self):
        consultation_id = random.randint(1000, 9999)
        logging.info(f"Ending consultation with ID: {consultation_id}")
        response = self.client.post("/api/consultation/end", json={"consultation_id": consultation_id})
        logging.debug(f"End consultation response: {response.text}")
        if response.status_code == 200:
            logging.info(f"Ended consultation ID {consultation_id}")
        else:
            logging.error(f"Failed to end consultation: {response.status_code} - {response.text}")
