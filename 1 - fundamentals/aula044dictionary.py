movies_dic = {'avatar':2009, 'titanic':1997, 'starwars': 2015,
              'harry-potter': 2002, 'brasileirinhas':2012};

movies_dic.update({'frozi':2013})

movies_dic.setdefault('ironman', 2015);

movies_dic.pop('frozi')
print(movies_dic)