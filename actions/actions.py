from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
import pandas as pd 
import numpy as np

df = pd.read_csv('C:/Users/asus/OneDrive/Desktop/Rasa/actions/a.csv')

class ActionClgNames(Action):
    def name(self) -> Text:
        return "action_clg_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        clg = ""
        for i,j in df.iterrows():
            clg += str(i) + "." + j['clg_names'] + "\n\n"
        dispatcher.utter_message(clg)
        return []

class ActionClgAdd(Action):
    def name(self) -> Text:
        return "action_get_address"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        """name = next(tracker.get_latest_entity_values("clg_name"), None)
        def get_details(name,df,parameter = ['location']):
            df = df[df['clg_names'] == name]
            data_dict = dict()
            if parameter != []:
                for each_param in parameter:
                    data_dict[each_param] = list(df[each_param])[0]
                    return data_dict
            else:
                for each_param in list(df):
                    data_dict[each_param] =  list(df[each_param])[0]
                    return data_dict
        dispatcher.utter_message(data_dict)
        return []"""

        a = df.iat[0, 1]
        dispatcher.utter_message(a)
        return []

class ActionClgContact(Action):
    def name(self) -> Text:
        return "action_get_contact"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        a = df.iat[0, 2]
        dispatcher.utter_message(a)
        return []

class ActionClgIntake(Action):
    def name(self) -> Text:
        return "action_get_intake"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        a = df.iat[0, 3]
        dispatcher.utter_message(a)
        return []

class ActionClgEmail(Action):
    def name(self) -> Text:
        return "action_get_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        a = df.iat[0, 4]
        dispatcher.utter_message(a)
        return []