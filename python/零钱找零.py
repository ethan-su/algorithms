# -*- coding:utf-8 -*-
import copy


def coinChangeCombination(total, values, currentCoins, coinsCombinations):
    """硬币找零所有组合方式
    
    :param total: 要拼凑的数值总额
    :param values: 给定的不同个硬币
    :param currentCoins: 当前硬币组合方式
    :param coinsCombinations: 硬币组合集合
    :return:
    """
    if total == 0:  # 如果总额为0，说明当前组合可以拼凑出给定总额，将当前组合加入总集合
        coinsCombinations.append(currentCoins)
        return
    
    for i in range(len(values)):
        currentValue = values[i]  # 本次使用的硬币
        if currentValue > total:  # 如果本次使用的硬币大于平凑总额，则忽略，选用其他硬币平凑
            continue
        
        newCoins = copy.deepcopy(currentCoins)  # 为了避免python中引用传递的影响，此处需要使用深拷贝。
        newCoins.append(values[i])
        rest = total - currentValue  # 剩余总额
        coinChangeCombination(rest, values, newCoins, coinsCombinations)


def coinChangeMinCount(coinsCombinations):
    """计算组成特定面额需要的最小硬币总数
    
    :param coinsCombinations: 硬币组合集合
    :return:
    """
    minCount = 2 << 255  # 初始化为最大值
    for combination in coinsCombinations:
        minCount = len(combination) if len(combination) < minCount else minCount
    return minCount


if __name__ == "__main__":
    values = [1, 2, 5]
    total = 13
    currentCoins, coinsCombinations = [], []
    coinChangeCombination(total, values, currentCoins, coinsCombinations)
    print coinChangeMinCount(coinsCombinations)
