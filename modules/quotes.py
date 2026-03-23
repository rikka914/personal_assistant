#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
励志名言管理模块
"""

import random
from src.utils.file_utils import save_json, load_json

class QuoteManager:
    def __init__(self):
        """初始化名言管理器"""
        self.quotes = load_json("quotes.json", default=self._get_default_quotes())
        # 计算下一个ID
        if self.quotes:
            self.next_id = max([quote.get("id", 0) for quote in self.quotes]) + 1
        else:
            self.next_id = 1
    
    def save(self):
        """保存名言到文件"""
        save_json(self.quotes, "quotes.json")
    
    def add_quote(self, text, author="未知"):
        """添加新名言"""
        quote = {
            "id": self.next_id,
            "text": text,
            "author": author,
            "favorite": False
        }
        self.quotes.append(quote)
        self.next_id += 1
        self.save()
        return quote
    
    def get_random_quote(self):
        """获取随机名言"""
        if not self.quotes:
            return {"text": "今天也是充满希望的一天！", "author": "小爱"}
        return random.choice(self.quotes)
    
    def toggle_favorite(self, quote_id):
        """切换收藏状态"""
        for quote in self.quotes:
            if quote["id"] == quote_id:
                quote["favorite"] = not quote["favorite"]
                self.save()
                return True
        return False
    
    def get_favorites(self):
        """获取收藏的名言"""
        return [quote for quote in self.quotes if quote["favorite"]]
    
    def search_quotes(self, keyword):
        """搜索名言"""
        keyword_lower = keyword.lower()
        results = []
        for quote in self.quotes:
            if (keyword_lower in quote["text"].lower() or 
                keyword_lower in quote["author"].lower()):
                results.append(quote)
        return results
    
    def show_quote(self):
        """显示随机名言"""
        quote = self.get_random_quote()
        print("\n" + "💪" * 20)
        print(f"   {quote['text']}")
        print(f"\n   —— {quote['author']}")
        print("💪" * 20)
        
        # 询问是否收藏
        if not quote.get('favorite', False):
            choice = input("\n❤️  收藏这条名言吗？(y/n): ").strip().lower()
            if choice == 'y':
                self.toggle_favorite(quote['id'])
                print("✅ 已收藏！")
    
    def show_menu(self):
        """显示名言管理菜单"""
        while True:
            print("\n" + "="*30)
            print("💪 励志名言管理")
            print("="*30)
            print("1. 随机鼓励")
            print("2. 查看收藏")
            print("3. 搜索名言")
            print("4. 添加名言")
            print("5. 管理收藏")
            print("6. 返回主菜单")
            
            choice = input("请选择 (1-6): ").strip()
            
            if choice == "1":
                self.show_quote()
            elif choice == "2":
                favorites = self.get_favorites()
                self._show_quotes(favorites, "收藏的名言")
            elif choice == "3":
                keyword = input("请输入搜索关键词: ").strip()
                quotes = self.search_quotes(keyword)
                self._show_quotes(quotes, f"搜索 '{keyword}' 的结果")
            elif choice == "4":
                self._add_quote_ui()
            elif choice == "5":
                self._manage_favorites_ui()
            elif choice == "6":
                break
    
    def _show_quotes(self, quotes, title):
        """显示名言列表"""
        if not quotes:
            print(f"📭 {title}为空")
            return
        
        print(f"\n📋 {title} ({len(quotes)}条):")
        for quote in quotes:
            favorite = "❤️" if quote.get('favorite', False) else "🤍"
            print(f"\n{favorite} [{quote['id']}] {quote['text']}")
            print(f"   —— {quote['author']}")
    
    def _add_quote_ui(self):
        """添加名言用户界面"""
        text = input("请输入名言内容: ").strip()
        if not text:
            print("❌ 名言内容不能为空")
            return
        
        author = input("请输入作者（可选）: ").strip() or "未知"
        self.add_quote(text, author)
        print("✅ 名言已添加")
    
    def _manage_favorites_ui(self):
        """管理收藏用户界面"""
        while True:
            favorites = self.get_favorites()
            self._show_quotes(favorites, "收藏的名言")
            
            if not favorites:
                break
            
            print("\n1. 取消收藏某条名言")
            print("2. 返回上一级")
            
            choice = input("请选择 (1-2): ").strip()
            
            if choice == "1":
                try:
                    quote_id = int(input("请输入要取消收藏的名言ID: ").strip())
                    if self.toggle_favorite(quote_id):
                        print("✅ 已取消收藏")
                    else:
                        print("❌ 名言ID不存在")
                except ValueError:
                    print("❌ 请输入有效的数字ID")
            elif choice == "2":
                break
    
    def _get_default_quotes(self):
        """获取默认名言库"""
        return [
            {
                "id": 1,
                "text": "代码写得好不好，调试的时候才知道。",
                "author": "程序员真理",
                "favorite": True
            },
            {
                "id": 2, 
                "text": "学习如逆水行舟，不进则退。",
                "author": "《增广贤文》",
                "favorite": False
            },
            {
                "id": 3,
                "text": "成功不是将来才有的，而是从决定去做的那一刻起，持续累积而成。",
                "author": "佚名",
                "favorite": False
            },
            {
                "id": 4,
                "text": "今天最好的表现，是明天最低的要求。",
                "author": "阿里巴巴",
                "favorite": True
            },
            {
                "id": 5,
                "text": "编程不只是写代码，更是解决问题的艺术。",
                "author": "Rika",
                "favorite": True
            }
        ]
