import json


class TranscriptLine:
    def __init__(self, lineID, speaker, timestamp, text):
        self.lineID = lineID
        self.speaker = speaker
        self.timestamp = timestamp
        self.text = text

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
