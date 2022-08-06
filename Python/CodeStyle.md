# Code Style

We use the standard PEP8 to format our code with some clarifications:

**1. The maximum line length is 120.** `FLAKE8`

**2. We use single quotes (') for one-line strings except for the case when there is an apostrophe in the string.** `FLAKE8`

```python
# not good
"some string"

# good ones
'some string'
"Nancy's smile is charming"
```

**3. We use triple double quotes for docstrings and multiline strings.** `FLAKE8`

```python
"""
Some long text
"""
```

**4. Imports must be absolute and grouped by the origin of imported modules. The order of groups is described below:** `FLAKE8`
```python
# builtin modules
import os
from sys import path

# third-party imports
import requests
from django.contrib.auth.models import User

# local imports
from vendor.models import Application
```
**5. Do not use a slash for breaking a line of code.** `FLAKE8` `BLACK`
```python
# not good
some_object \
  .call_method(param1, param2) \
  .call_other(keyword=value) \
  .finalize()
  
# good
some_objects.call_method(
    param1, param2,
).call_other(
    keyword=value
).finalize()
```
6. **A preferred way of text wrapping:** `BLACK`
```python
fields = (
    'id',
    'rate_period',
    'rate_currency',
    'rate_sum',
)

def some_func(
    param1,
    param2,
    param3,
    param4,
    param5,
    param6,
):
    ...
```


## Naming Conventions

**1. Classes**

- A class name must be a singular noun (the exception is unused words in the singular - 'News' for example).
- Name a class by its action. (`-Writer`, `-Builder`, `-Reader` & etc.).
- Use CamelCase.
```python
# not good
class HandlerExceptions:
  ...

class GalaxiesInMultiUniverses:
  ...

# good
class UserContact:
  ...

class EventSerializer:
  ...

class FileWriter:
  ...
```

**2. Variables**

- Never use the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase letter eye) as single character variable names.
- Don't use single character name.
- The name should be short and describe the instance of variable.
- Use snake_case.
```python
# not good
temp = 'something'
data = {}
a = 1
l = 'letter'
string = 'STRING'


# good
apples = 20
interests = ['music', 'writing', 'sport']
future_date = datetime.datetime(year=2021, month=10, day=5)
```
**3. Constants**

- Write only in UPPER_CASE.
- Divide words by underscore.
```python
# not good
constant = 'Some String'

# good
VERY_USEFUL_CONST = 'Some String'
```
**4. Methods & Functions**

Always starts from verb: `get_`, `set_`, `create_` & etc.:
```python
# not good
def data_changer(data: dict):
  ...

def speech_recognizer(voice_message: bytes):
  ...

# good
def set_name(name: str):
    ...

def get_location(timezone: str, accuracy: float):
    ...
```
- It’s a good practice to mark methods as private and protected if they are not used outside the class.
    ``` python
    # not good
    class Base:
        
      def private_method(self):
        ...
      
      def call_private(self):
        return self.private_method()
    
    # good
    class ProtectedMethodCaller:
        
      def _first_private_method(self):  # protected method
        ...
      
      def call_first_private(self):
        return self._first_private_method()
    
    
    class PrivateMethodCaller:
        
      def __second_private_method(self):  # private method
        ...
      
      def call_second_private(self):
        return self.__second_private_method()
    ```
**5. Boolean fields or instances always starts with** `is_`:
```python
# not good
blocked = False
credit_card = True

# good
is_blocked = False
is_credit_card = True
```


## Good Practices
### **Note:**
```
The Python runtime does not enforce function and variable type annotations. 
They can be used by third party tools such as type checkers, IDEs, linters, etc.
```
**1. Use typehints and type annotations in methods and functions.**

- Always write typehints for output data.
- Always write type annotations for params in functions and methods - for each input variable.
``` python
# not good
def get_location(city_name, accuracy):
    ...
    return 'location'


def create_event(...):
    ...
    return Response(serializer.data, status=HTTP_201_CREATED)


def get_is_admin(self, user):
    ...
    return is_admin
  
# good
def get_location(city_name: str, accuracy: float) -> str:
    ...
    return 'location'


def create_event(...) -> Response:
    ...
    return Response(serializer.data, status=HTTP_201_CREATED)


def get_is_admin(self, user: User) -> bool:
    ...
    return is_admin
```
**2. Use data structures.**

This is a good practice to avoid mistakes in responses.
``` python
# not good
def get_city_location(city_name: str) -> typing.Dict:
  ...
  result = {'city_name': city_name,
            'location': '9.80°N, 71.56°W',
            'is_megapolis': True}
  return result

# good
@dataclass
class CityLocationHolder:
     city_name: str
     location: str
     is_megapolis: bool


def get_city_location(city_name: str) -> CityLocationHolder:
  return CityLocationHolder(
      city_name=city_name,
      location='9.80°N, 71.56°W',
      is_megapolis= True,
      )
```
- Use the same structure of response for different situations in the same endpoint.
    ``` python
    # not good
    def get_some_tags(self) -> typing.Dict:
        if condition:
          return ['music', 'sport']
        else:
          return {'my_tags': ['music', 'sport'],
                  'friend_tags': ['art']}
    
    # good
    def get_some_tags(self) -> typing.Dict:
        if condition:
          return {'my_tags': ['music', 'sport'],
                  'friend_tags': []}
        else:
          return {'my_tags': ['music', 'sport'],
                  'friend_tags': ['art']}
    ```


## Tests

**1. Directory tree for app with tests.**

Create tests in the same app with code under test. Follow this directories example:
```
./events
├──migrations
│  ├──migration_01.py
│  ├──migration_02.py
│  └──migration_03.py
├──templates
│  └──index.html
├──tests
│  ├──models
│  │  ├──__init__.py
│  │  ├──test_first_model.py
│  │  └──test_second_model.py
│  ├──recievers
│  │  ├──__init__.py
│  │  ├──test_first_reciever.py
│  │  └──test_second_reciever.py
│  ├──tasks
│  │  ├──__init__.py
│  │  └──test_main_task.py
│  ├──views
│  │  ├──__init__.py
│  │  ├──event_view_set
│  │  │  ├──__init__.py
│  │  │  ├──test_list.py
│  │  │  └──test_retrive.py
│  │  ├──another_view_set
│  │  │  ├──__init__.py
│  │  │  └──test_create.py
│  │  └──users_event_view_set
│  │     ├──__init__.py
│  │     └──test_patch.py
│  ├──__init__.py
│  └──factories.py
├──__init__.py
├──admin.py
├──apps.py
├──filters.py
├──forms.py
├──models.py
├──recievers.py
├──tasks.py
├──urls.py
└──views.py
```
- Create Tests directory as a Python package with `__init__.py` file.
- Group tests by code files.
```
./tests
├──models
│  └──...
├──recievers
│  └──...
├──tasks
│  └──...
├──views
│  └──...
├──__init__.py
└──factories.py
```
|**Note: pytest's requirement.**|
|-------|
|Name of test file always starts from `test_`: `test_module.py`.|

- Name test files by name of units to be tested. Examples:
  - `test_event_reciever.py`
  - `test_send_email.py`
  - `test_patch.py` (in `.tests/views/event_view_set` for example)

- Name of tested code should be included only in directory name or test file name.
    ```
    ./tests
    ├──views
    │  ├──user_view_set
    │  │  ├──test_patch.py  # don't include 'user_view_set'
    │  │  ├──test_post.py
    │  │  └──...
    │  ├──event_view_set
    │  │  └──...
    │  ├──author_view_set
    │  │  └──...
    │  └──...
    ├──...
    ...
    ```
**2. Inside test file.**

- Place fixtures as close as possible to tests that use them.
- It's a good practice to locate fixtures in the same file with tests. Place fixtures before any tests.
    ``` python
    # test_celery_task.py
    
    
    @pytest.fixture(autouse=True)
    def celery_mock(mocker):
        return mocker.patch('app.celery.call')
    
    @pytest.mark.django_db
    def test_something(celery_mock):
        ...
        
        celery_mock.assert_called_once_with(...)
    ```
- Tests naming.
   - A test name should describe the test conditions. It doesn’t matter how long it is.
    ``` python
    def test_patch_with_extra_query_params(...):
          ...
    
    def test_patch(...):
          ...
    ```
  - Don't repeat name of tested code in test names.
    ``` python
    # not good
    def test_events_view_set_patch(...):
          ...
    
    def test_events_view_set_post(...):
          ...
    
    def test_events_view_set_list(...):
          ...
    
    # good
    def test_patch(...):
          ...
    
    def test_post(...):
          ...
    
    def test_list(...):
          ...
    ```
- A correct test structure:
  - preparing the test situation
  - calling a unit of code to be tested
  - check results

Example:
``` python
@pytest.mark.django_db
def test_patch_something(user_client, user):
    # Prepare data.
    patch_data = {patching_data}
    
    # Run the code under test.
    something_list_url = reverse('something-detail', args=[user.username])
    response = user_client.patch(something_list_url, data={'something': patch_data})
    user.refresh_from_db()

    # Assert results
    assert response.status_code == 200
    assert ...

```
- Divide test cases by responses.
- Don't check different responses in the same test.
``` python
# not good
@pytest.mark.django_db
@pytest.mark.parametrize('name', ['name', 'name_with_mistake'])
def test_search(user, user_client, name):
    response = user_client.get(URL, data={'name': name})

    if response.status_code == 200:
      ...
    if response.status_code == 404:
      ...

# good
@pytest.mark.django_db
def test_search(user, user_client, name):
    response = user_client.get(URL, data={'name':'name'})

    assert response.status_code == 200
    ...


@pytest.mark.django_db
def test_search_with_error(user, user_client):
    response = user_client.get(URL, data={'name': 'name_with_mistake'})

    assert response.status_code == 404
    ...

```
- To check test's results on several situations always use @pytest.mark.parametrize.
- Don't write new test for check result on different input data.
``` python
# not good
@pytest.mark.django_db
def test_search_name_first(user, user_client):
    response = user_client.get(URL, data={'name': 'Vasiliy'})

    assert response.status_code == 200
    ...

@pytest.mark.django_db
def test_search_name_second(user, user_client):
    response = user_client.get(URL, data={'name': 'Petya'})

    assert response.status_code == 404
    ...

# good

@pytest.mark.django_db
@pytest.mark.parametrize('name', ['Vasiliy', 'Petya'])
def test_search_name_second(user, user_client, name):
    response = user_client.get(URL, data={'name': name})

    assert response.status_code == 200
    ...

```
- Mock all calls to other services. Example:
``` python
@pytest.fixture(autouse=True)
def celery_mock(mocker):
    return mocker.patch('app.celery.call')

@pytest.mark.django_db
def test_something(celery_mock):
    ...
    
    celery_mock.assert_called_once_with(...)

```

## External Tools

To check and format the code according to this standard we use the following tools.

<table>
  <tr>
    <th>
      Tool
    </th>
    <th>
      Description
    </th>
    <th>
      Settings
    </th>
    <th>
      How to use
    </th>
  </tr>
  <tr>
    <th>
      flake8	
    </th>
    <th>
      Checks the code for conformity to PEP8
    </th>
    <th>
      <pre>
max-line-length = 120
inline-quotes = single
multiline-quotes = double
docstring-quotes = double
import-order-style = smarkets
ban-relative-imports = true
      </pre>
    </th>
    <th>
      <ol>
        <li>Run from sources root: <pre>flake .</pre></li>
        <li>Add flake8 plugin to your code editor so it could make checks automatically</li>
        <li>flake8 is called for every pull-request as a build step</li>
      </ol>
    </th>
  </tr>
  <tr>
    <th>
      black
    </th>
    <th>
      Formats the code according to PEP8.
    </th>
    <th>
      <pre>--line-length=120 --skip-string-normalization</pre>
    </th>
    <th>
      The best way to use it is to setup a plugin for your code editor and call it on save or by Ctrl+B e.g.
    </th>
  </tr>
</table>

**1. flake8**

- Always run flake8 command before push. For example:

    `docker-compose run --rm backend flake8 .`

**2. black**

- Turn on black formatter in your IDE. Code style must be the same for each team member.
- Bind hot key for black. It helps you use formatter faster. (In Pycharm you can add it like External Tool.)

**3. pytest**

- If you are writing a new part of code don't forget to write tests.
- Run the pytest command before each push.
- Don't forget mock calls to Celery, Redis & etc. (TURN OFF CELERY AND REDIS TO CHECK)
    
    `docker-compose run --rm backend pytest`

- Check coverage by using this command:
    
    `docker-compose run --rm backend pytest --cov=. --cov-report=html`

- To recreate test DB add `--create-db` key. It will drop the current test DB and create a new one from scratch.

    `docker-compose run --rm backend pytest --createdb -vv`

**4. Swagger**

- Add swagger documentation after creation a new endpoint. Example:
    ``` python
    from drf_yasg import openapi
    from drf_yasg.utils import swagger_auto_schema
    
    @swagger_auto_schema(
        operation_summary='Operation summary',
        responses={200: Serializer(many=True), 401: 'Unauthorized', 400: 'Bad request'},
        manual_parameters=[
            openapi.Parameter(
                name='name',
                in_=openapi.IN_QUERY,
                required=True,
                type=openapi.TYPE_STRING,
            )
        ],
    )
    def list(self, request, *args, **kwargs):
            ...
    ```