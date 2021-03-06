# BlenderBot 2.0

> July 16, 2021
Facebook Research
> 

## What is BlenderBot 2.0

<aside>
๐ก A chatbot with **its own long-term memory** and **the ability to access the internet**.

</aside>

ParlAI ๊ณต์ ๋ฌธ์์ ์๊ฐ๋ BlenderBot 2.0์ ์๊ฐํ๋ ์ฒซ๋ฒ์งธ ๋ฌธ์ฅ์ด๋ค. ๋ฌธ์ฅ ๊ทธ๋๋ก ์์ ๋ง์ ๊ณ ์ ํ long-term memory ๊ฐ์ง๊ณ , ์ธํฐ๋ท์ ์ ๊ทผํ  ์ ์๋ ๋ฅ๋ ฅ์ ๊ฐ์ง ํ์ํํ ์ฑ๋ด์ด๋ค.

## Model Architecture

![Untitled](BlenderBot 2/Untitled.png)

๊ธฐ์กด์ ๊ณ ๋ํ๋ ์ฑ๋ด(Google์ Meena, Facebook์ BlenderBot)๊ณผ ๋น๊ตํ์ ๋ BlenderBot 2.0์ด ๊ฐ์ง ์ฐจ๋ณ์ ์ ์์์ ์ค๋ชํ๋ฏ Internet Search์ Long-term Memory ๋ถ๋ถ์ด๋ค.

์ ๊ทธ๋ฆผ์ ๋ชจ๋ธ ์ ์ฒด์ ์ธ ๊ตฌ์กฐ๋ฅผ ๋ํ๋ธ ๊ทธ๋ฆผ์ผ๋ก ๋ค์๊ณผ ๊ฐ์ ํ๋ฆ์ ํตํด ์ฑ๋ด์ ์๋ต์ ์์ฑํ๋ค.

๋จผ์  ์ง๊ธ๊น์ง์ ๋๋ ๋ํ๋ฅผ ๊ธฐ๋ฐ์ผ๋ก Query Generator๋ฅผ ํตํด ์ฟผ๋ฆฌ๋ฅผ ์์ฑํ๋ค. ์ด๋ ๊ฒ ์์ฑ๋ ์ฟผ๋ฆฌ๋ Internet Search API๋ฅผ ํตํด ์ธํฐ๋ท์์ ์ฟผ๋ฆฌ์ ๋ํ ๊ฒ์ ๊ฒฐ๊ณผ ํ๋ณด๋ฅผ K๊ฐ ๋ฝ์์ค๊ณ , Long-term memory์์๋ ์ฟผ๋ฆฌ์ ํด๋นํ๋ ํ๋ณด๋ฅผ N๊ฐ ๋ฝ์์จ๋ค. ์ด๋ ๊ฒ ์์ฑ๋ ํ๋ณด๋ฅผ ์์ฑ ๋ชจ๋ธ(seq2seq ๊ฐ์)์ ์ธ์ฝ๋๋ฅผ ํตํด ์ธ์ฝ๋ฉ๋ ๋ฒกํฐ๋ฅผ ์์ฑํ๊ณ , ์์ฑ๋ ๋ฒกํฐ๋ฅผ ๋ชจ๋ ์ฐ๊ฒฐ(Concatenate)ํ๋ค. ์ฐ๊ฒฐ๋ ๋ฒกํฐ๋ฅผ ๋์ฝ๋๋ฅผ ํต๊ณผ์์ผ ๋ํ์ ์ ์ ํ ์๋ต(Response)๋ฅผ ์์ฑํ๊ฒ ๋๋ค.

## Related Papers

- [Internet-Augmented Dialogue Generation](https://parl.ai/projects/sea). Mojtaba Komeili, Kurt Shuster, Jason Weston.
    - ์์์ ์๊ฐํ BlenderBot 2.0์ ๋ ๊ฐ์ง ํน์ง ์ค ์ธํฐ๋ท์ ์ ๊ทผํ  ์ ์๋ ๋ฅ๋ ฅ์ ๋ํ๋ผ๋ฌธ
    - ์ฌ์ฉ์์ ๋ํํ๋ฉด์ ์ฟผ๋ฆฌ๋ฅผ ์์ฑํ๊ณ , ์์ฑ๋ ์ฟผ๋ฆฌ๋ฅผ API๋ฅผ ํตํด ๊ฐ๋ฅํ ํ๋ณด๊ตฐ(Candidates)์ ๋ฝ์์ ๋ํ์ ํ์ํ ์๋ต์ ์์ฑํ๋๋ฐ ์ฌ์ฉํ๋ค.
- [Beyond Goldfish Memory: Long-Term Open-Domain Conversation](https://parl.ai/projects/msc). Jing Xu, Arthur Szlam, Jason Weston.
    - ์์์ ์๊ฐํ BlenderBot 2.0์ ๋ ๊ฐ์ง ํน์ง ์ค long-term memory์ ๊ดํ ๋ผ๋ฌธ
    - ๊ธฐ์กด์ ์ฑ๋ด์ ์ฌ์ฉ๋ ๋ชจ๋ธ๋ค์ด๋ ๋ฐฉ๋ฒ๋ก ๋ค์ ์งง์ ๋ํ ๋ฐ์ดํฐ๋ฅผ ๊ธฐ๋ฐ์ผ๋ก ํ์ต๋์๊ณ , ์ด๋ก ์ธํด ๊ธด ๋ํ๊ฐ ์งํ๋๋ฉด์ ์ด์ ์ ๋๋ด๋ ๋ํ์ ์ ๋ณด๋ค์ ๊ธฐ์ตํ์ง ๋ชปํ๋ ๋ฌธ์ ๊ฐ ๋ฐ์ํ๋ค. ์ด๋ฅผ **Goldfish Memory**๋ผ๊ณ  ์นญํ๋ฉฐ ์ด๋ฅผ ํด๊ฒฐํ๊ธฐ ์ํด ์ ์๋ค์ด ๋ ๊ฐ์ง ๋ฐฉ๋ฒ์ผ๋ก **์๋ก์ด ๋ฐ์ดํฐ์ ์ ์**๊ณผ **๋ํ๋ฅผ ์์ฝํ์ฌ ์ฌ์ฉํ๋ ๋ฐฉ๋ฒ๋ก **์ ์๊ฐํ๋ค.

---

# Beyond Goldfish Memory

BlenderBot 2.0์ ํน์ง ์ค ํ๋์ธ long-term memory์ ๊ดํด ์๊ฐํ๋ ๋ผ๋ฌธ์ผ๋ก, ๋ผ๋ฌธ์ ๋ ๊ฐ์ง ํต์ฌ ํค์๋๋ ์๋์ ๊ฐ๋ค.

- ๋์ ํ๋ฆฌํฐ์ ๊ธด ๋ํ ๊ธธ์ด๋ฅผ ๊ฐ๋ Multi-Session Chat(MSC) ๋ฐ์ดํฐ์
- MSC๋ฅผ ์ํ ๋ชจ๋ธ๋ง ๋ฐฉ๋ฒ

## Multi-Session Chat

์ฑ๋ด ๊ณ ๋ํ๋ฅผ ์ํ ๋ํ ๋ฐ์ดํฐ์์ ํ๋ฆฌํฐ์ ์์ด ์ ์  ์ฆ๊ฐํ๊ณ  ์์ผ๋, ์์ง๊น์ง ํ์กดํ๋ ๋ฐ์ดํฐ์๋ค๊ณผ ์ฑ๋ด์ ์ํ SOTA ๋ชจ๋ธ๋ค์ด ๋์น๊ณ  ์๋ ๋ถ๋ถ์ ๋๋ถ๋ถ์ ์ฌ๋๋ค์ด ํ๋ ๋ํ๋ ์ค๋ ์๊ฐ ๋์ ์งํ๋๋ค๋ ์ ์ด๋ค.

๊ทธ๋ฌ๋ Human Resource์ ๋ถ์กฑ์ผ๋ก ๊ธด ๋ํ์ ๋ํ ๋ฐ์ดํฐ๋ ์ถฉ๋ถํ์ง ์๊ณ  ํ๊ท ์ ์ผ๋ก 2~15๋ฒ ์ ๋์ ๋ํ๋ฅผ ์ฃผ๊ณ  ๋ฐ๋ ๋จ์ผ ๋ํ๋ก ๊ตฌ์ฑ๋์ด์๋ค. ์ด๋ฌํ ์ด์ ๋ก ๋๋ถ๋ถ์ Dialogue task์์ SOTA ๋ชจ๋ธ๋ค(Google์ Meena, Facebook์ BlenderBot)์ ํ ํฐ ์ํ์ค์ ๊ธธ์ด๋ฅผ 128๋ก ์ ํํ์ฌ ์ฌ์ฉํ๋๋ฐ, ์ด๋ฐ ํ๊ฒฝ์ด ๊ธด ๋ํ๋ ์ฌ๋ฌ ์ฐจ๋ก์ ๊ฑธ์น ๋ํ์์ ์ข์ ์ฑ๋ฅ์ ๋ณด์ผ์ง๋ ํ์ค์น ์๋ค.

์ด๋ฅผ ์ํด ๋ผ๋ฌธ์ ์ ์๋ค์ ์ต๋ 5๋ฒ์ ๊ฑธ์ณ์ ์ต๋ 14๋ฒ์ ๋ํ๋ฅผ ์ฃผ๊ณ  ๋ฐ๋ ๋ฐ์ดํฐ์์ธ **Multi-Session Chat(MSC)**์ ๋ง๋ค์๋ค. MSC ๋ฐ์ดํฐ์์ ํน์ง์ ์๋์ ๊ฐ๋ค.

1. ๋ฐ์ดํฐ์ ์ ์์ ์ฐธ์ฌํ๋ ์ฐธ๊ฐ์๋ค์ ๊ฐ์ ์ญํ (Persona)๊ฐ ์ฃผ์ด์ง๋ค. ์ด๋ฌํ ๋ฐฉ๋ฒ์ ์ฐธ๊ฐ์๋ค์ด ์ฃผ์ด์ง ์ญํ ์ ์ํํ๊ธฐ ์ํด ๋ค์ํ ๋ํ๋ฅผ ์๋ํ๊ณ , ๋ ์ฐธ๊ฐ์๋ค์ ๊ฐ์ธ์ ๋ณด๊ฐ ๋ธ์ถ๋๋ ๋ฌธ์ ๋ฅผ ๋ฐฉ์งํ๋ค. ๊ฒ์ฆ ๋ฐ์ดํฐ์๊ณผ ํ์คํธ ๋ฐ์ดํฐ์์๋ ํ์ต ๋ฐ์ดํฐ์์์ ์ ์ด๋ ํ ๋ฒ ์ด์ ๋ฑ์ฅํ ์ญํ ์ด ์ฌ์ฉ๋์๊ณ  ์ด 1,155๊ฐ์ ์ญํ (Personas)์ด ์ฌ์ฉ๋์๋ค.
2. ์ฐธ๊ฐ์๋ค์ ๋ํ ํ๋ก๊ทธ๋จ์ ์ฌ์ฉํ์ฌ ์๋ก ๋ํ๋ฅผ ํ๋๋ฐ ํ ์ฐจ๋ก์ ๋ํ๋ฅผ ๋๋๋ ๊ฒ์ ์ธ์(Session)์ด๋ผ๊ณ  ํ๋ค. ์ฐธ๊ฐ์๋ค์ ์๋๋ฐฉ๊ณผ ์ต๋ 5๋ฒ์ ๊ฑธ์ณ ์ธ์์ ์ฐธ๊ฐํ๋ค. ์ด ๋ ์ธ์ ์ฌ์ด์ ๊ฐ๊ฒฉ์ 1~7์๊ฐ ํน์ 1~7์ผ์ ๊ฐ๋๋ค. ์ฆ, A์ B๊ฐ ํ ๋ฒ ๋ํ๋ฅผ ๋๋ ๋ค(์ธ์) 1~7์๊ฐ ํน์ 1~7์ผ ๋ค์ ๋ค์ ๋ํ๋ฅผ ๋๋๊ฒ ๋๋ค.
3. ์ด ๋ ์ฐธ๊ฐ์๋ค์ ์ด์  ์ธ์์ ๋ํ๋ฅผ ํ์ธํ  ์ ์์ง๋ง ๋ํ๊ฐ ๊ธธ์ด์ง์๋ก ์ ํ๋ ์๊ฐ ๋ด์ ์ฝ๊ณ  ์ด๋ฅผ ํ์ฉํ๋ ๊ฒ์ด ํ๋ค๊ธฐ ๋๋ฌธ์, ์ฒซ๋ฒ์งธ ์ธ์ ์ดํ๋ถํฐ๋ ์ธ์์์ ๋ฐ์ํ ๋ํ์ ์์ ์ ์์ฝํ์ฌ ๋ค์ ์ธ์์์ ์ด๋ฅผ ํ์ธํ  ์ ์๋๋ก ํ์ํ๋ค. ์ด๋ฌํ ๋ฐฉ๋ฒ์ ์ด์  ์ธ์์์ ๊ฐ ํ์์ ์์ ์ ์์ฝํ๊ธฐ ๋๋ฌธ์ ์ด๋ฅผ ๋ฐํ์ผ๋ก ์ฃผ์ด์ง ์ญํ ์ ๋ ํ์ฅํ๊ฑฐ๋ ๋ ๊น์ ๊ฐ์ฑ์ ํํํ๋ ๊ฒ๋ ๊ธฐ๋ํ  ์ ์๋ค.

![Untitled](BlenderBot 2/Untitled%201.png)

![Untitled](BlenderBot 2/Untitled%202.png)

## Modeling

- **Encoder-Decoder Transformer**

ํ์ฌ open-domain dialouge task์์ ์ ํํ๋ ๋ฐฉ๋ฒ์ Google์ Meena์์ ์ฌ์ฉํ ๊ฒ๊ณผ ๊ฐ์ด Encoder-Decoder Transformer๋ฅผ ์ฌ์ฉํ๊ฑฐ๋ BlednerBot system ๊ฐ์ด ํฐ ์ธ์ด ๋ชจ๋ธ์ ์ฌ์ฉํ๋ ๊ฒ์ด๋ค.

![Untitled](BlenderBot 2/Untitled%203.png)

์์ ๊ฐ์ด Encoder์ Decoder๋ฅผ ๊ฐ๋ Seq2Seq ๋ชจ๋ธ์ ์ฌ์ฉํ์ฌ ๋ํ๋ฅผ Encoder์ ์๋ ฅ์ผ๋ก ์ฌ์ฉํ๊ณ  Docoder๋ฅผ ํตํด ๋ํ์ ๋ํ ์๋ต์ ์์ฑํ๋ ๋ฐฉ๋ฒ์ ๊ธฐ๋ฐ์ผ๋ก ๋์ํ๋ค.

๊ทธ๋ฌ๋ ์ด๋ฌํ ๊ธฐ๋ณธ์ ์ธ Encoder-Decoder Transformer์ ์ฌ์ฉํ ๋ฐฉ๋ฒ๋ก ์๋ ๋๋ ทํ ํ๊ณ์ ์ด ์กด์ฌํ๋ค. ๋ฐ๋ก ํ์ต ๋ฐ์ดํฐ์ ์์กด์ ์ด๋ค๋ ๊ฒ์ด๋ค. ๋ชจ๋ธ์ด ํ์ต ๋ฐ์ดํฐ์ ๊ทผ๊ฑฐํ์ฌ ์๋ต์ ์์ฑํ๋ ๋ฐฉ๋ฒ์ ํ์ตํ๊ธฐ ๋๋ฌธ์ ํ์ต ๋ฐ์ดํฐ์๋ ์กด์ฌํ์ง ์๊ฑฐ๋ ๋ค๋ฅธ ๋๋ฉ์ธ์ ์ธ ํน์ฑ์ ๊ฐ์ง ๋ฐ์ดํฐ์ ๋ํด ๋์ ๊ฒฐ๊ณผ๋ฅผ ์์ฑํ๋ ๊ฒฐ์ ์ ์ธ ๋ฌธ์ ์ ์ด ์กด์ฌํ๋ค.

- **Retrieval-Augmentation**

์ด๋ฌํ ๋ฌธ์ ์ ์ ํด๊ฒฐํ๊ธฐ ์ํด RAG, FiD ๊ฐ์ Retrieval-augmentation์ด๋ผ๋ ๋ฐฉ๋ฒ๋ก ์ด ์ ์๋์๋ค. Retrieval-augmentation์ ์ธ์ฝ๋๋ฅผ ํต๊ณผ์ํฌ ์๋ ฅ ์ํ์ค๋ฅผ Retriever๋ฅผ ์ฌ์ฉํ์ฌ ์ฐพ์๋ธ ๋ค ๋ชจ๋ธ์ ์ถ๋ ฅ์ ์์ฑํ๋ ๋ฐฉ๋ฒ๋ก ์ด๋ค.

ElasticSearch๋ FAISS์ ๊ฐ์ ๊ฒ์์์ง์ ์ฌ์ฉํ์ฌ ์๋ ฅ ์ฟผ๋ฆฌ์ ์ ํฉํ Context๋ค์ ์ฐพ์๋ด๊ณ  ์ด๋ฅผ ํจ๊ป ์ฌ์ฉํด ์ธ์ฝ๋์ ๋์ฝ๋๋ฅผ ํต๊ณผ์์ผ ์๋ต์ ์์ฑํ๋ค. ์๋ฅผ ๋ค์ด, ์ํคํผ๋์ ๋คํ ํ์ผ์ ElasticSearch์ ์ธ๋ฑ์ฑ(์ ์ฅ)ํ๋ค. ๊ทธ๋ฆฌ๊ณ  ๋์ "๋ํ๋ฏผ๊ตญ์ ์๋๋ ์ด๋์ธ๊ฐ์?๋ผ๋ ์๋ ฅ ์ํ์ค๊ฐ ์ฃผ์ด์ง๋ค๋ฉด, ์ด๋ฅผ ๊ฒ์์์ง์ ํตํด ๊ด๋ จ๋ contexts๋ฅผ ๋ฝ๊ณ  ์ด๋ฅผ ๊ฐ์ด ๋ชจ๋ธ ์ธ์ฝ๋์ ์๋ ฅ ์ํ์ค๋ก ์ฌ์ฉํ์ฌ ๊ฒฐ๊ณผ๋ฅผ ๋ฝ์๋ธ๋ค.

- **Summarization Memory-Augmentation**

์์์ ์ด์ผ๊ธฐํ Retrieval-Augmentation์์ ํ์ฅ๋ ๋ฐฉ๋ฒ๋ก ์ผ๋ก, Retrieval-augmentation์ MSC ๋ฐ์ดํฐ์ ๋ํด ์ ์ฉํ  ๊ฒฝ์ฐ ๋ํ์ ํ์คํ ๋ฆฌ๋ฅผ ๋ฉ๋ชจ๋ฆฌ์ ์ ์ฅํ๊ณ  ๊ฒ์ํ์ฌ context๋ก ์ฌ์ฉํ๋ค. ๊ทธ๋ฌ๋ ์ด๋ฐ ๋ฐฉ๋ฒ์ ์๋์ ๊ฐ์ ๋ ๊ฐ์ง ๋จ์ ์ด ์กด์ฌํ๋ค.

1. ์ ์ฅํด์ผํ๋ Context๊ฐ ๋๋ฌด ๋ฐฉ๋ํ๊ณ , ๊ทธ ๋ฐฉ๋ํ Context์์ ๊ฒ์์ ์ํํด์ผ ํ๋ค.
2. ํด๋น Context(๋ํ ํ์คํ ๋ฆฌ)์ ๋ณ๋์ ์ฒ๋ฆฌ๊ฐ ๋์ด์์ง ์๊ธฐ ๋๋ฌธ์ ๋ชจ๋ธ์ด ํด๋น Context์์ ํ์ํ ์ ๋ณด๋ฅผ ์ถ์ถํ๊ณ  ์ด๋ฅผ ์ทจํฉํ๋ ๋ฑ์ ๋ง์ ์์์ ๊ฐ๋นํ๊ฒ ๋๋ค.

์ด๋ฅผ ํด๊ฒฐํ๊ธฐ ์ํด ๋ผ๋ฌธ์์๋ Context์์ ์ง์์ ๋ฝ์๋ด ์์ฝ์ ์์ฑํ๋ **Memory-Augmentation** ๋ฐฉ๋ฒ๋ก ์ ์ ์ํ๋ค. Memory-augmentation์ ๋ ๊ฐ์ง ๊ตฌ์ฑ์์๋ฅผ ๊ฐ์ง๋ค.

1. **An Encoder-Decoder Abstractive Summarizer** : ๋ํ๋ฅผ ์์ฝํ๋ ๋ชจ๋ธ๋ก ๋ํ ํ์คํ ๋ฆฌ๋ฅผ ์๋ ฅ ๋ฐ์ ํด๋น ๋ํ ํ์คํ ๋ฆฌ์ ๋ํ ์์ฝ์ ์์ฑํ๋ค. ์์ฑ๋ ์์ฝ์ด Long-term memory์ ์ ์ฅํ ์ง์ ๋ํ ์ฌ๋ถ๋ ๊ฒฐ์ ํ๋ค. ํด๋น ๋ชจ๋ธ์ MSC ๋ฐ์ดํฐ์์์ ์ ๊ณตํ๋ ์์ฝ ๋ฐ์ดํฐ๋ฅผ ์ฌ์ฉํ์ฌ Supervised Learning์ผ๋ก ํ์ต์ด ๊ฐ๋ฅํ๋ค.
2. **A Memory-Augmented Generator** : ๋ํ ํ์คํ ๋ฆฌ๋ฅผ ๋ฐ์ Long-term memory์ ์ ๊ทผํ์ฌ ์๋ง์ ์๋ต(Response)๋ฅผ ์์ฑํ๋ ๋ชจ๋ธ์ด๋ค. ํด๋น ๋ชจ๋ธ์ ๋ฉ๋ชจ๋ฆฌ์์ ๊ฒ์ํ๊ณ  ์ ์ ํ ์๋ต์ ์์ฑํ๊ธฐ ์ํด Retrieval-augmentation ๋ชจ๋ธ์ ์ฌ์ฉ ๊ฐ๋ฅํ๋ค.

ํด๋น ๋ฐฉ๋ฒ๋ก ์ ์ฌ์ฉํ์ ๋ ์ถ๊ฐ์ ์ธ ์ด์ ์ ๋ํ ํ์คํ ๋ฆฌ์ ๊ธธ์ด๊ฐ ๊ธธ๊ธฐ ๋๋ฌธ์ ๋ชจ๋ธ์ ์ ํ๋ ํ ํฐ ์ํ์ค ์ต๋ ๊ธธ์ด๋ฅผ ์ด๊ณผํ๋ ๊ฒฝ์ฐ ์๋ฆฌ๋ ๋ฌธ์ ๋ฅผ ํด์ํ  ์ ์๋ค๋ ์ ์ด๋ค.

## Benchmarks

![Untitled](BlenderBot 2/Untitled%204.png)

![Untitled](BlenderBot 2/Untitled%205.png)

![Untitled](BlenderBot 2/Untitled%206.png)

![Untitled](BlenderBot 2/Untitled%207.png)

---

# References

### BlenderBot 2.0

- [BlenderBot 2.0 article in ParlAI](https://parl.ai/projects/blenderbot2/)
- [BlenderBot 2.0 article in Facebook AI](https://ai.facebook.com/blog/blender-bot-2-an-open-source-chatbot-that-builds-long-term-memory-and-searches-the-internet)
- [BlenderBot 2.0 korean Review article](https://brunch.co.kr/@advisor/38)

### Beyond Goldfish Memory

- [Retrieval Augmented Generation artical in Facebook AI](https://ai.facebook.com/blog/retrieval-augmented-generation-streamlining-the-creation-of-intelligent-natural-language-processing-models/) : Retrieval-Augmentation ๊ด๋ จ๋ Facebook AI ๊ณต์ ์ํฐํด
- [Paper - Fusion in Docoder](https://arxiv.org/pdf/2007.01282.pdf) : Retrieval-Augmentation ๋ชจ๋ธ ์ค ํ๋๋ก ์ฌ์ฉ๋ Fusion-in-Decoder(FiD) ๋ผ๋ฌธ