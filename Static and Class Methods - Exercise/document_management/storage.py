from document_management.category import Category
from document_management.document import Document
from document_management.topic import Topic


class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    @staticmethod
    def find_object(item: str or int, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = Storage.find_object(category_id, 'id', self.categories)
        if category is not None:
            category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = Storage.find_object(topic_id, 'id', self.topics)
        if topic is not None:
            topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = Storage.find_object(document_id, 'id', self.documents)
        if document is not None:
            document.edit(new_file_name)

    def delete_category(self, category_id):
        category = Storage.find_object(category_id, 'id', self.categories)
        if category is not None:
            self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = Storage.find_object(topic_id, 'id', self.topics)
        if topic is not None:
            self.topics.remove(topic)

    def delete_document(self, document_id):
        document = Storage.find_object(document_id, 'id', self.documents)
        if document is not None:
            self.documents.remove(document)

    def get_document(self, document_id):
        document = Storage.find_object(document_id, 'id', self.documents)
        if document is not None:
            return document

    def __repr__(self):
        result = []
        for document in self.documents:
            result.append(document.__repr__())
        return '\n'.join(result)
