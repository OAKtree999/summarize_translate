import streamlit as st
from googletrans import Translator
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords

# 제목
st.title("타오른다 봇의 요약 및 번역")
st.subheader("영어문장을 요약하고 번역해드립니다.")

# 텍스트 기입란
text = st.text_area("본문", height=300, help="이곳에 글을 작성하시면, 요약문과 번역본을 받을 수 있습니다.")

translator = Translator()
values = st.slider('몇 퍼센트 요약해드릴까요?',
                   0.3, 0.9)
btn = st. button('요약 및 번역')


if btn:
    trans = translator.translate(text, dest='ko', src='auto')
    st.success('원문 번역 \n\n' + trans.text)


if btn:
    summarize_text = summarize(text, ratio=values)
    keyword = keywords(text, ratio=values, split=True)
    print(type(keyword))
    trans_summarize = translator.translate(summarize_text, dest='ko', src='auto')
    st.success('원문 요약 \n\n' + trans_summarize.origin + '\n\n' + '요약 번역 \n\n' + trans_summarize.text)
    st.radio('키워드',keyword[:5], disabled=True)
    