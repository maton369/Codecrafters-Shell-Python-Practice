import os
import sys
import subprocess

BUILTINS = {"echo", "exit", "type", "pwd", "cd"}


def find_executable_in_path(command_name: str) -> str | None:
    path_env = os.environ.get("PATH", "")

    for directory in path_env.split(os.pathsep):
        if not directory:
            continue

        candidate = os.path.join(directory, command_name)

        if os.path.isfile(candidate) and os.access(candidate, os.X_OK):
            return candidate

    return None


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        try:
            command = input()
        except EOFError:
            break

        parts = command.strip().split()

        if len(parts) == 0:
            continue

        if parts[0] == "exit":
            break

        elif parts[0] == "type":
            if len(parts) < 2:
                continue

            target = parts[1]

            if target in BUILTINS:
                print(f"{target} is a shell builtin")

            else:
                executable_path = find_executable_in_path(target)

                if executable_path:
                    print(f"{target} is {executable_path}")

                else:
                    print(f"{target}: not found")

        elif parts[0] == "echo":
            print(" ".join(parts[1:]))

        elif parts[0] == "pwd":
            print(os.getcwd())

        elif parts[0] == "cd":
            if len(parts) < 2:
                continue

            target_dir = parts[1]

            try:
                os.chdir(target_dir)
            except FileNotFoundError:
                print(f"cd: {target_dir}: No such file or directory")

        else:
            executable_path = find_executable_in_path(parts[0])
            if executable_path is not None:
                subprocess.run(parts)
            else:
                print(f"{parts[0]}: command not found")


if __name__ == "__main__":
    main()
