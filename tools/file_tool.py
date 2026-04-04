class FileTool:
    def save_to_file(self, filename, content):
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            return f"File saved as {filename}"
        except Exception as e:
            return f"Error saving file: {str(e)}"