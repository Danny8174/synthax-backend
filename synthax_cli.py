import sys
import os
from synthax_interpreter import tasks, context, log, macros

def parse_line(line, lineno, base_dir=None):
    try:
        line = line.strip()
        if line.startswith("import "):
            imported_file = line.replace("import", "").strip().strip('"')
            file_path = os.path.join(base_dir or ".", imported_file)
            run_file(file_path)
        elif line.startswith("log "):
            content = line[4:].strip('"').strip()
            log(content)
        elif line.startswith("choose model"):
            context["use_fast"] = True
            if context.get("use_fast"):
                import synthax_interpreter
                synthax_interpreter.model = "gpt-3.5-turbo"
            else:
                import synthax_interpreter
                synthax_interpreter.model = "gpt-4"
        elif line.startswith("define "):
            parts = line.split("define", 1)[1].strip()
            name, args = parts.split("(", 1)
            arg = args.strip("):")
            def macro_func(x):
                return f"Running macro {name.strip()} with {x}"
            macros[name.strip()] = macro_func
        elif "=" in line and not line.startswith("define"):
            key, value = line.split("=", 1)
            context[key.strip()] = eval(value.strip())
        elif line.startswith("result ="):
            task_call = line.split("=", 1)[1].strip()
            if "(" in task_call:
                name, arg = task_call.split("(", 1)
                arg = arg.rstrip(")").strip()
                if name.strip() in macros:
                    context["result"] = macros[name.strip()](context[arg])
                elif name.strip() in tasks:
                    context["result"] = tasks[name.strip()](context[arg])
                else:
                    raise NameError(f"Undefined function: {name.strip()}")
        elif line.startswith("loop "):
            parts = line.replace("loop ", "").replace(":", "").split(" in ")
            var_name = parts[0].strip()
            iterable_name = parts[1].strip()
            if iterable_name in context:
                for item in context[iterable_name]:
                    context[var_name] = item
                    log(item)
            else:
                raise NameError(f"Undefined list: {iterable_name}")
        else:
            raise SyntaxError("Unknown command")
    except Exception as e:
        print(f"[Error @ line {lineno}]: {line}")
        print(f"[Reason]: {str(e)}")

def run_file(filepath):
    print(f"=== Synthax: Running {filepath} ===")
    base_dir = os.path.dirname(filepath)
    with open(filepath, "r") as file:
        for lineno, line in enumerate(file, start=1):
            if line.strip().startswith("#") or line.strip() == "":
                continue
            parse_line(line, lineno, base_dir=base_dir)
    print("=== Execution Complete ===")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: synth run <file.synth>")
    else:
        run_file(sys.argv[1])