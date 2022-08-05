# Тестирование


## Виды тестирования

1. **Static Analysis** - mypy, flake8 тд
2. **Unit** - тестирование классов, функций, фиксация кода. Внешние вызовы мокаются
3. **Integration** - тестирование интеграции с различными сервисами, микросервисами и тд.
4. **E2E** - тестирование  с вызовом допустим начиная с **_request-FE-BE-DB-BE-FE-result_**. Эмуляция сценария запускаемого пользователем

- ![img.png](pictures/testing/img.png)
- чем выше в пирамиде вид тестирования , тем сложнее писать тесты

## Линтеры, форматтеры, тайпинги

### Линтеры

1. **pep8** (pycodestyle - новое название) - самый простой линтер
2. **flake8** - оптимальный выбор. огромное количество плагинов имеет: от докстрингов, до 
3. **pylint** - более серьезная вещь, больше ошибок ищет чем flake8, но зачастую хватает flake8.

### Форматтеры

**Black** - автоматическое форматирование кода, по pep8 и выставленным правилам в конфигурационном файле

### Статические анализаторы

**mypy** - статический анализатор, проверяющий код на соответствие типам возвращаемых в функциях, методах, в параметрах и тд.
Работает только с тайпингами. Конфигурируется реагирование на различные ошибки, игнорирование проверки каких то модулей и файлов.


## Unit тесты
- проверяются отдельные модули/классы/функции

### Pytest
![img.png](pictures/testing/img2.png)

pytest парсит исходный код тестов и подменяет вызов assert в тестах на подходящую функцию, которая добавляет возможность интроспекции.

#### pytest: raises, xfail, skipif

- `raises` - отвечает за отлавливание ошибок в тесте - отловил, значит тест прошёл
    ```python
    def test_raises():
        with pytest.raises(IndexError):
            kth_stat(1, 0)
    ```
- `xfail` - позволяет пометить тест, что он сломан. помечают когда чинить долго и дорого 
/ функциональность не используется сейчас
на тестовый сценарий влиять не будет.
    
- `skipif` - позволяет какой то тест пропустить. Можно указать условие когда пропустится. Я часто использую если под какой причине тест не работает на какой то системе (Windows например)
    ```python
    @pytest.mark.xfail()
    def test_raises():
        kth_stat([1 ,2, 3], 100)
    ```
    ```python
    @pytest.mark.skipif(
        sys.platform == 'macos',
        reason='This test fails on mac',
    )
    def test_not_run_on_mac():
        assert kth_stat([1 ,2, 3], 100) == 499
    ```

#### Pytest: полезные флаги
- `--collect-only` - вывод списка найденных тестов
- `-k` - фильтрация по имени теста
- `-s` - включает вывод stdout & stderr тестов (по-умолчанию по выводятся только для упавших тестов)
- `-v` - повышает детализацию процесса запуска тестов
- `--lf`, `--last-failed` - перезапускает тесты, упавшие при последнем запуске
- `--sw`, `--stepwise` - выходит при падении и при последующих запусках продолжает с последнего упавшего теста.

From pytest-django:
- `--create-db` - принудительное повторное создание тестовой базы данных
- `--reuse-db` - повторное использование тестовой базы данных между тестовыми запусками
- `--no-migrations` - Отключить Django миграции

#### fixtures
Фикстура - функции и методы, которые запускаются для создания соответствующего окружения для теста.
1 Пример фикстуры в которой выполняется блок кода до yield, затем yield и выполняется тест, после yield - после теста
```python
@pytest.fixture()
def connection():
    connection.create()
    yeild
    connection.close()
```
2`scope` регулирует уровень доступа фикстуры. В данном случае вызывается и отрабатывает 1 раз при запуске тестов на целый модуль.
```python
@pytest.fixture(scope='module')
def call_me_once():
    print('call me once')
```
3`autouse` вызывается в любом случае, если даже явно не указывать ее в параметрах теста и не вызывать
```python
@pytest.fixture(autouse=True)
def call_me_everywhere():
    print('call me everywhere')
```

- наследование фикстур - важная вещь, чтобы не дублировать участки кода. 
Принято декомпозировать логику, чтобы избежать фикстур в 100 строк кода к примеру.
    ```python
    @pytest.fixture
    def init_db():
        print('init_db')
  
    @pytest.fixture
    def run_migrations(init_db):
        print('run_migrations')
  
    @pytest.fixture
    def create_superuser(run_migrations):
        print('create_superuser')
  
    def test_one(create_superuser):
        print('test one')

    def test_two(run_migrations):
        print('test two')
    ```
    ```
    OUTPUT:
    test_one: init_db 
              run_migrations 
              create_superuser
              test one

    test_two: init_db 
              run_migrations 
              test two
    ```
- `conftest.py` - файлик, откуда фикстура может подтягиваться без импорта явного. Принято фикстуры держать там, которые надо переиспользовать в нескольких тестах и в разных модулях.
- `pytest.ini` - основной конфигурационный файл, в котором можно изменять поведение pytest по-умолчанию
    ```
    [pytest]
    addopts = --cov-report=html --cov=<path> --flake8
    testpath = <test_paths>
    ```
- `pytest-coverage` плагин показывающий % покрытия тестами код проекта

#### parametrize
Пример:
```python
@pytest.mark.parametrize('value', [-2, '23', 7, -231])
def test_positive_float_error(value):
    cls = PositiveFloatTesting()
    with pytest.raises(ValueError):
        cls.var = value
```
**нельзя так делать**
```python
@parametrized_expand_doc(
    [
        (False, False, False, False, False, False, 3, False),
        (False, False, True, False, False, False, 3, False),
        (False, True, False, False, False, False, 5, False),
        (False, True, True, False, False, False, 6, True),
        (True, False, False, False, False, False, 4, True),
        (True, False, True, False, False, False, 4, True),
        (True, True, False, False, False, False, 6, True),
        (True, True, True, False, False, False, 6, True),
        (False, False, False, True, False, False, 3, False),
        (False, False, False, False, True, False, 3, False),
        (False, False, False, False, False, True, 3, False),
        (False, True, False, True, False, False, 6, True),
        (False, True, False, False, True, False, 6, True),
        (False, True, False, False, False, True, 6, True),
    ]
)
def test_list_smth(
    is_active,
    is_preview_mode,
    is_user_only,
    user_is_author,
    user_has_permission,
    user_in_team,
    num_queries,
    has_result,
) -> None:
...
```

есть еще библиотека hypothesis - параметризация для ленивых.
```python
from hypothesis import given
import hypothesis.strategies as st

@given(st.integers(), st.integers())
def test_ints_are_commutative(x, y):
    assert x + y == y + x
```

## Интеграционные тесты

### unittest.mock
Иногда необходимо изолировать часть программы, для того чтобы тестировать только минимально возможную часть системы,
для этого можно использовать специальные объекты подменяющие внешние объекты или функции

`unittest.mock` - это набор универсальных объектов для таких подмен.

#### Mock
`Mock` - специальный объект, на любой вызов, обращение к методам или свойствам возвращающий новый объект `Mock`
```python
>>> from unittest.mock import Mock
>>> m = Mock()
>>> m()
<Mock name='mock()' id='4513423432'>
>>> m.f()
<Mock name='mock.f()' id='4512334234'>
>>> m.is_alive
<Mock name='mock.is_alive' id='443434234'>
>>> m.call_count
1
>>> m.f.call_count
1
```

Пример:
```python
from unittest.mock import Mock

class AliveChecker:
    def __init__(self, http_session, target):
        self.http_session = http_session
        self.target = target
    
    def do_check(self):
        try:
            resp = self.http_session.get(f'https://{self.target}/ping')
        except Exception:
            return False
        else:
            return resp == 200
```
```python
def test_with_mock():
    get_mock = Mock(return_value=200)
    pseudo_client = Mock()
    pseudo_client.get = get_mock
    alive_checker = AliveChecker(pseudo_client, 'test.com')
    assert alive_checker.do_check()
    pseudo_client.get.assert_called_once_with('https://test.com/ping')


def test_with_raising_mock():
    get_mock = Mock(side_effect=Exception('EEEEE'))
    pseudo_client = Mock()
    pseudo_client.get = get_mock
    alive_checker = AliveChecker(pseudo_client, 'test.com')
    assert not alive_checker.do_check()
    pseudo_client.get.assert_called_once_with('https://test.com/ping')
```

#### patch
`patch` - позволяет подменить поведение конкретной части кода

Тут в примере патчим запуск Celery таски. И чтобы не ждать время пока она запустится и отработает - проверяем наличие того что она была запущена с определенными параметрами.
```python
from unittest.mock import patch

def test_car_post_save():
    with patch('app.another_dir.car.create.delay') as mock:
        CarFactory()
        mock.assert_not_called()
        
        car = CarFactory(enabled=True)
        mock.assert_called_once_with(part=car.part_id)
        
        car.save()
        mock.assert_called_once_with(part=car.part_id)
```
```python
import math
from unittest.mock import patch

def test_patch_sin():
    with patch('math.sin', return_value=2) as m:
        assert math.sin(0) == 2
        assert math.sin(1) == 2
        assert m.call_count == 2
```

#### freezegun
`freezegun` - библиотека, позволяющая заморозить время в тесте, чтобы исключить рандомность в тесте.
Параметрами можно настроить от времени с датой до таймзоны, что надо зафикировать в конкретном тесте.
```python
from freezegun import freeze_time
import datetime

@freeze_time('2002-03-14')
def test_smth():
    now = datetime.datetime.now()
    assert now == datetime.datetime(2002, 3, 14)
```

#### vcr
`vcr` - mock внешних http-запросов

```python
from services import get_score

@vcr.use_cassete('scores/200.yaml')
def test_get_score():
    assert get_score(1) == 21
```

При первом запуске теста ответ сохраняется в определенный `.yaml` файл. При повторных запусках теста ответ берется и подставляется из существующего файла.


#### snapshottest
`snapshottest` - библиотека позволяющая зафиксировать отрендеренный html. 

При первом запуске теста снимок загружается в определенный `.html` файл в директории `snapshots`. При повторных запусках теста ответ сравнивается в содержимым существующего файла.

#### factory-boy и faker 
Помогают генерировать данные для тестов, фабрики заменяющие реальные объекты.

## End-to-End тесты
- Тест всегда покрывает какой-то реальный сценарий использования. По-простому эмулируют поведение пользователя. 
Допустим выкладывание фото пользователем через UI - затем в бэк запрос уходит - кладет в бд - и обратно пока не покажет пользователю, что фотка загружена.

## Другие виды тестов
- `Smoke` - для минимальной функциональности сервиса, чтобы проверить запускается ли он вообще. 
Позволяет поднять и запустить сервис и проверить его на работоспособность(могут быть баги и ошибки не в важном коде для системы в целом).
- `Regression` - позволяют проверить работоспособность старой функциональности при наличии новой.
- `Compatibility` - проверка совместимости.
- `Installation` - проверка установки и инсталляции приложения / программы
- `Acceptance`
- `Alpha`
- `Beta`
- `Performance` - нагрузочное тестирование 
- `Stress` - нагрузочное тестирование 

## Полезные мысли
- не мокать весь сервис - растет процент ложноотрицательных тестов
- не писать тесты завязанные на сеть или рандом - повышается процент ложноположительных тестов
- не гнаться за 100% покрытием тестов
- в новой компании/команде, в коде которой нет тестов - начните добавлять по мере написания новой функциональности и появления багов
Не нужно бросаться писать тесты на все подряд.
- тест проверяет и фиксирует либо отдельный метод (unit, интеграционный), либо целый сценарий (e2e)
- проверять количество обращений к бд/сервису, чтобы отлавливать лишние запросы и вызовы.
- если в фун-ии есть много ифов и ситуаций, с помощью параметризации надо зайти в каждый
- тестировать код на максимально реалистичном сценарии (включать логгирование, кэширование, поднимать все вспомогательные сервисы и тд), приближайте его к продовому.
- разбитие тестов по группам (по тестируемым модулям или файлам), чтобы не было каши.
- `./requirements/` иерахичен `base.txt` для прода, потом от этого наследуется и файл для CI и тестирования, и файл для dev окружения.
## TDD (test driven development)
Методология разработки ПО при которой сначала пишется тест, а потом логику. Итеративная вещь. Пишем логику до тех пор, пока тесты не пройдут, запуская на каждый момент, когда что-то новое добавили в код.