def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template must be a string")
        return
    if not isinstance(attendees, list):
        print("Error: attendees must be a list")
        return
    for person in attendees:
        if not isinstance(person, dict):
            return "Error: attendees must be a list of dictionaries"

    if (template == ""):
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for i, person in enumerate(attendees, start=1):
        output = template

        name = person.get("name") or "N/A"
        title = person.get("event_title") or "N/A"
        date = person.get("event_date") or "N/A"
        location = person.get("event_location") or "N/A"

        output = output.replace("{name}", str(name))
        output = output.replace("{event_title}", str(title))
        output = output.replace("{event_date}", str(date))
        output = output.replace("{event_location}", str(location))

        filename = f"output_{i}.txt"
        with open(filename, "w") as f:
            f.write(output)
