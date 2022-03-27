from mycroft import MycroftSkill, intent_file_handler


class SearchingPetrolPump(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('pump.petrol.searching.intent')
    def handle_pump_petrol_searching(self, message):
        self.speak_dialog('pump.petrol.searching')


def create_skill():
    return SearchingPetrolPump()

