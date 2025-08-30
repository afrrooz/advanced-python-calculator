HISTORY_FILE = "history.txt"
def save_history(expression, result):
    with open(HISTORY_FILE, "a") as f:
        f.write(f'{expression} = {result}\n')

def view_history():
    try:
        with open(HISTORY_FILE, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "No history found!."
