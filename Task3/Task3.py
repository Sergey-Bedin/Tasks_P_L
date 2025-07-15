import json
import sys

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=1)

def fill_values(test_data, values_map):
    if isinstance(test_data, dict):
        if 'id' in test_data and 'value' in test_data:
            test_id = test_data['id']
            if test_id in values_map:
                test_data['value'] = values_map[test_id]
        if 'values' in test_data:
            for item in test_data['values']:
                fill_values(item, values_map)
    elif isinstance(test_data, list):
        for item in test_data:
            fill_values(item, values_map)

def main():
    if len(sys.argv) != 4:
        print("Usage: python Task3.py values.json tests.json report.json")
        sys.exit(1)

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    try:
        values_data = load_json_file(values_file)
        tests_data = load_json_file(tests_file)

        values_map = {item['id']: item['value'] for item in values_data['values']}

        if 'tests' in tests_data:
            for test in tests_data['tests']:
                fill_values(test, values_map)

        save_json_file(tests_data, report_file)
        print(f"Report successfully saved to {report_file}")

    except FileNotFoundError as e:
        print(f"Error: File not found - {e.filename}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()

#python Task3.py values.json tests.json report.json