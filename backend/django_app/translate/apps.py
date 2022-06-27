from django.apps import AppConfig
from argostranslate import translate as argo_translate
from googletrans import Translator as goog_translator


def get_translator(from_code, to_code):
    installed_languages = argo_translate.get_installed_languages()
    from_lang = list(filter(
        lambda x: x.code == from_code,
        installed_languages))[0]
    to_lang = list(filter(
        lambda x: x.code == to_code,
        installed_languages))[0]
    return from_lang.get_translation(to_lang)


class TranslateConfig(AppConfig):
    name = 'translate'
    # Example access: TranslateConfig.translators['es']['en']
    argo_translators = {'es': {'en': get_translator('es', 'en')},
                   'en': {'es': get_translator('en', 'es')}}

    google_translator = goog_translator()
