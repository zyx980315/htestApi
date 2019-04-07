import pytest
@pytest.fixture(scope='module',autouse='True')
def class_fisture():
    print("module start")
    yield
    print("module end")