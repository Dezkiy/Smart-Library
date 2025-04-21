from src.book import Book

class ResourceFactory:
    @staticmethod
    def create_resource(resource_type: str, **kwargs):
        if resource_type.lower() == "book":
            return Book(**kwargs)
        else:
            raise ValueError(f"Invalid resource type: {resource_type}")
