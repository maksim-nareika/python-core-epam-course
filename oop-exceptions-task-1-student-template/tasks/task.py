import math
class Pagination:
    __page_dict = {}
    def __init__(self, data, items_on_page):
        self.data = data
        self.items_on_page = items_on_page
        self.set_page_by_page_number()

    def set_page_by_page_number(self):
        text_list = list(self.data)
        page_text = ''

        for page in range(0, self.page_count):
            for i in range(0, self.items_on_page):
                if len(text_list) > 0:
                    page_text += text_list[0]
                    text_list.remove(text_list[0])
            self.__page_dict[page] = page_text
            page_text = ''


    @property
    def item_count(self):
        return len(self.data)

    @property
    def page_count(self):
        page_count = math.ceil(len(self.data) / self.items_on_page)
        return page_count

    def count_items_on_page(self, page_number):
        if page_number < 0 or page_number >= self.page_count:
            raise PaginationException("Invalid index. Page is missing")
        else:
            items_on_page = len(self.__page_dict.get(page_number))
        return items_on_page



    def find_page(self, data):
        result_pages = set()
        raise_error = []
        data_list = []

        if type(data) is str:
           data_list.append(data)
        else:
            data_list.extend(data)

        for item in data_list:
            for key, page in self.__page_dict.items():
                if item in page:
                    raise_error.append(False)
                    result_pages.add(key)
                elif (page in item and item in self.data):
                    raise_error.append(False)
                    for key2, page2 in self.__page_dict.items():
                        if page2.strip() in item:
                            result_pages.add(key2)
                else:
                    raise_error.append(True)
            if False not  in raise_error:
                raise PaginationException("\'<symbol/word>\' is missing on the pages")
        return list(result_pages)
    
    def display_page(self, page_number):
        if page_number < 0 or page_number >= self.page_count:
            raise PaginationException("Invalid index. Page is missing")
        else:
            page_text = self.__page_dict.get(page_number)
        return page_text


class PaginationException(Exception):
    pass
