def convert_to_jsonl(incident):
    inc = {}
    input_text = "Classify the following incident into a service offering." + "\n\n" + "Short Description:" + "\n" + incident["Short description"].replace('\n', '') + "\n\n" + "Long Description" + "\n" + incident["Description"].replace('\n', '') + "\n\n" + "Service Offering:"
    output_text = incident["Service offering"]

    inc["contents"] = []
    inc["contents"].append({"role": "user", "parts" : [{"text": input_text}]})
    inc["contents"].append({"role": "model", "parts" : [{"text": output_text}]})

    return inc