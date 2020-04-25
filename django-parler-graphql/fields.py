import graphene

from django_parler_graphql.enums import LanguageCodeEnum
from django_parler_graphql.resolvers import resolver


class TranslatedInstanceFields(graphene.Field):
    def __init__(self, translated_model_type, resolver=resolver):
        super().__init__(
            translated_model_type,
            language_code=graphene.Argument(LanguageCodeEnum, required=True),
            resolver=resolver,
        )
