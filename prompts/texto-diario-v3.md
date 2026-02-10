---
layout: default
---

# prompt para un texto diario
Este prompt está en inglés, cualquier cosa hablame por (discord)[esbendev.com/discord]
Deberías reemplazar las palabras con las que estás estudiando vos.

> [!CAUTION]
> ESTOY PIDIENDOLE NOTICIAS A UNA INTELIGENCIA ARTIFICIAL... 
> El objetivo es simplemente generar texto para practicar chino. 
> ¡nunca se crean las bobadas que dice!

## detalles
 - v2 pero espero que ahora no me de cosas en inglés....


### prompt
```
Data:
- Date: {fecha} 
- Topic: {tema}
- Name: {nombre}
- Vocabulary List: {vocabulario}

Task:
Act as a Chinese language teacher. Using the Data above, write a 3-part reading exercise.

Part 1: 今日新闻  
Write 4 paragraphs (one per location: {lugares}).  
Each: 4-5 simple sentences about {tema}. Show different weather/activities/moods per city.  
Add 1 short quote per paragraph (like "今天很忙啊！").

Part 2: 生活故事  
Write 6-7 sentences about {nombre}'s typical day (morning→night).  
Place {nombre} in one city from Part 1. Use "然后", "以后" for sequence. Connect to {tema}.

Part 3: 词语检查  
4 questions in Chinese only. Mix: True/False, Multiple Choice, Short Answer.  
**Do not include any English or Pinyin translations.**  
Number each question clearly. All question content must be in Chinese characters only.

VOCABULARY RULES (FLEXIBLE):  
- Use ONLY words from Vocabulary List + 4 city names + {nombre}  
- You may add UP TO 3 new words total (not in list) if absolutely necessary for natural flow  
- List these 3 extra words at the very end of your response  
- Goal: Keep 97%+ within provided vocabulary

Output Rules:  
- 100% Chinese characters (except Date/headers)  
- Start: "你好, {nombre}!"
- No English explanations or translations anywhere in the output
```