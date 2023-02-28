import plotly.express as px
import pandas as pd

dataitems = []
# quants = []
while True:
    try:dataitems.append(input())
    except:break

quants = (dataitems[-1])[1:-1].split(",")
dataitems = dataitems[:-1]

def AGAL(str):
    listo = str[1:-1].split(",")
    return [int(x) for x in listo]


pd.options.plotting.backend = "plotly"
df = pd.DataFrame(dict(Items = quants, Quantity = AGAL(dataitems[-1]) ))
# print(df)
# fig = df.plot.bar()
# fig.show()


#Final result : simple plot
fig = px.bar(df,x = "Items", y = "Quantity")
fig.show()


####ANIMATED PLOT
# data = []
# count = 1
# maxi = 0
# for n in dataitems:
#     data.append(AGAL(n) + [count])
#     maxi = max(max(AGAL(n)),maxi)
#     count+=1

# dd = pd.DataFrame( data,columns = quants+["Attempts"])

# dd = pd.melt(dd,id_vars=["Attempts"],var_name="Product",value_name="Quantity")


# fig2 = px.bar(dd,y="Quantity",x = "Product",animation_frame="Attempts", color = "Product",title="Timeline of obtained roulette products", template = "plotly_dark",range_y=[0,maxi])

# fig2.show()
