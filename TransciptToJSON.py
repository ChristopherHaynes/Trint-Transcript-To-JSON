import json
from TranscriptLine import *

SCORE_WORDS = False
SAVE_TO_JSON = True
FILEPATH = "F:\\PhD\\Age In\\Oksana_Cleaned_Transcripts\\"
FILENAME = "FG1_cleaned_up_no_q"


def saveToJSON(filepath, data):
    jsonFile = open(filepath + ".json", "w")

    jsonData = list()
    for item in data:
        jsonData.append(item.toJson())

    jsonString = json.dumps(jsonData)
    jsonFile.write(jsonString)
    jsonFile.close()


transcriptFile = open(FILEPATH + FILENAME + ".txt")
transcript = list()
lineID = 1

for line in transcriptFile:
    timestampStartIndex = line.find("[")
    timestampEndIndex = line.find("]")
    if timestampStartIndex != -1 and timestampEndIndex != -1:
        speaker = line[0: timestampStartIndex].strip()
        timestamp = line[timestampStartIndex + 1: timestampEndIndex].strip()
        text = line[timestampEndIndex + 1:].strip()

        transLine = TranscriptLine(lineID, speaker, timestamp, text)
        transcript.append(transLine)

        lineID += 1

transcriptFile.close()

if SAVE_TO_JSON:
    saveToJSON(FILEPATH + FILENAME, transcript)


