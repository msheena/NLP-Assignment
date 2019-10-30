# 2.1 What conditions are required to make the BFS return the optimal solution ?
# A:
#     1.每两个节点直接的花费一样且非负
#     2.维护搜索历史的列表在每次迭代中排序


# 2.2 Is there a way to make DFS find the optimal solution ? (You may need to read some material about iterative DFS)
# A:
# 1.动态规划法
# 2.把原输出过程的地方改为记录过程，即记录达到当前目标的路径和相应的路程值，并与前面已记录的值进行比较，保留其中最优的，等全部搜索完成后，才把保留的最优解输出


# 2.3 In what conditions BFS is a better choice than DFS and vice versa ?
# A:
# 1.当需要搜索最短路径时，适合用BFS，因为BFS搜索过程中遇到的解一定是离根最近的，是最优解，此时搜索算法可以终止；而DFS需要全局搜索
# 2.内存较小时，搜索全部解，适合用DFS，因为DFS不用记录过多信息


# 2.4 When can we use machine learning ?
# A:
# 无法根据简单规则进行人力编码且数据规模较大时需要用机器学习，比如物联网，聊天机器人，自动驾驶等


# 2.5 What is the gradient of a function ?
# A:
# 函数在此方向上变化最快，变化率最大

# 2.6 How can we find the maximum value of a function using the information of gradient ?
# A:
# 可以对原函数取负值