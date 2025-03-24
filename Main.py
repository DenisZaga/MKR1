import streamlit as st

# Українські голосні та приголосні
vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ"
consonants = "бвгґджзйклмнпрстфхцчшщБВГҐДЖЗЙКЛМНПРСТФХЦЧШЩ"

# Функція для підрахунку голосних і приголосних
def count_letters(text):
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1

    return vowel_count, consonant_count

# Інтерфейс Streamlit
st.title("🔡 Підрахунок голосних і приголосних")
st.write("Введіть текст, потім натисніть кнопку для аналізу:")

# Поле для введення тексту
user_input = st.text_area("Текст:")

# Кнопка запуску підрахунку
if st.button("🔍 Порахувати"):
    if user_input.strip() != "":
        vowels_num, consonants_num = count_letters(user_input)
        st.subheader("📊 Результати аналізу:")
        st.write(f"🔴 Кількість голосних: **{vowels_num}**")
        st.write(f"🔵 Кількість приголосних: **{consonants_num}**")
    else:
        st.warning("Будь ласка, введіть текст перед підрахунком.")
