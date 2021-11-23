# Trint-Transcript-To-JSON
A basic Python script to convert Trint formatted transcripts into JSON.

# Useage
The trint transcript must first be saved as a plain text file (.txt) extension. This can be done either by re-saving the file using a word processor (Microsoft Word, Google Docs, Open Office Writer etc).

Open the "TransciptToJSON.py" script, and alter the "FILEPATH" and "FILENAME" variables to point to the plain text version of the transcript (you don't need to include the file format within the filename). The script can then either be ran from an IDE or directly from the command line with "python TranscriptToJSON.py".

# Format
The JSON format is based on the class format in the transcript line file:
```
  [
    { lineID: 1,
      speaker: "Speaker Reference",
      timestamp: "00:00:00",
      text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis in justo ut dolor aliquam convallis."
    },
    { lineID: 2,
      speaker: "Speaker Reference",
      timestamp: "00:02:16",
      text: "Ut hendrerit mi et vulputate finibus. Duis viverra est vitae turpis feugiat tincidunt."
    },
    ...
  ]
```
# Improvements
If this script is found to be useful it would be convenient to add some CLI argument parseing for choosing the input/output file path/name.
