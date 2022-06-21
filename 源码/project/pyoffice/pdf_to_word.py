# author by Michealzou@126.com
# 2022/6/21 10:06
from pdf2docx import Converter
import PySimpleGUI as sg


# 定义函数，file_path是待转换的pdf路径
def pdf2word(file_path):
    # 取出pdf文件并按.截取出第0号元素，也就是.pdf前面的元素
    file_name = file_path.split('.')[0]
    # 保持pdf同名，并定义后缀名.docx
    docx_file = f'{file_name}.docx'
    # pdf转word
    p2w = Converter(file_path)
    # start=0,end=None表示从第一页转到最后一页，可按需要设置转换的起始页
    p2w.convert(docx_file, start=0, end=None)
    p2w.close()
    return docx_file


# 定义main函数，设置gui窗口
def main():
    # 选择主题
    sg.theme('BlueMono')

    # 设置窗口页布局
    layout = [
        # Text设置文本内容和格式
        [sg.Text('PDF转word', font=("微软雅黑", 12)),
        sg.Text('', key='filename', size=(50, 1), font=("微软雅黑", 10), text_color='blue')],
        # Output设置窗口输出的地方
        [sg.Output(size=(80, 10), font=("微软雅黑", 10))],
        # FileBrowse设置浏览器，key是指定键名称，target是选定的文件夹名
        [sg.FileBrowse('选择文件', key='file', target='filename'),
         sg.Button('开始转换'), sg.Button('退出')]
        ]

    # 创建窗口
    window = sg.Window('python', layout, font=("微软雅黑", 15), default_element_size=(50, 1))

    # 打开窗口，保持循环
    while True:
        # event为事件，如点击按钮，选择文件
        # values包含输入的值，如文件名信息
        event, values = window.read()
        if event in (None, '退出'):
            break
        if event == '开始转换':
            if values['file'] and values['file'].split('.')[1] == 'pdf':
                file_path = pdf2word(values['file'])
                print('\n' + '转换成功' + '^_^' + '\n')
                print('word文件位置',file_path)
            else:
                print('未选取文件或文件不是pdf格式，请重新选择')

    window.close()


main()
