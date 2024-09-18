import sys
sys.path.insert(0,"C:/Users/alekberovalf/PycharmProjects/Diplom_1/")
import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from unittest.mock import Mock
class TestBurger:

    # Тест на добавление булочки
    @pytest.mark.parametrize('name', ['Флюоресцентная булка R2-D3'])
    def test_set_buns(self, name):
        burger = Burger()
        burger.set_buns(name)
        assert burger.bun == 'Флюоресцентная булка R2-D3'

    # Тест на добавление ингридиентов
    @pytest.mark.parametrize('ingredient', ['Соус с шипами Антарианского плоскоходца'])
    def test_add_ingredient(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    # Тест на удаление ингридиентов
    @pytest.mark.parametrize('ingredients', [('Соус Spicy-X', 'Мясо бессмертных моллюсков Protostomia')])
    def test_remove_ingredient(self, ingredients):
        burger = Burger()
        burger.add_ingredient(ingredients[0])
        burger.add_ingredient(ingredients[1])
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1

    #Тест на изменения порядка ингридиентов
    @pytest.mark.parametrize('ingredient_1, ingredient_2', [('Соус фирменный Space Sauce', 'Мясо бессмертных моллюсков Protostomia')])
    def test_move_ingredient(self, ingredient_1, ingredient_2):
        burger = Burger()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == 'Мясо бессмертных моллюсков Protostomia'

    # Тест на получение цены бургера
    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_ingredient = Mock()
        mock_bun.get_price.return_value = 1337.0
        mock_ingredient.get_price.return_value = 88.0
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        assert burger.get_price() == 2762




