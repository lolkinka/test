from doc import get_doc_owner_name, add_new_shelf, delete_doc, get_doc_shelf
from yandex_api import create_folder
class TestCalculatePytest:

    @classmethod
    def setup_class(cls):
        print('connect DB')

    def setup(self):
        print('create user')

    def test_list_of_documents(self):
        assert delete_doc('10006') == 'Документ с номером "10006" был успешно удален'

    def test_adding(self):
        assert add_new_shelf('123') == 'Добавлена полка "123"'

    def test_doc_name(self):
        assert get_doc_owner_name ('10006') == 'Аристарх Павлов'

    def test_get_shelf(self):
        assert get_doc_shelf('11-2') =='1'

    def test_yandex_api(self):
        assert create_folder('hello world') == 'Success'

    def teardown(self):
        print('delete user')

    @classmethod
    def teardown(cls):
        print('delete DB')
