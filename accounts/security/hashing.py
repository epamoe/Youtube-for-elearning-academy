import hashlib

class Hasher:
    
    @classmethod
    def hash(self, regist_id: int) -> str:
        return hashlib.sha224(f"{regist_id}".encode("ascii","ignore")).hexdigest()
        