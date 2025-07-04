import streamlit as st
import random

st.set_page_config(page_title="Adam Asmaca", page_icon="🪓")

# Başlık
st.title("🎉 Adam Asmaca 🎉")
st.write("Bir kelime tuttuk! Harf harf tahmin etmeye çalış. Maksimum 6 yanlış hakkın var.")

# Kelimeler ve başlangıç ayarları
if "word" not in st.session_state:
    kelimeler = ["elma", "armut", "muz", "çilek", "erik", "kiraz"]
    st.session_state.word = random.choice(kelimeler)
    st.session_state.guesses = []
    st.session_state.attempts = 6
    st.session_state.finished = False

# Adam çizimi
adam_art = [
    "   \n   \n   ",
    " o \n   \n   ",
    " o \n | \n   ",
    " o \n |\\\n   ",
    " o \n/|\\\n   ",
    " o \n/|\\\n  \\",
    " o \n/|\\\n/ \\"
]

# Tahmin edilen durumu göster
durum = [harf if harf in st.session_state.guesses else "_" for harf in st.session_state.word]
st.subheader("Kelime: " + " ".join(durum))
st.text(adam_art[6 - st.session_state.attempts])

# Oyunun bitip bitmediğine bak
if "_" not in durum:
    st.success("🥳 Tebrikler! Kelimeyi buldun!")
    st.session_state.finished = True
elif st.session_state.attempts == 0:
    st.error(f"💀 Oyun bitti! Doğru kelime: {st.session_state.word}")
    st.session_state.finished = True

# Harf tahmini
if not st.session_state.finished:
    harf = st.text_input("Bir harf gir:", max_chars=1).lower()

    if st.button("Tahmin Et") and harf:
        if not harf.isalpha():
            st.warning("Lütfen sadece harf gir.")
        elif harf in st.session_state.guesses:
            st.info("Bu harfi zaten denedin.")
        else:
            st.session_state.guesses.append(harf)
            if harf not in st.session_state.word:
                st.session_state.attempts -= 1
            st.rerun()

# Yeniden başlat
if st.button("🔁 Yeni Oyun"):
    for key in ["word", "guesses", "attempts", "finished"]:
        del st.session_state[key]
    st.experimental_rerun()
