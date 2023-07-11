class CustomContextManager:
    def __enter__(self):
        print("컨텍스트에 진입")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("컨텍스트를 떠남")

with CustomContextManager():
    print("컨텍스트 내부에서 작업 수행")
