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
 - Le puse mi nombre chino para verlo seguido y reconocerlo mejor.
 - Le estoy pidiendo noticias de Portland, Guatemala, Argentina y China porque son mis intereses, pero podés pedirle de lo que quieras!
 - Estoy pidiendo solo texto en chino. yo copio la respuesta y la pego en pleco para leer el texto.
 - un cambio grande acá es que ahora voy a usar un script de python para agregar las partes que cambian.


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

VOCABULARY RULES (FLEXIBLE):
- Use ONLY words from Vocabulary List + 4 city names + {nombre}
- You may add UP TO 3 new words total (not in list) if absolutely necessary for natural flow
- List these 3 extra words at the very end of your response
- Goal: Keep 97%+ within provided vocabulary

Output Rules:
- 100% Chinese characters (except Date/headers)  
- Start: "你好, {nombre}!"
```