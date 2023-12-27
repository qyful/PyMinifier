class LineParser():
    """
    Responsible for splitting the script and stripping it of any lines not important to the Python interpreter, i.e. comments or whitespace.
    """
    def __init__(self, script: str):
        self.script = script

    def Parse(self) -> list[str]:
        script = self.script

        script_lines = script.split('\n')

        count = 0
        continue_loop = True
        
        script_lines = [line.replace("    ", "	") for line in
                        [line for line in script_lines if line != ""]
                        if not line.startswith("#")]
        
        self.Minify_LOIs(script_lines)
    
        return script_lines
    
    def Minify_LOIs(self, script_lines: list[str]) -> list[str]:
        line_LOIs = []
        count = 1
        
        for line in script_lines:
            line_LOIs.append(len(line) - len(line.lstrip('	')))

        indentation_levels = []

        for i in range(1, len(line_LOIs)):
            if line_LOIs[i] == line_LOIs[i - 1]:
                count += 1
            else:
                indentation_levels.append((count, line_LOIs[i - 1]))
                count = 1
        
        indentation_levels.append((count, line_LOIs[-1]))

        print(indentation_levels)