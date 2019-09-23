"""
author:wjw
email:975504808@qq.com
create time:2019/09/23 2:03
训练文件，按样式更改下面的数据集就可以训练自己的模型了，模型保存在工程目录下
"""
import utils
import numpy as np

# 数据集
# datas_header长这样
datas_header = ['是否帅', '脾气是否好', '是否高', '是否上进', '结果']
# datas长这样
datas = np.array([['帅', '不好', '矮', '不上进'],
                  ['不帅', '好', '矮', '上进'],
                  ['帅', '好', '矮', '上进'],
                  ['不帅', '爆好', '高', '上进'],
                  ['帅', '不好', '矮', '上进'],
                  ['帅', '不好', '矮', '上进'],
                  ['帅', '好', '高', '不上进'],
                  ['不帅', '好', '中', '上进'],
                  ['帅', '爆好', '中', '上进'],
                  ['不帅', '不好', '高', '上进'],
                  ['帅', '好', '矮', '不上进'],
                  ['帅', '好', '矮', '不上进']])
# labels长这样
labels = np.array(['不嫁', '不嫁', '嫁', '嫁', '不嫁', '不嫁', '嫁', '嫁', '嫁', '嫁', '不嫁', '不嫁'])

# 创建树
tree_model = utils.create_tree(datas_header, datas, labels)
print("决策树构建完成")

# 保存树模型
utils.store_tree(tree_model, '嫁不嫁.pkl')     # .pkl和.txt什么的都可以，但建议.pkl
print("模型保存完毕")