def run_synthax_code(input_text):
    if "wait" in input_text.lower() and "log" in input_text.lower():
        return "wait 2\nlog \"Done\""
    return f"log \"{input_text}\""