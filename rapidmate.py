import ctypes
import os
import subprocess
import sys

class RapidMate:
    def __init__(self):
        self.GUID_MAX_LENGTH = 39
        self.POWERCFG_CMD = "powercfg"

    def _run_command(self, command):
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
            return None

    def list_power_plans(self):
        command = [self.POWERCFG_CMD, "/list"]
        output = self._run_command(command)
        if output:
            print("Available Power Plans:")
            print(output)

    def create_power_plan(self, name, description, based_on_plan_guid):
        command = [
            self.POWERCFG_CMD, "/duplicatescheme", based_on_plan_guid
        ]
        output = self._run_command(command)
        if output:
            new_plan_guid = output.split()[-1]
            rename_command = [
                self.POWERCFG_CMD, "/changename", new_plan_guid, name, description
            ]
            self._run_command(rename_command)
            print(f"Created new power plan {name} with GUID: {new_plan_guid}")

    def delete_power_plan(self, plan_guid):
        command = [self.POWERCFG_CMD, "/delete", plan_guid]
        self._run_command(command)
        print(f"Deleted power plan with GUID: {plan_guid}")

    def set_active_power_plan(self, plan_guid):
        command = [self.POWERCFG_CMD, "/setactive", plan_guid]
        self._run_command(command)
        print(f"Set power plan with GUID {plan_guid} as active")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False

def main():
    if not is_admin():
        print("This script requires administrative privileges. Please run as administrator.")
        return

    rapid_mate = RapidMate()
    rapid_mate.list_power_plans()

    # Example usage
    # rapid_mate.create_power_plan("My Custom Plan", "Custom power plan based on balanced", "381b4222-f694-41f0-9685-ff5bb260df2e")
    # rapid_mate.set_active_power_plan("new-plan-guid")
    # rapid_mate.delete_power_plan("plan-guid-to-delete")

if __name__ == "__main__":
    main()