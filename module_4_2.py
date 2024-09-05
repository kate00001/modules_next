def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function() # Так все работает
#inner_function() # Так не видит функцию inner_function
