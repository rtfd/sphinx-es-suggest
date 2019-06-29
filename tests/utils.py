# -*- coding: utf-8 -*-

"""Utils for testing."""

import os


class InjectJsManager:
    """
    Context manager for injected script tag.

    This will insert ``html_tag`` after the script tag which inserts
    jquery.js to the file which is passed when entered.
    And it will remove that line when exiting from it.
    """
    def __init__(self, file, html_tag):
        self._file = file
        self._script = html_tag

    def __enter__(self):
        if os.path.exists(self._file):
            with open(self._file, 'r+') as f:
                self.old_content = f.read()
                new_content = self.old_content.replace(
                    '<script type="text/javascript" src="_static/jquery.js"></script>',
                    '<script type="text/javascript" src="_static/jquery.js"></script>' + self._script
                )
                f.seek(0)
                f.write(new_content)
        
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if os.path.exists(self._file):
            with open(self._file, 'w') as f:
                f.write(self.old_content)


def set_viewport_size(driver, width, height):
    """Sets the viewport size to the given width and height."""
    window_size = driver.execute_script(
        """
        return [window.outerWidth - window.innerWidth + arguments[0],
            window.outerHeight - window.innerHeight + arguments[1]];
        """,
        width,
        height
    )
    driver.set_window_size(*window_size)