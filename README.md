# 说点什么
这是一个使用python语言编写的SQL代码格式化工具。制作原因：本人喜欢写写SQL代码，尤其是做力扣题目的时候，但不用专门的软件编写没有快速格式化功能，手动调整觉得麻烦，就写了一个小小的程序，并添加了GUI界面方便使用。  
  
## 核心功能代码：  
formatted = sqlparse.format(  
&nbsp;&nbsp;&nbsp;&nbsp;raw_sql,  
&nbsp;&nbsp;&nbsp;&nbsp;reindent=True,          # 重新缩进  
&nbsp;&nbsp;&nbsp;&nbsp;indent_width=2,         # 缩进2个空格  
&nbsp;&nbsp;&nbsp;&nbsp;keyword_case='upper'    # 关键字转大写  
)  
  
## 依赖库：  
pip install sqlparse pyperclip  
  
图片示例1：  
<img width="602" height="832" alt="1" src="https://github.com/user-attachments/assets/98a8e3c3-9265-43c6-becc-b4f14138b0ad" />  
图片示例2：  
<img width="602" height="832" alt="2" src="https://github.com/user-attachments/assets/43ab6ebe-0d07-45fe-befd-c10345d10be4" />  
  
# 许可证
MIT
