| Cценарий                                                                                        | Действие                                                | Ожидаемый результат                                      | Фактический результат                                    | Оценка          |
|:------------------------------------------------------------------------------------------------|:--------------------------------------------------------|:---------------------------------------------------------|:---------------------------------------------------------|:----------------|
| 001-1: Запуск приложения                                                                        | Запустить приложение                                    | Запуск приложения                                        | Запуск приложения                                        | Тест пройден    |  
| 001-2: Отображение окна приложения согласно мокапу                                              | Запустить приложение                                    | Отображение окна приложения согласно мокапу              | Отображение окна приложения согласно мокапу              | Тест пройден    |
| 002-1: Корректное отображение страницы                                                          | Перейти на страницу регистрации                         | Открылась страница для регистрации                       | Открылась страница для регистрации                       | Тест пройден    |
| 002-2: Правильность валидации данных                                                            | Ввести данные, которые не удовлетворяют условию         | Уведомление пользователя, что данные введены некорректно | Уведомление пользователя, что данные введены некорректно | Тест пройден    |
| 003-1: Cуществующий маршрут                                                                     | Выбрать существующий маршрут и нажать кнопку "Search"   | Отобразились маршруты удовлетворяющие условию            | Отобразились маршруты удовлетворяющие условию            | Тест пройден    |
| 003-2: Несуществующий маршрут                                                                   | Выбрать несуществующий маршрут и нажать кнопку "Search" | Маршруты не отобразились                                 | Маршруты не отобразились                                 | Тест пройден    |
| 003-3: Поиск по дате                                                                            | Выбрать дату маршрута                                   | Найден маршрут по соотвествующей дате                    | Предложены все маршруты, не учитывая дату                | Тест не пройден |
| 004-1: Корректность информации, которая попадает в корзину                                      | Добавить маршрут в корзину                              | Данные о маршруте внесены верно                          | Данные о маршруте внесены верно                          | Тест пройден    |
| 005-1: Корректность подсчета сумм для несколькх пассажиров                                      | Добавить маршрут в корзину                              | Суммы подсчитаны корректно                               | Суммы подсчитаны корректно                               | Тест пройден    |
| 005-2: Корректность подсчета сумм для несколькх перелетов                                       | Добавить маршрут в корзину                              | Суммы подсчитаны корректно                               | Суммы подсчитаны корректно                               | Тест пройден    |
| 007-1: Попытка авторизации существующего пользователя                                           | Нажать на кнопку "Log in"                               | Открылся профиль пользователя                            | Нет возможности войти в систему                          | Тест не пройден |
| 007-2: Попытка авторизации не существующего пользователя                                        | Нажать на кнопку "Log in"                            | Отобразилась ошибка, что пользователя нет в системе      | Нет возможности войти в систему                          | Тест не пройден |


## Замечания
* Отсутствует указанный функционал в требуемые сроки
* Отсутствует инструкция к запуску приложения
* Не реализована оплата