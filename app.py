from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source="pt", target="en")

texto = "volta o cão arrependido, com suas orelhas tão fartas, e seu osso ruido, e com o rabo entre as patas."

traducao = tradutor.translate(texto)
print(traducao)