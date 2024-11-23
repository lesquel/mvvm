class Task:
    def __init__(self, title: str, description: str) -> None:
        self.title = title
        self.description = description
        self._completed = False
    
    def toggle(self): 
        self._completed = not(self._completed)