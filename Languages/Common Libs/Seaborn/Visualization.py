#%%
# based on matploylib, statistical graphics
# seaborn.pydata.org
#%%
%config ZMQInteractiveShell.ast_node_interactivity='all' 

#%%
# import libs
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
sns.set(style="darkgrid")
# %matplotlib inline
tips = sns.load_dataset("tips")
tips.head()
#%%
# 散点图
sns.relplot(x="total_bill", y="tip", 
            hue="smoker", data=tips) # color
sns.relplot(x="total_bill", y="tip", 
            hue="size", data=tips) # continuous
sns.relplot(x="total_bill", y="tip", 
            style="time", data=tips)# shape
sns.relplot(x="total_bill", y="tip", 
            size="size", sizes=(15,200), # optional
            data=tips)# size
sns.lmplot(x="total_bill", y="tip", data=tips) # linear model
#%%
sns.color_palette("hls", 8)

#%%
df = pd.DataFrame(dict(time=np.arange(500),
                        value=np.random.randn(500).cumsum())) # cumsum = cumulative sum

sns.relplot(x="time", y="value", kind="line", data=df)

#%%
df = pd.DataFrame(np.random.randn(500, 2).cumsum(axis=0), columns=["x", "y"])
sns.relplot(x="x", y="y", 
            sort=False, # optional, default is based on X
            kind="line", data=df)

#%%
# 折线图
fmri = sns.load_dataset("fmri")
fmri.head()
sns.relplot(x="timepoint", y="signal", kind="scatter", data=fmri)
sns.relplot(x="timepoint", y="signal", kind="line", 
            hue="event", style="region",
            data=fmri)
sns.relplot(x="timepoint", y="signal", kind="line", ci=None, data=fmri) # 95% confidence interval
sns.relplot(x="timepoint", y="signal", kind="line", ci="sd", data=fmri) # standard deviation
sns.relplot(x="timepoint", y="signal", kind="line", estimator=None, data=fmri) # just link each node

#%%
# 分类数据的可视化分析
# 分类散点图
sns.catplot(data=tips, x="day", y="total_bill",
            jitter=True # True(default): data swing, False: data in one y line same as relplot
            )

#%%
sns.catplot(data=tips, x="day", y="total_bill",
            kind="swarm",
            hue="sex"
            )
sns.catplot(data=tips, x="size", y="total_bill",
            kind="swarm"
            )
sns.catplot(data=tips, x="smoker", y="total_bill",
            kind="swarm", order=["No", "Yes"]
            )
sns.catplot(data=tips, x="total_bill", y="smoker",
            kind="swarm", order=["No", "Yes"]
            )

#%%
# 箱线图 分析异常点
# IQR = Q3 - Q1
# 1.5 * IQR
sns.catplot(data=tips, x="day", y="total_bill",
            kind="box"
            )

#%%
tips["weekend"] = tips["day"].isin(["Sat", "Sun"])
sns.catplot(data=tips, x="day", y="total_bill",
            kind="box",
            hue="weekend",
            dodge=False, # True(default): split dataset with space
            )

#%%
# boxen图
diamonds = sns.load_dataset("diamonds")
diamonds.head()
sns.catplot(x="color", y="price", 
            kind="boxen",
            data=diamonds.sort_values("color"))
sns.catplot(x="color", y="price", 
            kind="boxen", hue="cut",
            data=diamonds.sort_values("color"))

#%%
# 提琴图 boxplot + KDE
sns.catplot(x="total_bill", y="day", 
            hue="time",
            data=tips)
# problem in above figure: 
sns.catplot(x="day", y="total_bill", 
            hue="sex",
            kind="violin",
            data=tips)
# above: height means histagram, 

#%%
# merge two kinds of plot together in one ax
g = sns.catplot(x="day", y="total_bill",
            kind="violin", data=tips)

sns.catplot(x="day", y="total_bill", 
            color="k", data=tips,
            size=3, kind="swarm",
            ax=g.ax)

#%%
# 条形图
titanic = sns.load_dataset("titanic")
titanic.head()
sns.catplot(x="sex", y="survived", hue="class",
            kind="bar", data=titanic)

#%%
# distribution
# 灰度图
x = np.random.normal(size=100) # returns a list of gauss distributed values
sns.distplot(x) # default is kde=True, parameter using ndarray or list
sns.distplot(x, kde=False, bins=20) # default bins is 10
# probability density ( 积分 = 1 )
# probability mass ( sum = 1 )
sns.distplot(x, kde=True, bins=20, rug=True)

#%%
# 核密度估计 kernel density estimation
# 样本的正态分布合体后归一化
# bandwidth：用于近似的正态分布曲线的宽度
sns.kdeplot(x, label="raw")
sns.kdeplot(x, bw=0.2, label="bw: 0.2") # default bw is scott
sns.kdeplot(x, bw=2, label="bw: 2")
plt.legend()

#%%
# 双变量分布
mean, cov = [0,1], [(1, .5), (.5, 1)] # 平均数与协方差for 二维
data = np.random.multivariate_normal(mean, cov, 200)
df = pd.DataFrame(data, columns=["x", "y"])

# 散点图
sns.jointplot(x="x", y="y", data=df)

# 六角箱图
sns.jointplot(x="x", y="y", data=df, kind="hex")

# kde (等高线图+二维kde)
sns.jointplot(x="x", y="y", data=df, kind="kde")
f, ax = plt.subplots()
cmap = sns.cubehelix_palette(as_cmap=True, dark=1, light=0)
sns.kdeplot(df.x, df.y, cmap=cmap, n_levels=60, shade=True)
sns.rugplot(df.x, color="green", ax=ax)
sns.rugplot(df.y, color="blue", vertical=True, ax=ax)

#%%
# 数据两两关系
iris = sns.load_dataset("iris")
iris.corr()
sns.pairplot(iris,
            hue="species")

#%%
# 线性回归模型
sns.lmplot(data=tips, x="total_bill", y="tip")
sns.lmplot(data=tips, x="size", y="tip", x_estimator=np.mean, ci=50)

#%%
# 拟合不同模型
anscombe = sns.load_dataset("anscombe")
anscombe.query("dataset =='I'")

sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'II'"), 
            order=2,
            ci=None, scatter_kws={"s": 80})
# deal with abnormal value
sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'III'"), 
            robust=True,
            ci=None, scatter_kws={"s": 200})

#%%
# 二值变量拟合
# tips["big_tips"]

#%%
# 评价拟合效果
sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'I'"), 
            ci=None, scatter_kws={"s": 80})
sns.residplot(x="x", y="y", data=anscombe.query("dataset == 'I'"), 
            ci=None, scatter_kws={"s": 80})

#%%
# 变量间条件关系摸索
sns.lmplot(x="total_bill", y="tip", data=tips, 
            hue="day")
sns.lmplot(x="total_bill", y="tip", data=tips, 
            col="time", row="sex",
            hue="smoker",
            height=20, # control image size
            aspect=0.4 # control image layout
            # size=??
            )

