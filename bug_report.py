class Bug:
    def __init__(self, bug_id, title, description, severity, status="Open"):
        self.bug_id = bug_id
        self.title = title.strip()
        self.description = description.strip()
        self.severity = severity.strip()
        self.status = status

    def validate_report(self):
        missing_fields = []
        if not self.title:
            missing_fields.append("title")
        if not self.description:
            missing_fields.append("description")
        if not self.severity:
            missing_fields.append("severity")

        if not missing_fields:
            return "VALID"
        else:
            fields_str = "', '".join(missing_fields)
            return f"Error: The bug report is missing data in the following field(s): '{fields_str}'."

def read_bug_data(file_path):
    bug_list = []
    try:
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) != 4:
                    print(f"Warning: Skipping invalid line: {line}")
                    continue
                bug_id, title, description, severity = parts
                bug_list.append({
                    "bug_id": bug_id,
                    "title": title,
                    "description": description,
                    "severity": severity
                })
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    return bug_list

def process_and_save_report(data_list, output_file):
    try:
        with open(output_file, "w") as f_out:
            for data in data_list:
                bug = Bug(
                    bug_id=data["bug_id"],
                    title=data["title"],
                    description=data["description"],
                    severity=data["severity"]
                )
                status = bug.validate_report()
                f_out.write(f"Bug ID {bug.bug_id}: {status}\n")
        print(f"Validation results saved to {output_file}")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    input_file = "bugs.txt"
    output_file = "bug_report.txt"

    bug_data = read_bug_data(input_file)
    process_and_save_report(bug_data, output_file)
