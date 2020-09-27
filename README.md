
# Django parler graphql
Django-parler-graphql is an app that allows querying of django-parler's translatable fields with Django GraphQL (graphene).

!!! The library is still being developing. 

## Requirements
Python 3.5+

Django 2.0+

(It has not been tested with older versions. It probably compatible with older versions.)

## Installation
Installation via pip is easier way and will install all other dependency packages.
```
$ pip install django-parler-graphql
```
or can be installed over github repo.
```
$ git clone https://github.com/selmanceker/django-parler-graphql.git
$ cd django-parler-graphql
$ python setup.py sdist
$ pip install dist/django_parler_graphql-...
```

## Usage

```python
from graphene_django_optimizer.types import OptimizedDjangoObjectType
from django_parler_graphql.fields import TranslatedInstanceFields


class MyType(OptimizedDjangoObjectType):
    name = TranslationField()

    class Meta:
        description = (
            "MyType's description"
        )
        only_fields = [
            "name",
        ]
        interfaces = [graphene.relay.Node]
        model = models.MyModel

    def resolve_name(root: models.MyModel, info, language_code=None):
        return root.safe_translation_getter("name", language_code=language_code)
```

# Maintainer
- Selman Çeker <selmanceker@gmail.com>
