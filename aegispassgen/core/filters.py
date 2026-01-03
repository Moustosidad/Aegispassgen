class FilterEngine:
    def reject(self, pwd: str) -> bool:
        if len(pwd) < 6:
            return True
        if pwd.isdigit():
            return True
        return False
