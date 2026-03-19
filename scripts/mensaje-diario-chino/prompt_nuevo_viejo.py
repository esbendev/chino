vocabulario = "点,每天,⼤概,起床,刷⽛,洗脸,洗澡,运动,开车,聊天,吃早饭,吃晚饭,玩⼿机,以前,以后,就,或者,还是,然后,呢,玩,零,分,差,一刻,半,生日,月,号,日,星期,打算,一起,啊,还,但是,完,酒吧,喝酒,可以,因为,为什么,第二天,哈哈,忘,国庆节,年,明年,去年,下个星期,最近,最,近,新,电影,听说,好看,好听,好吃,忙,空,上个月,听,次,以前,以后,真的,请客,可爱,今年,我,我们,你们,老师,你,他,她,您,好,叫,岁,哪,国,⼈,很,也,早上,晚上,什么,名字,⾼兴,认识,不,很好,喜欢,吗,是,英国,德国,法国,⽇本,西班⽛,这,那,书,笔,本⼦,杯⼦,⼿机,电脑,苹果,鸡蛋,⼿,电,脑,鸡,朋友,中文,英文,美国,在,哪⾥,去,家,学校,公司,厕所,商店,商场,饭店,咖啡店,今天,昨天,明天,现在,书店,了,要,没有,睡觉,学习,⼯作,上厕所,买东西,看书,吃饭,喝咖啡,回,来,做,买,东西,看,喝,爸爸,妈妈,哥哥,姐姐,弟弟,妹妹,朋友,男朋友,⼥朋友,有,⼿表,孩⼦,狗,猫,车,钱,谁,的,男,女,个,本,张,台,只,辆,⽀,词典,桌⼦,椅⼦,床,纸,电视,冰箱,上,下,⾥,外,房间,一个苹果,一本书,一张床,一台电脑,一只狗,一辆车,一支笔,几,几个人,三辆车,这只狗,那本书,哪支笔,一共,都,上车,下车,请,谢谢,爱,问题,大,小,口,爷爷,奶奶,外公,外婆,先生,太太,老公,老婆,儿子,女儿,学生,医生,商人,家庭主妇,翻译,职员,律师,工程师,生意,家,和,外国,外国人,外语,大学,中学,小学,读书,多少,想,对不起,请问,包子,饺子,猪肉,牛肉,鱼,虾,贵,给,吧,找,请,时间,多长时间,小时,分钟,假期,旅游,坐,飞机,太好了,从,到,用,别,礼物,怎么样,好玩,非常,再,城市,只,多,少,比较,菜,又。。。又。。。,酸,甜,苦,辣,对了,象,字,怎么,常常,自己,写,教,练习,口语,网,网站,一样,母语者,介绍,视频,那,等一下,发,邮件,长城,怎么了,虽然,过,出,租,出租车,打的,先,地铁,行,打折,假,学生证,淘宝" 

name = "石本城"

prompt = """You are an assistant that simplifies and rewrites English text into Chinese using a restricted vocabulary.

Hard constraints:
1) You MUST start with a greeting that includes the user's name, exactly like: "Hi {name},"
2) Output language MUST be Chinese (after the greeting).
3) You MUST use ONLY the words/terms found in the Allowed vocabulary list below (match by exact tokens/entries as best as possible).
   - You may also use: Chinese punctuation (，。；：？！、（）「」『』《》—…).
   - You may use Arabic numerals (0-9) and dates.
   - For words not in the allowed vocabulary, include the pinyin and meaning in parentheses (e.g., 不可思议 (bù kě sī yì, incredible)).
4) If a required concept cannot be expressed using the allowed vocabulary, replace it with English (do not invent).
5) Do not add facts that are not in the source text.
6) Output exactly TWO paragraphs total (the greeting + the rewritten Chinese text all in one paragraph).
7) Return ONLY the final paragraphs. No title, no bullets, no explanations.
8) If the source text contains errors (e.g., typos, grammatical mistakes, or non-Chinese characters), preserve them as is without correction.
9) For synonyms or near-synonyms within the allowed vocabulary, choose the most common or contextually appropriate term.
10) Limit the rewritten text to a maximum of 200 characters (excluding the greeting).

Date: {fecha}

Allowed vocabulary (Chinese):
{vocabulario}

Source text (English):
{articulo}

Example inputs and outputs:
Input:
Date: 2026-03-04
Source text: "Today is a special day, we are celebrating."

Output:
Hi 石本城,
今天是一个特别的日子 (rì zi, day)，我们要庆祝 (qìng zhù, celebrate)。
"""

def generar_prompt_nuevo(fecha, articulo):
    articulo_safe = articulo.replace("{", "{{").replace("}", "}}").replace("(", "（").replace(")", "）")
    return prompt.format(
        fecha=fecha,
        articulo=articulo_safe,
        name=name,
        vocabulario=vocabulario
    )
