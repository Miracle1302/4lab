# Ревера Святослав
text = """Even though large tracts of Europe and many old and famous States have fallen or may fall into the grip of the Gestapo and all the odious apparatus of Nazi rule, we shall not flag or fail. We shall go on to the end. We shall fight in France, we shall fight on the seas and oceans, we shall fight with growing confidence and growing strength in the air, we shall defend our island, whatever the cost may be. We shall fight on the beaches, we shall fight on the landing grounds, we shall fight in the fields and in the streets, we shall fight in the hills; we shall never surrender. And even if, which I do not for a moment believe, this island or a large part of it were subjugated and starving, then our Empire beyond the seas, armed and guarded by the British Fleet, would carry on the struggle, until, in God's good time, the New World, with all its power and might, steps forth to the rescue and the liberation of the Old."""

# 1. Перетворення тексту на нижній регістр
lower_text = text.lower()

# 2. Підрахунок кількості входжень слова "shall"
count_shall = lower_text.count("shall")

# 3. Заміна "shall" на "will"
replaced_text = lower_text.replace("shall", "will")

# 4. Пошук індексу першої згадки "europe"
index_europe = lower_text.find("europe")

# 5. Перевірка, чи закінчується текст словом "old."
ends_with_old = text.endswith("Old.")

# 6. Розділення тексту на речення
sentences = text.split(".")

# 7. Об'єднання речень назад у текст через новий роздільник
joined_text = " | ".join(sentences)

# 8. Перевірка, чи текст містить слово "freedom"
contains_freedom = "freedom" in text

# 9. Використання str.capitalize() для переведення першої літери тексту у верхній регістр
capitalized_text = text.capitalize()


print("Текст у нижньому регістру:")
print(lower_text)
print("\nКількість входжень 'shall':", count_shall)
print("\nТекст з заміненими 'shall' на 'will':")
print(replaced_text)
print("\nІндекс першої згадки 'Europe':", index_europe)
print("\nЧи закінчується текст словом 'Old.':", ends_with_old)
print("\nТекст поділений на речення:")
print(sentences)
print("\nТекст об'єднаний через ' | ':")
print(joined_text)
print("\nЧи містить текст слово 'freedom':", contains_freedom)
print("\nТекст з великої букви:")
print(capitalized_text)


