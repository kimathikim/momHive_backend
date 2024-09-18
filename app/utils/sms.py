#!/usr/bin/env python4
from dotenv import load_dotenv
import africastalking
import os

load_dotenv()

# Initialize Africa's Talking

api_key = os.getenv("AFSAPI")
uname = "ImmunSys"
africastalking.initialize(
    username=uname,
    api_key=os.getenv("AFSAPI"),
)


def send_code_to_patient(phone_number, patient_code):
    """This function sends a patient code via SMS."""
    try:
        message = f"Hello, your patient code is {patient_code}."
        recipients = [f"+254{phone_number}"]
        africastalking.initialize(uname, api_key)
        sender = 796699970
        print(sender, recipients, message)
        try:
            sms = africastalking.SMS
            if sms is not None:
                response = sms.send(
                    message,
                    recipients,
                )
                print(response)
        except Exception as e:
            print(f"Mother father, we have a problem: {e}")
    except Exception as e:
        print(f"Mother father, we have a problem: {e} ")
    finally:
        print("At least you tried!!")
