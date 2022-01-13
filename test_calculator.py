from App import App

def test_verify_correct_calculation():
    # Arrange
    app = App()
    # Act
    app.SearchPage().Search("Калькулятор")
    
    app.Calculator().ClickButton("1")
    app.Calculator().ClickButton("×")
    app.Calculator().ClickButton("2")
    app.Calculator().ClickButton("−")
    app.Calculator().ClickButton("3")
    app.Calculator().ClickButton("+")
    app.Calculator().ClickButton("1")
    app.Calculator().ClickButton("=")
    # Assert
    assert app.Calculator().Result().text == "0"
    assert app.Calculator().History().text == "1 × 2 - 3 + 1 ="
