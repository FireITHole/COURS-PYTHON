from datetime import datetime

class Logger:
    def __init__(self, file_path=f"./logs-{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log"):
        self.file_path = file_path
        with open(self.file_path, "w") as file:
            file.write("")

    def _write_log(self, level: str, log: str) -> None:
        now = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")

        with open(self.file_path) as file:
            file_content = file.read()

        with open(self.file_path, 'a') as file:
            file.write(f"\n[{now}] [{level}] : {log}") if file_content else file.write(f"[{now}] [{level}] : {log}")

    def info(self, log: str) -> None:
        self._write_log("INFO", log)

    def debug(self, log: str) -> None:
        self._write_log("DEBUG", log)
    
    def error(self, log: str) -> None:
        self._write_log("ERROR", log)
    
    def critical(self, log: str) -> None:
        self._write_log("CRITICAL", log)