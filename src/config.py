MAIL = "smrnjeet222@gmail.com"
PASS = ".................."

DATA_PATH = "input/test_data.csv"
CER_PATH = "input/cat.jpg"

SUBJECT = "Certificate of participation in event organised by Illuminate society."


def body(name):
    name = name.replace("_", " ").upper()
    return f"Greetings,\n{name} please find your event participation certificate attached with this mail.\n\nRegards,\nIlluminate Society\n\n"
