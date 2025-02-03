# RapidMate

RapidMate is a Python-based utility for managing power settings and creating custom power plans on Windows. It enables you to list available power plans, create new custom plans, delete existing ones, and set a power plan as active.

## Features

- List all available power plans.
- Create a custom power plan based on an existing one.
- Delete a power plan using its GUID.
- Set a specific power plan as the active plan.

## Requirements

- Windows operating system.
- Administrative privileges to execute power management commands.
- Python 3.6 or later.

## Installation

1. Ensure you have Python installed on your Windows machine.
2. Clone this repository or download `rapidmate.py`.

## Usage

1. Open a command prompt with administrative privileges.
2. Navigate to the directory containing `rapidmate.py`.
3. Run the script using Python:

   ```bash
   python rapidmate.py
   ```

4. Follow the example in the script to create, delete, or set active power plans by modifying the commented section in `main()` function.

## Example

```python
# Example usage
rapid_mate.create_power_plan("My Custom Plan", "Custom power plan based on balanced", "381b4222-f694-41f0-9685-ff5bb260df2e")
rapid_mate.set_active_power_plan("new-plan-guid")
rapid_mate.delete_power_plan("plan-guid-to-delete")
```

## Note

- The script requires administrative privileges to modify power settings. Make sure to run it as an administrator.
- Use the GUID of the existing plan as a template when creating a new plan.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.