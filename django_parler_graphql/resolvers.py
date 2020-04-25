from django.conf import settings


def resolver(instance, _info, language_code):
    try:
        instance = instance.get_translation(language_code=language_code)
    except:
        instance = instance.get_translation(language_code=settings.LANGUAGE_CODE)
    return instance
