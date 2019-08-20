from admin import AlphaResource

alpha_resource = AlphaResource()
dataset = alpha_resource.export()
print(dataset.csv)