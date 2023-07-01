from enum import Enum


class VectorStoreType(Enum):
    REDIS = 'redis'
    PINECONE = 'pinecone'
    CHROMA = 'chroma'
    WEAVIATE = 'weaviate'
    QDRANT = 'qdrant'

    @classmethod
    def get_enum(cls, store):
        store = store.upper()
        if store in cls.__members__:
            return cls[store]
        raise ValueError(f"{store} is not a valid vector store name.")
