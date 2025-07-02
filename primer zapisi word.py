from docxtpl import DocxTemplate

result = {
    'node_name': 'Шкаф №1',
    'max_temp': 95.2,
    'status': 'Отклонение обнаружено',
    'coordinates': (120, 80),
    'avg_temp': 60.4
}

context = {
    'Имя_узла': result['node_name'],
    'Макс_темп': f"{result['max_temp']} °C",
    'Заключение': result['status'],
    'Сред_темп': f"{result['avg_temp']} °C",
    'Координаты': f"{result['coordinates'][0]}, {result['coordinates'][1]}"
}

doc = DocxTemplate("шаблон.docx")
doc.render(context)
doc.save("отчет.docx")