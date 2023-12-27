class ValidationError(Exception):
    def __init__(self, message, errors):            
        super().__init__(message)

        self.errors = errors

class LineParser():
    """
    Responsible for splitting the script and stripping it of any lines not important to the Python interpreter, i.e. comments or whitespace.
    """
    def __init__(self, script: str, write_to_file: bool = False, file_name: str = ""):
        self.script = script
        self.write_to_file = write_to_file
        self.file_name = file_name

    def Parse(self) -> list[str]:
        script = self.script

        script_lines = script.split('\n')

        count = 0
        continue_loop = True

        script_lines = [line for line in 
                        [line for line in script_lines if line != ""]
                        if not line.startswith("#")]
        
        """if self.write_to_file == True:
            with open(f"{self.file_name}.min.py", "w") as fp:
                fp.write("\n".join(script_lines))
                fp.close()"""

        return script_lines