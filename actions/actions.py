# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
import random
# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

import yaml
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionCheckQuestions(Action):

    def name(self) -> Text:
        return "action_check_exist_questions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message['text']

        with open('../data/nlu.yml', 'r') as questions:
            questions = yaml.safe_load(questions)
        possible_answers = ['Iltimos savolingizni boshqacharoq shaklda bersangiz!',
                            "Men bu savolingiz haqida o'ylab olgunimcha boshqa savol berishingizni so'rayman :)",
                            "Savolingizni boshqacharoq shaklda bersangiz, iltimos!",
                            "Men tushunmaydigan savollar bermasangiz yaxshi bo'ladi :)", ]
        for intent_num in range(len(questions["nlu"])):
            intent_examples = questions["nlu"][intent_num]["examples"]
            if user_message in intent_examples:
                continue
            elif user_message not in intent_examples and tracker.latest_message['intent']['confidence'] < 0.65:
                    dispatcher.utter_message(text=possible_answers[random.randint(0, len(possible_answers) - 1)])
        return []
