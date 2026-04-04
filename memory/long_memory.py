class LongMemory:
    def __init__(self, vector_store):
        self.vector_store = vector_store

    def store(self, text):
        self.vector_store.add(text)

    def search(self, query):
        return self.vector_store.search(query)