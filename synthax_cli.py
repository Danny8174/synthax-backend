def run_synthax_code(code):
    import time
    lines = code.strip().splitlines()
    output = []

    for line in lines:
        line = line.strip()
        if line.startswith("log "):
            output.append(line[4:].strip().strip('"'))
        elif line.startswith("wait "):
            try:
                seconds = int(line.split()[1])
                time.sleep(seconds)
            except:
                output.append("Invalid wait syntax")
        else:
            output.append("Unrecognized command: " + line)

    return "\n".join(output)