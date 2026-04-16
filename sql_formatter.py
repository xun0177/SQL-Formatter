import tkinter as tk
import sqlparse
import pyperclip

def format_sql_text():
    raw_sql = input_text.get("1.0", tk.END).strip()
    if not raw_sql:
        status_label.config(text="请先输入原代码", fg="red")
        return

    try:
        formatted = sqlparse.format(
            raw_sql,
            reindent=True,
            indent_width=2,
            keyword_case='upper'
        )
        output_text.delete("1.0", tk.END)
        output_text.insert("1.0", formatted)
        pyperclip.copy(formatted)
        status_label.config(text="结果已复制到剪贴板，可直接粘贴使用", fg="green")
    except Exception as e:
        status_label.config(text=f"格式化失败：{e}", fg="red")

root = tk.Tk()
root.title("SQL 格式化工具")
root.geometry("600x800")

font_settings = ("Consolas", 12)

tk.Label(root, text="原代码：").pack(anchor="w", padx=10, pady=(10, 0))
input_text = tk.Text(root, height=12, font=font_settings)
input_text.pack(fill="x", padx=10, pady=5)

tk.Button(root, text="格式化并复制", command=format_sql_text).pack(pady=5)

tk.Label(root, text="格式化结果：").pack(anchor="w", padx=10, pady=(5, 0))
output_text = tk.Text(root, height=12, font=font_settings)
output_text.pack(fill="both", expand=True, padx=10, pady=5)

status_label = tk.Label(root, text="", fg="gray")
status_label.pack(pady=5)

root.mainloop()