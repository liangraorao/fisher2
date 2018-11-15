
class BookViewModel:

    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            "book": [],
            "total": 0,
            "keyword": keyword
        }
        if data:
            returned['total'] = 1
            returned['book'] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            "book": [],
            "total": 0,
            "keyword": keyword
        }
        if data:
            returned['total'] = data['total']
            returned['book'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def __cut_book_data(cls, data):
        res = {
            "author": '、'.join(data['author']),
            "publisher": data['publisher'],
            "summary": data['summary'],
            "title": data['title'],
            "price": data['price'],
            "pages": data['pages'] or '',
            "image": data['image']
        }
        return res

