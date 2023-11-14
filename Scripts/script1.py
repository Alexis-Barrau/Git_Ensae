x = pd.DataFrame(
    {'prix': np.random.uniform(size = 5),
     'quantite': [i+1 for i in range(5)]
    },
    index = ['yaourt','pates','riz','tomates','gateaux']
)
x