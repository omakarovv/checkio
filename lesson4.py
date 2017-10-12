def find_message(text):
    text_content = list(filter(lambda x: x.isupper(), text))
    return "".join(text_content)

Когда-нибудь пробовали отправить секретное сообщение кому-то не пользуясь услугами почты? Вы можете использовать газету, чтобы рассказать кому-то свой секрет. Даже если кто-то найдет ваше сообщение, легко отмахнуться и сказать что это паранойя и теория заговора. Один из самых простых способов спрятать ваше секретное сообщение это использовать заглавные буквы. Давайте найдем несколько таких секретных сообщений.
Дан кусок текста. Соберите все заглавные буквы в одно слово в том порядке как они встречаются в куске текста.
Например: текст = "How are you? Eh, ok. Low or Lower? Ohhh.", если мы соберем все заглавные буквы, то получим сообщение "HELLO".
Входные данные: Текст как строка (юникод).
Выходные данные: Секретное сообщение как строка или пустая строка.
