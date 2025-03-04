from spire.pdf import PdfDocument, FileFormat

# 创建PdfDocument类的实例
pdf = PdfDocument()

# 加载PDF文件
pdf.LoadFromFile("input/(11.4.3)--劳动合同与就业协议书.pdf")

# 将PDF文件保存为PowerPoint文件
pdf.SaveToFile("output/(11.4.3)--劳动合同与就业协议书.pptx", FileFormat.PPTX)
pdf.Close()