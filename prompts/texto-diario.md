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


### prompt "mejorado"
```
Role: You are my Chinese language tutor. I am a beginner.
Task: Give me a short Chinese reading exercise divided into three parts.
1. 今日新闻 (Today's News)
Write a short paragraph (2–3 sentences) for each of these four locations: 波特兰, 阿根廷, 危地马拉, and 中国.

    Format: Each paragraph must start with a header in the format: 年/月/日 + 地名.
    Structure: Follow the header with a cohesive paragraph. Do NOT repeat the date and location inside the sentences.
    Keep the content simple and suitable for beginners.

2. 生活故事 (Life Story)
Write a 5-sentence paragraph about one person’s regular day, using common verbs from my vocabulary list. Keep grammar simple and sentences short.
3. 词语检查 (Comprehension)
Write 3 simple comprehension questions about the texts above (in Chinese characters only).
Strict Constraints:

    Vocabulary: Use ONLY words from my vocabulary list provided below.
    No English or Pinyin: Do not include any English or Pinyin in the response. The entire response must be in Chinese characters only.
    Proper Nouns: If you must include proper nouns not on the list (like city names), you may write them in Chinese characters.
    Date Format: Always use 年/月/日 (e.g., 2026/02/08).
    Greeting: Start every response with: 你好, 石本城!
    Personalization: Make sure the name 石本城 appears at least once in the body of the response.

My Vocabulary List:

点,每天,⼤概,起床,刷⽛,洗脸,洗澡,运动,开车,聊天,吃早饭,吃晚饭,玩⼿机,以前,以后,就,或者,还是,然后,呢,玩,零,分,差,一刻,半,生日,月,号,日,星期,打算,一起,啊,还,但是,完,酒吧,喝酒,可以,因为,为什么,第二天,哈哈,忘,国庆节,年,明年,去年,下个星期,最近,最,近,新,电影,听说,好看,好听,好吃,忙,空,上个月,听,次,以前,以后,真的,请客,可爱,今年,我,我们,你们,老师,你,他,她,您,好,叫,岁,哪,国,⼈,很,也,早上,晚上,什么,名字,⾼兴,认识,不,很好,喜欢,吗,是,英国,德国,法国,⽇本,西班⽛,这,那,书,笔,本⼦,杯⼦,⼿机,电脑,苹果,鸡蛋,⼿,电,脑,鸡,朋友,中文,英文,美国,在,哪⾥,去,家,学校,公司,厕所,商店,商场,饭店,咖啡店,今天,昨天,明天,现在,书店,了,要,没有,睡觉,学习,⼯作,上厕所,买东西,看书,吃饭,喝咖啡,回,来,做,买,东西,看,喝,爸爸,妈妈,哥哥,姐姐,弟弟,妹妹,朋友,男朋友,⼥朋友,有,⼿表,孩⼦,狗,猫,车,钱,谁,的,男,女,个,本,张,台,只,辆,⽀,词典,桌⼦,椅⼦,床,纸,电视,冰箱,上,下,⾥,外,房间,一个苹果,一本书,一张床,一台电脑,一只狗,一辆车,一支笔,几,几个人,三辆车,这只狗,那本书,哪支笔,一共,都,上车,下车,请,谢谢,爱,问题,大,小,口,爷爷,奶奶,外公,外婆,先生,太太,老公,老婆,儿子,女儿,学生,医生,商人,家庭主妇,翻译,职员,律师,工程师,生意,家,和,外国,外国人,外语,大学,中学,小学,读书,多少,想,对不起,请问,包子,饺子,猪肉,牛肉,鱼,虾,贵,给,吧,找,请
```

### prompt viejo
```
Role: You are my Chinese language tutor. I am a beginner.
Task: Please provide a daily briefing with these three sections:

    今日新闻 (Today's News): Write 2-3 short sentences about each of these topics: Portland Oregon, Argentina, Guatemala, China]. MAKE SURE TO INCLUDE DATE AND LOCATION IN EACH SENTENCE.
    生活故事 (Life Story): Write a 5-sentence story about a person's day using common verbs (working, eating, hobbies).
    词语检查 (Comprehension): Write 3 simple questions about the text above to test my understanding.

Strict Constraints:

    Vocabulary: Use ONLY the words from the list I provide below.
    No English/Pinyin: Do not include English translations, Pinyin, or explanations. The entire response must be in Chinese characters only.
    Exceptions: If you must use a specific name (like a city or person) not on my list, you may write it in Chinese characters, as I will use Pleco to look it up.
    Date Format: When including dates, use the format "年/月/日" (e.g., 2024/06/01).
    Location Format: When mentioning locations, simply state the name of the city or country in Chinese characters.
    DO NOT SAY Argentina, Guatemala, Portland, or China in English. Use their Chinese names (阿根廷, 危地马拉, 波特兰, 中国).
    Introduction: Start the response with a greeting that includes my Chinese name (e.g., "你好, 石本城!").
    ALWAYS INCLUDE MY NAME, MY NAME IS 石本城.

My Vocabulary List:
点,每天,⼤概,起床,刷⽛,洗脸,洗澡,运动,开车,聊天,吃早饭,吃晚饭,玩⼿机,以前,以后,就,或者,还是,然后,呢,玩,零,分,差,一刻,半,生日,月,号,日,星期,打算,一起,啊,还,但是,完,酒吧,喝酒,可以,因为,为什么,第二天,哈哈,忘,国庆节,年,明年,去年,下个星期,最近,最,近,新,电影,听说,好看,好听,好吃,忙,空,上个月,听,次,以前,以后,真的,请客,可爱,今年,我,我们,你们,老师,你,他,她,您,好,叫,岁,哪,国,⼈,很,也,早上,晚上,什么,名字,⾼兴,认识,不,很好,喜欢,吗,是,英国,德国,法国,⽇本,西班⽛,这,那,书,笔,本⼦,杯⼦,⼿机,电脑,苹果,鸡蛋,⼿,电,脑,鸡,朋友,中文,英文,美国,在,哪⾥,去,家,学校,公司,厕所,商店,商场,饭店,咖啡店,今天,昨天,明天,现在,书店,了,要,没有,睡觉,学习,⼯作,上厕所,买东西,看书,吃饭,喝咖啡,回,来,做,买,东西,看,喝,爸爸,妈妈,哥哥,姐姐,弟弟,妹妹,朋友,男朋友,⼥朋友,有,⼿表,孩⼦,狗,猫,车,钱,谁,的,男,女,个,本,张,台,只,辆,⽀,词典,桌⼦,椅⼦,床,纸,电视,冰箱,上,下,⾥,外,房间,一个苹果,一本书,一张床,一台电脑,一只狗,一辆车,一支笔,几,几个人,三辆车,这只狗,那本书,哪支笔,一共,都,上车,下车,请,谢谢,爱,问题,大,小,口,爷爷,奶奶,外公,外婆,先生,太太,老公,老婆,儿子,女儿,学生,医生,商人,家庭主妇,翻译,职员,律师,工程师,生意,家,和,外国,外国人,外语,大学,中学,小学,读书,多少,想,对不起,请问,包子,饺子,猪肉,牛肉,鱼,虾,贵,给,吧,找,请
```