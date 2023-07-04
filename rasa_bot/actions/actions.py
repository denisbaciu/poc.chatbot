import re
import requests
import json
import random
from typing import Dict, Text, Any, List, Union
import logging

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk import Action
from rasa_sdk.events import AllSlotsReset


class ValidateRestaurantForm(FormValidationAction):
    """Example of a form validation action."""

    def name(self) -> Text:
        return "validate_restaurant_form"

    @staticmethod
    def cuisine_db() -> List[Text]:
        """Database of supported cuisines."""

        return [
            "caribbean",
            "chinese",
            "french",
            "greek",
            "indian",
            "italian",
            "mexican",
        ]

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer."""

        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_cuisine(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate cuisine value."""

        if value.lower() in self.cuisine_db():
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"cuisine": value}
        else:
            dispatcher.utter_message(response="utter_wrong_cuisine")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"cuisine": None}

    def validate_num_people(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""

        if self.is_int(value) and int(value) > 0:
            return {"num_people": value}
        else:
            dispatcher.utter_message(response="utter_wrong_num_people")
            # validation failed, set slot to None
            return {"num_people": None}

    def validate_outdoor_seating(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate outdoor_seating value."""

        if isinstance(value, str):
            if "out" in value:
                # convert "out..." to True
                return {"outdoor_seating": True}
            elif "in" in value:
                # convert "in..." to False
                return {"outdoor_seating": False}
            else:
                dispatcher.utter_message(response="utter_wrong_outdoor_seating")
                # validation failed, set slot to None
                return {"outdoor_seating": None}

        else:
            # affirm/deny was picked up as True/False by the from_intent mapping
            return {"outdoor_seating": value}
        

class ValidateInsuranceForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_insurance_form"

    @staticmethod
    def car_reg_db() -> List[Text]:
        """Database of supported car reg."""

        return [
            "KJH789",
            "KP10XRJ",
            "456XYZ",
            "DF123G",
            "LMN123",
            "XYZ123",
            "ABC789",
            "DF123G",
        ]
    
    @staticmethod
    def job_title_db() -> List[Text]:
        """Database of supported car reg."""

        return [
            "developer",
            "doctor",
            "firefighter",
            "police officer",
            "worker"
        ]
    
    @staticmethod
    def postcode_db() -> List[Text]:
        """Database of supported car reg."""

        return [
                "HP",
                "G1",
                "CR",
                "OX",
                "HP",
                "AB",
                "NP",
                "GU",
                "E1",
                "PE",
                "IP",
                "JE",
                "B3",
                "BA",
                "ME",
                "KA",
                "OL",
                "KA",
                "IP",
                "AB",
                "IG",
                "NW",
                "N1",
                "RM",
                "NP",
                "ME",
                "BD",
                "PR",
                "BA",
                "BD",
                "ME",
                "RM",
                "RM",
                "E1",
                "L1",
            ]
    
    @staticmethod
    def car_use_db() -> List[Text]:
        """Database of supported car reg."""

        return [
            "business",
            "personal",
            "personal and business",
            "personal & business",
            "commercial",
            "private",
        ]

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer."""

        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_car_reg(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate car_reg value."""

        if value in self.car_reg_db():
            # validation succeeded, set the value of the "car_reg" slot to value
            return {"car_reg": value}
        else:
            dispatcher.utter_message(response="utter_wrong_car_reg")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"car_reg": None}
    
    def validate_job_title(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate job_title value."""

        if value in self.job_title_db():
            # validation succeeded, set the value of the "job_title" slot to value
            return {"job_title": value}
        else:
            dispatcher.utter_message(response="utter_wrong_job_title")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"job_title": None}
    
    def validate_postcode(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate postcode value."""

        if value in self.postcode_db():
            return {"postcode": value}
        else:
            dispatcher.utter_message(response="utter_wrong_postcode")
            return {"postcode": None}
        
    def validate_car_use(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate car_use value."""

        if value in self.car_use_db():
            # validation succeeded, set the value of the "car_use" slot to value
            return {"car_use": value}
        else:
            dispatcher.utter_message(response="utter_wrong_car_use")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"car_use": None}

    def validate_total_miles(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate total_miles value."""

        if self.is_int(value) and int(value) > 0:
            return {"total_miles": value}
        else:
            dispatcher.utter_message(response="utter_wrong_total_miles")
            # validation failed, set slot to None
            return {"total_miles": None}

    def validate_previous_claims(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate previous_claims value."""

        if isinstance(value, str):
            if "yes" in value:
                # convert "out..." to True
                return {"previous_claims": "yes"}
            elif "no" in value:
                # convert "in..." to False
                return {"previous_claims": "no"}
            else:
                dispatcher.utter_message(response="utter_wrong_previous_claims")
                # validation failed, set slot to None
                return {"previous_claims": None}

        else:
            # affirm/deny was picked up as True/False by the from_intent mapping
            return {"previous_claims": value}
    

class ActionGetQuotes(Action):
    def name(self) -> Text:
        return "action_get_quotes"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["job_title", "car_use", "total_miles", "previous_claims", "postcode"]

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> List[Dict]:
        
        try:
            url_car_insurance_price_predict = "http://localhost:8001/predict"

            data_car = {
                "job_title": f"{tracker.get_slot('job_title')}",
                "car_use": f"{tracker.get_slot('car_use')}",
                "total_miles": tracker.get_slot('total_miles'),
                "previous_claims": f"{tracker.get_slot('previous_claims')}",
                "postcode": f"{tracker.get_slot('postcode')}",
                "credit_score": random.randint(100, 999)
            }

            logging.info(f"Date sent to car insurance prediction: {data_car}")

            headers = {'Content-Type': 'application/json'}

            response_car = requests.post(url_car_insurance_price_predict, data=json.dumps(data_car), headers=headers)
            if response_car.status_code == 200:
                data = response_car.json()
                response_text = f"Hey {tracker.get_slot('first_name')}, I just did a quick search for you and the cheapest quote would be £{data['cheapest_quote']} per annum"
                dispatcher.utter_message(text=f"{response_text}")
            else:
                dispatcher.utter_message(text=f"Error fetching the Car API, status code {str(response_car.status_code)}")
        except:
                dispatcher.utter_message(text="Try/Catch Error")
        
        try:
            url_home_insurance_recommendation = "http://localhost:5001/predict"

            #supposedly we will fetch this data from our database - for now I randomly generate it
            data_home = {
                "profession": f"{tracker.get_slot('job_title')}",
                "married": random.randint(0, 1),
                "cars_owned": random.randint(0, 5),
                "kids_number": random.randint(0, 6),
                "credit_card_owned": random.randint(0, 1),
                "annual_salary": random.randint(12000, 160000),
                "months_ago_quoted": random.randint(0, 12),
                "has_a_house": random.randint(0, 1),
            }

            # "married": 0,
            # "cars_owned": 1,
            # "kids_number": 1,
            # "credit_card_owned": 1,
            # "annual_salary": 160000,
            # "months_ago_quoted": 12,
            # "has_a_house": 1

            logging.info(f"Date sent to house insurance recommendation: {data_home}")

            headers = {'Content-Type': 'application/json'}

            response_home = requests.post(url_home_insurance_recommendation, data=json.dumps(data_home), headers=headers)
            if response_home.status_code == 200:
                data = response_home.json()
                if(data['prediction'] > 0.6):
                    response_text = f"Also we offer the cheapest home insurance quotes, do you want to have a look?"
                    dispatcher.utter_message(text=f"{response_text}", image="https://images.vexels.com/media/users/3/210321/isolated/lists/c14fc2ab99fee935a402582c27c70e24-home-sweet-home-badge.png")
                else:
                    response_text = f"Can I suggest some mortgages?"
                    dispatcher.utter_message(text=f"{response_text}", image="https://cdn-icons-png.flaticon.com/256/781/781730.png")

            else:
                dispatcher.utter_message(text=f"Error fetching the Home API, status code {str(response_car.status_code)}")
        except:
                dispatcher.utter_message(text="Try/Catch Error")
        
        return []#AllSlotsReset()


def encode_to_utf(string):
    charList = []
    for i in [ord(x) for x in string]:
        if i < 128:
            charList.append(chr(i))
        else:
            charList.append('\\u%04x' % i)
    
    res = ''.join(charList)
    return res
