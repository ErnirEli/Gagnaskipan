"""
Browser Navigation Simulator (Problem 1)

Implements back/forward functionality similar to web browsers.

Author: Generated for assignment use
"""

from typing import List
from datetime import datetime


class BrowserHistoryError(Exception):
    """Custom exception for browser history errors."""
    pass


class BrowserHistory:
    """
    A class to simulate browser navigation using two stacks:
    - back_stack: stores previously visited pages
    - forward_stack: stores pages we can go forward to
    """

    def __init__(self):
        self.current_page = None
        self.back_stack: List[str] = []
        self.forward_stack: List[str] = []
        self.history_stack: List[str] = []

    def visit(self, page: str) -> str:
        """
        Visit a new page.

        Args:
            page (str): The page name to visit.

        Returns:
            str: The current page after visiting.
        """
        if not isinstance(page, str) or not page.strip():
            raise BrowserHistoryError("Invalid page name.")

        if self.current_page is not None:
            self.back_stack.append(self.current_page)
            

        self.current_page = page.strip()
        self.forward_stack.clear()  # Clear forward history
        self.history_stack.append((page, datetime.now().strftime("%H:%M:%S")))

        return self.current_page

    def back(self) -> str:
        """
        Go back to the previous page.

        Returns:
            str: The page after going back.
        """
        if not self.back_stack:
            raise BrowserHistoryError("No pages in back history.")

        self.forward_stack.append(self.current_page)
        self.current_page = self.back_stack.pop()

        return self.current_page

    def forward(self) -> str:
        """
        Go forward to the next page.

        Returns:
            str: The page after going forward.
        """
        if not self.forward_stack:
            raise BrowserHistoryError("No pages in forward history.")

        self.back_stack.append(self.current_page)
        self.current_page = self.forward_stack.pop()

        return self.current_page
    
    def history(self) -> list[str]:
        """
        Return a list of history"""

        if not self.history_stack:
            raise BrowserHistoryError("No pages in history.")

        return self.history_stack


def process_command(browser: BrowserHistory, command: str) -> str:
    """
    Processes a single command.

    Args:
        browser (BrowserHistory): The browser instance.
        command (str): The input command.

    Returns:
        str: Output message.
    """
    if not isinstance(command, str) or not command.strip():
        return "Error: Empty command."

    parts = command.strip().split()

    try:
        if parts[0] == "visit":
            if len(parts) < 2:
                return "Error: 'visit' requires a page name."
            return browser.visit(" ".join(parts[1:]))

        elif parts[0] == "back":
            return browser.back()

        elif parts[0] == "forward":
            return browser.forward()
        
        elif parts[0] == "history":
            return browser.history()

        else:
            return f"Error: Unknown command '{parts[0]}'."

    except BrowserHistoryError as e:
        return f"Error: {str(e)}"


def main():
    """
    Main loop for reading commands from terminal.
    """
    browser = BrowserHistory()

    print("Browser Simulator (type 'exit' to quit)")
    while True:
        try:
            command = input("> ")

            if command.lower() == "exit":
                print("Exiting...")
                break

            result = process_command(browser, command)
            if isinstance(result, list):
                for k in result:
                    print(f'{k[0]:<20}:{k[1]:>20}')
            else:
                print(result)

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    main()
