def convert_to_jsonl(incident):
    inc = {}
    inc["input_text"] = "Classify the following incident into a service offering." + "\n\n" + "Short Description:" + "\n" + incident["Short description"].replace('\n', '') + "\n\n" + "Long Description" + "\n" + incident["Description"].replace('\n', '') + "\n\n" + "Service Offering:"
    inc["output_text"] = incident["Service offering"]

    return inc