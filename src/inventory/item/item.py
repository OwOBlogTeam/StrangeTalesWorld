'''
       _____   _          __  _____   _____   _       _____   _____
     /  _  \ | |        / / /  _  \ |  _  \ | |     /  _  \ /  ___|
     | | | | | |  __   / /  | | | | | |_| | | |     | | | | | |
     | | | | | | /  | / /   | | | | |  _  { | |     | | | | | |   _
     | |_| | | |/   |/ /    | |_| | | |_| | | |___  | |_| | | |_| |
     \_____/ |___/|___/     \_____/ |_____/ |_____| \_____/ \_____/

Copyright (c) 2023 by OwOTeam-DGMT (OwOBlog).
Date         : 2024-07-23 15:12:40
Author       : HanskiJay
LastEditors  : HanskiJay
LastEditTime : 2024-07-23 19:05:39
E-Mail       : support@owoblog.com
Telegram     : https://t.me/HanskiJay
GitHub       : https://github.com/Tommy131
'''
# item.py

class Item:
    DURABILITY = 1

    def __init__(self, item_id, name, description='no description', main_image=None, quantity=1, durability=DURABILITY):
        """
        初始化物品

        :param item_id: 物品ID
        :param name: 物品名称
        :param description: 物品描述
        :param quantity: 物品数量, defaults to 1
        :param durability: 耐久性, defaults to DURABILITY
        """
        self.id = item_id
        self.name = name
        self.description = description
        self.main_image = main_image
        self.quantity = quantity
        self.durability = durability
        self.equipped = False

    def __len__(self):
        """
        返回物品数量

        :return: int
        """
        return self.quantity

    def is_equipped(self):
        """
        返回当前物品装备状态

        :return: bool
        """
        return self.equipped == True

    def update(self, quantity=0, durability=0):
        """
        更新物品的数量和耐久性

        :param quantity: 要增加的数量
        :param durability: 要增加的耐久性
        """
        self.quantity += quantity
        self.durability = min(self.durability + durability, Item.DURABILITY)

    def remove_quantity(self, quantity):
        """
        移除指定数量的物品

        :param quantity: 要移除的数量
        """
        if quantity >= self.quantity:
            self.quantity = 0
        else:
            self.quantity -= quantity

    def __repr__(self):
        return f'Item(id={self.id}, name={self.name}, description={self.description}, quantity={self.quantity})'

    def use(self, quantity=1):
        """
        使用物品

        :param entity: 实体
        :param quantity: 数量, defaults to 1
        """
        # 省略执行逻辑, 因物品不同所需执行的代码不同

        self.remove_quantity(quantity)
        return True