#!/usr/bin/env python3

directory = '/'

def main():
    print(r"""
                    -*%@@%*-
                .=#@@@@@@@@@@#=.
            .=%@@@@@*-..-*@@@@@%=.
          -#@@@@@+:        :+@@@@@#-
        :*@@@@@*:              :*@@@@@*:
      =%@@@@#-                    -#@@@@%=.
    *@@@@@+.                        .+@@@@@*
    *@@*-   *@@*      *@@*      *@@*   :*@@*
            @@@@      @@@@      @@@@
            @@@@      @@@@      @@@@
            @@@@      @@@@      @@@@
            @@@@      @@@@      @@@@
            @@@@      @@@@      @@@@
            @@@@      @@@@      @@@@
            @@@@      @@@@      @@@@
            *@@*      *@@*      *@@*

      *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*
      *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*

            Welcome to the HCB CLI!
     """)
    while True:
        print(directory + '> ', end='')
        args = input().strip().split()
        if not args:
            continue
        match args[0].lower():
            case 'help':
                help()

            case 'exit':
                print("Exiting the HCB CLI.")
                exit(0)

            case _:
                print(f"Unknown command: {args[0]}")
                help()

def help():
    print("Available commands:")
    print("  help - Show this help message")
    print("  exit - Exit the HCB CLI")

if __name__ == "__main__":
    main()