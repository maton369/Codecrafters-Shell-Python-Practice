import sys

BUILTINS = {"echo", "exit", "type"}


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
                print(f"{target} not found")
        elif parts[0] == "echo":
            print(" ".join(parts[1:]))
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
