vocabulario = "点,每天,⼤概,起床,刷⽛,洗脸,洗澡,运动,开车,聊天,吃早饭,吃晚饭,玩⼿机,以前,以后,就,或者,还是,然后,呢,玩,零,分,差,一刻,半,生日,月,号,日,星期,打算,一起,啊,还,但是,完,酒吧,喝酒,可以,因为,为什么,第二天,哈哈,忘,国庆节,年,明年,去年,下个星期,最近,最,近,新,电影,听说,好看,好听,好吃,忙,空,上个月,听,次,以前,以后,真的,请客,可爱,今年,我,我们,你们,老师,你,他,她,您,好,叫,岁,哪,国,⼈,很,也,早上,晚上,什么,名字,⾼兴,认识,不,很好,喜欢,吗,是,英国,德国,法国,⽇本,西班⽛,这,那,书,笔,本⼦,杯⼦,⼿机,电脑,苹果,鸡蛋,⼿,电,脑,鸡,朋友,中文,英文,美国,在,哪⾥,去,家,学校,公司,厕所,商店,商场,饭店,咖啡店,今天,昨天,明天,现在,书店,了,要,没有,睡觉,学习,⼯作,上厕所,买东西,看书,吃饭,喝咖啡,回,来,做,买,东西,看,喝,爸爸,妈妈,哥哥,姐姐,弟弟,妹妹,朋友,男朋友,⼥朋友,有,⼿表,孩⼦,狗,猫,车,钱,谁,的,男,女,个,本,张,台,只,辆,⽀,词典,桌⼦,椅⼦,床,纸,电视,冰箱,上,下,⾥,外,房间,一个苹果,一本书,一张床,一台电脑,一只狗,一辆车,一支笔,几,几个人,三辆车,这只狗,那本书,哪支笔,一共,都,上车,下车,请,谢谢,爱,问题,大,小,口,爷爷,奶奶,外公,外婆,先生,太太,老公,老婆,儿子,女儿,学生,医生,商人,家庭主妇,翻译,职员,律师,工程师,生意,家,和,外国,外国人,外语,大学,中学,小学,读书,多少,想,对不起,请问,包子,饺子,猪肉,牛肉,鱼,虾,贵,给,吧,找,请,时间,多长时间,小时,分钟,假期,旅游,坐,飞机,太好了,从,到,用,别,礼物" 

name = "石本城"

lugares = "波特兰, 阿根廷, 危地马拉, 中国"

prompt = """Data:
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
Number each question clearly. All question content must be in Chinese characters only. At end of response include answers to each question.

VOCABULARY RULES (FLEXIBLE):  
- Use ONLY words from Vocabulary List + 4 city names + {nombre}  
- You may add UP TO 3 new words total (not in list) if absolutely necessary for natural flow  
- List these 3 extra words at the very end of your response  
- Goal: Keep 97%+ within provided vocabulary

Output Rules:  
- 100% Chinese characters (except Date/headers)  
- Start: "你好, {nombre}!"
- No English explanations or translations anywhere in the output
"""

def elegir_tema(dia):
    temas = [
        "运动",
        "天气",
        "食物",
        "家庭",
        "爱好",
        "学校/工作",
        "旅行"
    ]
    return temas[dia % len(temas)]

def generar_prompt(fecha, tema):
    return prompt.format(fecha=fecha, tema=tema, nombre=name, lugares=lugares, vocabulario=vocabulario)