#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
待办事项管理模块
"""

import json
from datetime import datetime
from src.utils.file_utils import save_json, load_json

class TodoManager:
    def __init__(self):
        """初始化待办事项管理器"""
        self.todos = load_json("todos.json", default=[])
        # 计算下一个ID
        if self.todos:
            self.next_id = max([todo.get("id", 0) for todo in self.todos]) + 1
        else:
            self.next_id = 1
    
    def save(self):
        """保存待办事项到文件"""
        save_json(self.todos, "todos.json")
    
    def add_todo(self, task, priority="中"):
        """添加待办事项"""
        todo = {
            "id": self.next_id,
            "task": task,
            "priority": priority,
            "done": False,
            "created_at": self._get_timestamp()
        }
        self.todos.append(todo)
        self.next_id += 1
        self.save()
        return todo
    
    def complete_todo(self, todo_id):
        """标记待办事项为完成"""
        for todo in self.todos:
            if todo["id"] == todo_id:
                todo["done"] = True
                todo["completed_at"] = self._get_timestamp()
                self.save()
                return True
        return False
    
    def delete_todo(self, todo_id):
        """删除待办事项"""
        self.todos = [todo for todo in self.todos if todo["id"] != todo_id]
        self.save()
    
    def get_todos(self, show_all=True):
        """获取待办事项列表"""
        if show_all:
            return self.todos
        else:
            return [todo for todo in self.todos if not todo["done"]]
    
    def show_menu(self):
        """显示待办事项管理菜单"""
        while True:
            print("\n" + "="*30)
            print("📝 待办事项管理")
            print("="*30)
            print("1. 查看所有待办事项")
            print("2. 查看未完成事项")
            print("3. 添加新事项")
            print("4. 标记为完成")
            print("5. 删除事项")
            print("6. 返回主菜单")
            
            choice = input("请选择 (1-6): ").strip()
            
            if choice == "1":
                self._show_todos(show_all=True)
            elif choice == "2":
                self._show_todos(show_all=False)
            elif choice == "3":
                task = input("请输入任务内容: ").strip()
                if task:
                    self.add_todo(task)
                    print("✅ 任务已添加")
            elif choice == "4":
                todo_id = self._get_todo_id_input()
                if todo_id and self.complete_todo(todo_id):
                    print("✅ 任务标记为完成")
                else:
                    print("❌ 任务ID不存在")
            elif choice == "5":
                todo_id = self._get_todo_id_input()
                if todo_id:
                    self.delete_todo(todo_id)
                    print("✅ 任务已删除")
            elif choice == "6":
                break
    
    def _show_todos(self, show_all=True):
        """显示待办事项列表"""
        todos = self.get_todos(show_all)
        if not todos:
            print("📭 暂无待办事项")
            return
        
        print(f"\n📋 {'所有' if show_all else '未完成'}待办事项:")
        for todo in todos:
            status = "✅" if todo["done"] else "⭕"
            print(f"{status} [{todo['id']}] {todo['task']} (优先级: {todo['priority']})")
    
    def _get_todo_id_input(self):
        """获取用户输入的待办事项ID"""
        try:
            return int(input("请输入任务ID: ").strip())
        except ValueError:
            print("❌ 请输入有效的数字ID")
            return None
    
    def _get_timestamp(self):
        """获取当前时间戳"""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
