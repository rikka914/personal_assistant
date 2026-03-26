#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
学习笔记管理模块
"""

from datetime import datetime
from src.utils.file_utils import save_json, load_json

class NoteManager:
    def __init__(self):
        """初始化笔记管理器"""
        self.notes = load_json("notes.json", default=[])
        # 计算下一个ID
        if self.notes:
            self.next_id = max([note.get("id", 0) for note in self.notes]) + 1
        else:
            self.next_id = 1
    
    def save(self):
        """保存笔记到文件"""
        save_json(self.notes, "notes.json")
    
    def add_note(self, title, content, category="学习"):
        """添加新笔记"""
        note = {
            "id": self.next_id,
            "title": title,
            "content": content,
            "category": category,
            "created_at": self._get_timestamp(),
            "updated_at": self._get_timestamp()
        }
        self.notes.append(note)
        self.next_id += 1
        self.save()
        return note
    
    def edit_note(self, note_id, title=None, content=None, category=None):
        """编辑笔记"""
        for note in self.notes:
            if note["id"] == note_id:
                if title:
                    note["title"] = title
                if content:
                    note["content"] = content
                if category:
                    note["category"] = category
                note["updated_at"] = self._get_timestamp()
                self.save()
                return True
        return False
    
    def delete_note(self, note_id):
        """删除笔记"""
        self.notes = [note for note in self.notes if note["id"] != note_id]
        self.save()
    
    def search_notes(self, keyword):
        """搜索笔记（标题或内容）"""
        keyword_lower = keyword.lower()
        results = []
        for note in self.notes:
            if (keyword_lower in note["title"].lower() or 
                keyword_lower in note["content"].lower() or
                keyword_lower in note["category"].lower()):
                results.append(note)
        return results
    
    def get_notes_by_category(self, category):
        """按分类获取笔记"""
        return [note for note in self.notes if note["category"] == category]
    
    def show_menu(self):
        """显示笔记管理菜单"""
        while True:
            print("\n" + "="*30)
            print("📒 学习笔记管理")
            print("="*30)
            print("1. 查看所有笔记")
            print("2. 按分类查看")
            print("3. 搜索笔记")
            print("4. 添加新笔记")
            print("5. 编辑笔记")
            print("6. 删除笔记")
            print("7. 返回主菜单")
            
            choice = input("请选择 (1-7): ").strip()
            
            if choice == "1":
                self._show_notes(self.notes)
            elif choice == "2":
                category = input("请输入分类名称: ").strip()
                notes = self.get_notes_by_category(category)
                self._show_notes(notes)
            elif choice == "3":
                keyword = input("请输入搜索关键词: ").strip()
                notes = self.search_notes(keyword)
                self._show_notes(notes)
            elif choice == "4":
                title = input("请输入笔记标题: ").strip()
                content = input("请输入笔记内容: ").strip()
                category = input("请输入分类（默认: 学习）: ").strip() or "学习"
                if title and content:
                    self.add_note(title, content, category)
                    print("✅ 笔记已添加")
            elif choice == "5":
                self._edit_note_ui()
            elif choice == "6":
                self._delete_note_ui()
            elif choice == "7":
                break
    
    def _show_notes(self, notes):
        """显示笔记列表"""
        if not notes:
            print("📭 暂无笔记")
            return
        
        print(f"\n📋 找到 {len(notes)} 条笔记:")
        for note in notes:
            print(f"\n[{note['id']}] {note['title']}")
            print(f"   分类: {note['category']}")
            print(f"   创建: {note['created_at']}")
            if len(note['content']) > 50:
                print(f"   内容: {note['content'][:50]}...")
            else:
                print(f"   内容: {note['content']}")
    
    def _edit_note_ui(self):
        """编辑笔记用户界面"""
        note_id = self._get_note_id_input()
        if not note_id:
            return
        
        note = next((n for n in self.notes if n["id"] == note_id), None)
        if not note:
            print("❌ 笔记ID不存在")
            return
        
        print(f"\n当前标题: {note['title']}")
        new_title = input("新标题（直接回车保持原样）: ").strip()
        
        print(f"\n当前内容: {note['content']}")
        new_content = input("新内容（直接回车保持原样）: ").strip()
        
        print(f"\n当前分类: {note['category']}")
        new_category = input("新分类（直接回车保持原样）: ").strip()
        
        # 只更新用户输入的内容
        title = new_title if new_title else None
        content = new_content if new_content else None
        category = new_category if new_category else None
        
        if any([title, content, category]):
            self.edit_note(note_id, title, content, category)
            print("✅ 笔记已更新")
        else:
            print("ℹ️  没有修改任何内容")
    
    def _delete_note_ui(self):
        """删除笔记用户界面"""
        note_id = self._get_note_id_input()
        if note_id:
            self.delete_note(note_id)
            print("✅ 笔记已删除")
    
    def _get_note_id_input(self):
        """获取用户输入的笔记ID"""
        try:
            return int(input("请输入笔记ID: ").strip())
        except ValueError:
            print("❌ 请输入有效的数字ID")
            return None
    
    def _get_timestamp(self):
        """获取当前时间戳"""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
