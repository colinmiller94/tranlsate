from rest_framework.response import Response
from rest_framework.views import APIView

from translate.apps import TranslateConfig

from googletrans import Translator, constants

translator = Translator()


# Create your views here.
class CompareTranslate(APIView):
    def post(self, request):
        data = request.data
        from_lang = data['from_lang']
        to_lang = data['to_lang']
        content = data['content']

        argo_translator = TranslateConfig.argo_translators[from_lang][to_lang]
        google_translator = TranslateConfig.google_translator

        response_dict = {"Google Translate": google_translator.translate(content).text,
                         "Argos": argo_translator.translate(content)}
        return Response(response_dict, status=200)
