import os

# Automatically detect current folder location
main_folder = os.path.dirname(os.path.abspath(__file__))

# Create 15 session folders
for session in range(1, 16):

    session_folder = os.path.join(
        main_folder, f"Session_{session:02d}"
    )

    os.makedirs(session_folder, exist_ok=True)

    # Create 5 question files in each session
    for question in range(1, 6):

        file_path = os.path.join(
            session_folder, f"Question_{question:02d}.py"
        )

        with open(file_path, "w") as file:
            file.write("# Assignment Question\n\n")

print("15 Sessions with 5 Questions each created successfully!")