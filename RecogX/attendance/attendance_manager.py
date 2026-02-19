import pandas as pd
from datetime import datetime

def save_attendance(name, attendance_file):
    now = datetime.now()

    new_entry = pd.DataFrame(
        [[name, now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S")]],
        columns=["Name", "Date", "Time"]
    )

    try:
        existing = pd.read_excel(attendance_file)
        updated = pd.concat([existing, new_entry], ignore_index=True)
    except FileNotFoundError:
        updated = new_entry

    updated.to_excel(attendance_file, index=False)