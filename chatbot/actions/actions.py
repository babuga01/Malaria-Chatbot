# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher


# class ActionMalariaOverview(Action):
#     def name(self) -> Text:
#         return "action_malaria_overview"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(text="Malaria is a life-threatening disease caused by Plasmodium parasites transmitted through the bite of infected female Anopheles mosquitoes.")
#         return []

# class ActionSymptoms(Action):
#     def name(self) -> Text:
#         return "action_symptoms"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(text="Common symptoms of malaria include fever, chills, vomiting, headache, muscle aches, and fatigue. It’s best to consult a healthcare provider.")
#         return []

# class ActionPrevention(Action):
#     def name(self) -> Text:
#         return "action_prevention"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(text="To prevent malaria, sleep under treated bed nets, use mosquito repellent, wear long sleeves, and eliminate standing water nearby.")
#         return []

# class ActionTreatment(Action):
#     def name(self) -> Text:
#         return "action_treatment"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(text="Malaria is treated with antimalarial medications such as ACTs (Artemisinin-based Combination Therapies). Early diagnosis and treatment are essential.")
#         return []

# class ActionTransmission(Action):
#     def name(self) -> Text:
#         return "action_transmission"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(text="Malaria is transmitted to humans through the bites of infected female Anopheles mosquitoes. It is not spread from person to person directly.")
#         return []

# class ActionCauses(Action):
#     def name(self) -> Text:
#         return "action_causes"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(text="Malaria is caused by Plasmodium parasites. These parasites are transmitted to people through the bites of infected mosquitoes.")
#         return []

# class ActionUnknown(Action):
#     def name(self) -> Text:
#         return "action_unknown"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(text="Sorry, Retry asking me about malaria symptoms, treatment, or prevention.")
#         return []
