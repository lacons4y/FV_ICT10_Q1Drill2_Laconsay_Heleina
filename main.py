from pyscript import document, display

def generate_msg(e):
    # It gets values inputted from the HTML form.
    name = str(document.getElementById("name").value)
    age = str(document.getElementById("age").value)
    school = str(document.getElementById("school").value)

    # Creates the main student information area using a multiline string
    message = f'''Student\'s Information:
Name:\t{name}
Age:\t{age}
School:\t{school}'''

    # Compiles all information also using multiline string.
    note = f'''Notes:
{name} is currently {age} years old and studies at {school}.
This information was collected through input fields and displayed using a multiline string in Python via PyScript.'''

    # It clears the previous output before displaying a new one.
    document.getElementById("msg").textContent = ""

    # Used to display both the message and the note inside the div
    document.getElementById("msg").textContent = message + "\n\n" + note

