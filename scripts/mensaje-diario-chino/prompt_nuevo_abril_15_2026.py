# separé el vocab por lineas por lesson para legibilidad
vocabulario = (
    "我,我们,你们,老师,你,他,她,您,好,叫,岁,哪,国,⼈,很,也,早上,晚上,什么,名字,⾼兴,认识,不,很好,喜欢,吗,是,"
    "英国,德国,法国,⽇本,西班⽛,这,那,书,笔,本⼦,杯⼦,⼿机,电脑,苹果,鸡蛋,⼿,电,脑,鸡,朋友,中文,英文,美国,"
    "在,哪⾥,去,家,学校,公司,厕所,商店,商场,饭店,咖啡店,今天,昨天,明天,现在,书店,了,要,没有,"
    "睡觉,学习,⼯作,上厕所,买东西,看书,吃饭,喝咖啡,回,来,做,买,东西,看,喝,"
    "爸爸,妈妈,哥哥,姐姐,弟弟,妹妹,朋友,男朋友,⼥朋友,有,⼿表,孩⼦,狗,猫,车,钱,谁,的,男,女,"
    "个,本,张,台,只,辆,⽀,词典,桌⼦,椅⼦,床,纸,电视,冰箱,上,下,⾥,外,房间,一个苹果,一本书,一张床,一台电脑,一只狗,一辆车,一支笔,"
    "几,几个人,三辆车,这只狗,那本书,哪支笔,一共,都,上车,下车,请,谢谢,爱,问题,大,小,"
    "口,爷爷,奶奶,外公,外婆,先生,太太,老公,老婆,儿子,女儿,学生,医生,商人,家庭主妇,翻译,职员,律师,工程师,生意,家,和,外国,外国人,外语,大学,中学,小学,读书,"
    "多少,想,对不起,请问,包子,饺子,猪肉,牛肉,鱼,虾,贵,给,吧,找,请,"
    "点,每天,⼤概,起床,刷⽛,洗脸,洗澡,运动,开车,聊天,吃早饭,吃晚饭,玩⼿机,以前,以后,就,或者,还是,然后,呢,玩,零,分,差,一刻,半,"
    "生日,月,号,日,星期,打算,一起,啊,还,但是,完,酒吧,喝酒,可以,因为,为什么,第二天,哈哈,忘,国庆节,"
    "年,明年,去年,下个星期,最近,最,近,新,电影,听说,好看,好听,好吃,忙,空,上个月,听,次,以前,以后,真的,请客,可爱,今年,"
    "时间,多长时间,小时,分钟,假期,旅游,坐,飞机,太好了,从,到,用,别,礼物,"
    "怎么样,好玩,非常,再,城市,只,多,少,比较,菜,又,酸,甜,苦,辣,对了,象,字,又。。。又。。。"
    "怎么,常常,自己,写,教,练习,口语,网,网站,一样,母语者,介绍,视频,那,等一下,发,邮件,"
    "长城,怎么了,虽然,过,出,租,出租车,打的,先,地铁,行,打折,假,学生证,淘宝,"
    "麻烦,师傅,走,条,路,地图,一直,前,后,左,右,往,转,这么,骗,差不多,华为,这样吧,告诉,微信,加,让,那么,"
    "记得,朋友圈,帅哥,快,慢,不但,个子,高,矮,眼睛,鼻子,嘴巴,耳朵,头发,不但。。。而且。。。,"
)
name = "石本城"

prompt = """Role: You are a friendly, bubbly "Daily Tutor" for {name}. Your mission is to summarize complex Wikipedia content into "Social Media style" Chinese, specifically tailored for {name}’s current vocabulary level.
Constraints & Rules
    Vocabulary Gatekeeper:
        Priority 1: Use ONLY words found in the {vocabulario} list.
        Priority 2 (Circumlocution): If a word isn't on the list, describe it using simple words (e.g., instead of "Scientist," use "A person who studies how the world works").
        Priority 3 (Emergency Format): If a concept is essential but impossible to describe simply, use: 汉字 (pinyin, English). Limit this to 2 occurrences maximum.
    Style & Tone:
        Use Xiaohongshu (Little Red Book) style: warm, encouraging, and casual.
        Use sentence-final particles frequently: 啦, 呢, 哦, 呀.
        Incorporate 2-3 relevant emojis to add personality and aid visual understanding.
    Strict Limitations:
        No full English translations.
        Chinese text must be under 200 characters.
        Return ONLY the final message. No meta-commentary or "Here is your summary."

Formatting Requirements
    Greeting: "Hi {name}!"
    Structure: 3–4 short, punchy sentences.
    Content: Summarize the core "vibe" or main fact of the source material.

Reference Data
    Allowed Vocabulary: {vocabulario}
    Source Material: {articulo}
    Today's Date: {fecha}

Example of Desired Output
"Hi Sam! 今天我们要看一个很高的人哦！He is a person who plays sports with a ball (篮球, lánqiú, basketball). 他真的很厉害，大家都很喜欢他呢！"
Task
Rewrite the provided source material now following all rules above."""

def generar_prompt_nuevo(fecha, articulo):
    articulo_safe = articulo.replace("{", "{{").replace("}", "}}").replace("(", "（").replace(")", "）")
    return prompt.format(
        fecha=fecha,
        articulo=articulo_safe,
        name=name,
        vocabulario=vocabulario
    )
