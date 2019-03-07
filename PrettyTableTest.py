import prettytable as pt

# 按行添加数据Prettytable数据库数据打印等等
tb = pt.PrettyTable()
tb.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
tb.add_row(["Adelaide", 1295, 1158259, 600.5])
tb.add_row(["Brisbane", 5905, 1857594, 1146.4])
tb.add_row(["Darwin", 112, 120900, 1714.7])
tb.add_row(["Hobart", 1357, 205556, 619.5])
tb.add_column('index', [1, 2, 3, 4])

# 设置输出风格
# tb.set_style(pt.PLAIN_COLUMNS)
print(tb)
