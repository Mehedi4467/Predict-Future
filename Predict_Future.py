import pandas
# import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


m="yes"
while m=="yes":

    print("1.Predict Bangladesh Population")
    print("2.Predict Facebook User")

    n = int(input("Enter Number: "))


    if n==1:
        yr=int(input("Enter Year : "))
        data = pandas.read_csv('population.csv')
        model = LinearRegression()
        model.fit(data[['year']], data[['population']])
        result=model.predict([[yr]])
        print("the population will be ",result,"in",yr)
    elif n==2:
        yr = int(input("Enter Year : "))
        data = pandas.read_csv('fbuser.csv')
        model = LinearRegression()
        model.fit(data[['year']], data[['users']])
        result = model.predict([[yr]])
        print(result)
    print("==================")
    print("0.Exist")
    print("Yes.Continue")
    m =(input("Yes/0 : "))
# plt.scatter(data["year"],data["population"])
# plt.show()