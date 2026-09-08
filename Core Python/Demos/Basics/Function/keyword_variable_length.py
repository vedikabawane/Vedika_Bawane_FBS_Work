def emp(**data):
    for key, val in data.items():
        print(key, ':', val)

emp(id=101,name='ABC',salary=20000,dept='IT')