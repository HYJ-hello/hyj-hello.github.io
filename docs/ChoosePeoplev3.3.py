from tkinter import  *
from  tkinter import  messagebox
import  random
import  tkinter as tk


root = Tk()
root.title("抽人V3.3")
#列表
'''
group1 = ['冉城驿','黄俊霖','李金泽','吴睿淇','秦紫轩','于彦若','曾锐涵']
group2 = ['张露桐','杨媛婷','李思齐','李姿乐','姚博凯','文耀杰','侯妍西']
group3 = ['刁钰函','罗海纳','周子潇','李鸿成','蔡泽轩','王瑞','王翌潘']
group4 = ['殷嘉悦','沈渝轩','唐玮翎','周妍怡','周俊池','雷智瑀','刘靖琪']
group5 = ['何宇京','余宥歆','胡宸嘉','何文一','冯乙朗','何贞辰']
group6 = ['刘芷彤','敖小童', '惠盈溪','陈欣亦','何浩宇','李林翰','孔舒奇']
group7 = ['袁显虹','王奕欢','何悦月','刘恒睿','吴清怡','况贝迪','冉汶沁']
group8 = ['唐梓淳','童韵润','陈骏娇','胡棚','覃芮琳','王颢霖']
teacher = ['Miss Huang']
xuanname = [group1*7, group2*7,group3*7, group4*7,group5*6, group6*7 , group7*7 ,group8*6,teacher*5]
xuanname = random.choice(xuanname)
zj = random.choice(xuanname)
'''
# 初始化名单（建议改为元组防止意外修改）
GROUPS = (
    ['冉城驿','黄俊霖','李金泽','吴睿淇','秦紫轩','于彦若','曾锐涵'] * 7,
    ['张露桐','杨媛婷','李思齐','李姿乐','姚博凯','文耀杰','侯妍西'] * 7,
    ['刁钰函','罗海纳','周子潇','李鸿成','蔡泽轩','王瑞','王翌潘']*7,
    ['殷嘉悦','沈渝轩','唐玮翎','周妍怡','周俊池','雷智瑀','刘靖琪']*7,
    ['何宇京','余宥歆','胡宸嘉','何文一','冯乙朗','何贞辰']*5,
    ['刘芷彤','敖小童', '惠盈溪','陈欣亦','何浩宇','李林翰','孔舒奇']*7,
    ['袁显虹','王奕欢','何悦月','刘恒睿','吴清怡','况贝迪','冉汶沁']*7,
    ['唐梓淳','童韵润','陈骏娇','胡棚','覃芮琳','王颢霖']*6,
    ['Miss Huang'] * 1
)
'''
# 创建带验证的输入框
def validate_input(new_text):
    return new_text.isdigit() or new_text == ""

entry = Entry(root, width=30, validate="key",
            validatecommand=(root.register(validate_input), '%P'))
entry.pack(pady=10)

entry.insert(0, "请输入抽人次数")  # 插入默认提示
entry.config(fg='grey')           # 设置灰色文字
'''


# 创建带提示的输入框
def create_entry_with_hint():
    def on_focus_in(event):
        if entry.get() == "请输入抽人次数":
            entry.delete(0, END)
            entry.config(fg='black')  # 正常文字颜色

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, "请输入抽人次数")
            entry.config(fg='grey')  # 提示文字颜色

    # 输入验证函数（只允许数字或空）
    def validate_input(new_text):
        return new_text.isdigit() or new_text == ""

    # 创建输入框
    entry = Entry(root,
                  width=30,
                  validate="key",
                  validatecommand=(root.register(validate_input), '%P'),
                  fg='grey'  # 初始文字颜色设为灰色
                  )
    entry.pack(pady=10)

    # 插入提示文本
    entry.insert(0, "请输入抽人次数")

    # 绑定焦点事件
    entry.bind('<FocusIn>', on_focus_in)
    entry.bind('<FocusOut>', on_focus_out)

    return entry


# 创建带提示的输入框
entry = create_entry_with_hint()

#抽人按钮
btn01 = Button(root)
btn01["text"] = "抽人"
btn01.pack()
'''
def chosiename(e):
    global  xuanname
    global  zj
    xuanname = [group1 * 7, group2 * 7, group3 * 7, group4 * 7, group5 * 6, group6 * 7, group7 * 7, group8 * 6,teacher * 5]
    xuanname = random.choice(xuanname)
    zj = random.choice(xuanname)
    messagebox.showinfo("抽人结果","已抽中"+zj)
'''
def chosiename(e):
    try:
        # 获取输入值并转换为整数
        times = int(entry.get())
        if times <= 0:
            times=1
            messagebox.showinfo("提示","默认抽1次")
        if times > 100:
            messagebox.showerror("安全系统:", "数值过大")
            return
        results = []
        for _ in range(times):
            # 每次重新随机选择组别和人
            selected_group = random.choice(GROUPS)
            selected_person = random.choice(selected_group)
            results.append(selected_person)

        messagebox.showinfo(
            "抽人结果",
            f"共抽选{times}次：\n" + "\n".join(results)
        )
    except ValueError:
        #messagebox.showerror("错误", "请输入有效的正整数")
        times = 1
        results = []
        for _ in range(times):
            # 每次重新随机选择组别和人
            selected_group = random.choice(GROUPS)
            selected_person = random.choice(selected_group)
            results.append(selected_person)

        messagebox.showinfo(
            "抽人结果",
            f"共抽选{times}次：\n" + "\n".join(results)
        )

btn01.bind("<Button-1>",chosiename)#按键绑定

#关于按钮
btn02 = Button(root)
btn02["text"] = "关于"
btn02.pack()
def about_info(a):
    messagebox.showinfo("关于","conding by HYJ   编码:UTF-8 V3.3(专和147对着干)")

btn02.bind("<Button-1>",about_info)#按键绑定

root.mainloop()
