                    # 选择器
# 1、CSS元素选择器
#   直接选取文档元素
#   如：head、p

# 2、类选择器
#     元素的class属性，如<h1 class="improtant">
#     类名就是important
#     .important选择所有有这个类属性的元素
#     可以结合元素选择器，比如p.important

# 3、ID选择器
#     1、元素id属性，如：<h1 id="intro">
#         id就是important
#         #intro用于选择id=intro的元素
#     2、可以结合元素选择器，比如p.#intro
#     3、与类选择器异同
#         ID文档只能出现一次
#         ID选择器不能使用单次列表
#         与类选择去一样，都区分大小写

# 4、属性选择器
#     选择某个属性的元素，而不论值是什么，如：<p title='dsada'>
#     *[title]选择所有包含title属性的元素
#     a[href]选择所有带href属性的锚元素,如：<a href="qqq">
#     还可以选择多个属性，如：a[href][title]，注意这里要同时满足(and),如：如：<a href="qqq", title='dsad'>
#     限定值：a[href='www.SO.com']

# 5、后代选择器
#     选择某元素后代的元素（层级不收限制）
#     选择h1元素的em元素：h1 em,所有em都能找到
# <h1>
#     <em>...</em>
#     <body>
#         <em>...</em>
#     </body>
# </h1>

# 6、子元素选择器
#     范围限制在子元素
#     选择h1元素的子元素strong:    h1 >strong

