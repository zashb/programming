import numpy as np
import pandas as pd


class Solution:
    def __init__(self):
        self.seed = 5
        self.moviesDF = pd.DataFrame()
        self.ratingsDF = pd.DataFrame()
        self.usersDF = pd.DataFrame()
        self.mergedDF = pd.DataFrame()

    def main(self):
        # load data
        self.moviesDF = self.loadData("movies.dat")
        self.ratingsDF = self.loadData("ratings.dat")
        self.usersDF = self.loadData("users.dat")
        # clean and merge dfs
        self.mergedDF = self.cleanAndMerge([self.moviesDF, self.ratingsDF, self.usersDF])

    def loadData(self, fileName):
        dir = r"C:\Users\sg0222350\My Stuff\learn\python\conferences\pycon2015_tutorial322\data\ml-1m\\"
        colnamesDict = {"users.dat": ['user_id', 'gender', 'age', 'occupation', 'zip'],
                        "ratings.dat": ['user_id', 'movie_id', 'rating', 'timestamp'],
                        "movies.dat": ['movie_id', 'title', 'genres']}
        df = pd.read_table(dir + fileName, sep="::", header=None, names=colnamesDict[fileName], engine="python")
        return df

    def describeDF(self, df):
        print("------------------------------------------")
        print("HEAD : \n", df.head())
        print("SHAPE : \n", df.shape)
        print("DTYPE COUNTS : \n", df.get_dtype_counts())
        print("DTYPES : \n", df.dtypes)

    def cleanAndMerge(self, dfList):
        cleanedDFList = self.cleanDF(dfList)
        m, r, u = cleanedDFList
        mergedDF = pd.merge(pd.merge(r, u), m)
        return mergedDF

    def cleanDF(self, dfList):
        cleanedDFList = []
        for df in dfList:
            for col in df.columns:
                col = col.strip()
                if df[col].dtypes == "object":
                    df[col] = df[col].str.strip()
            cleanedDFList.append(df)
        return cleanedDFList

    def trainTestSplit(self,df):
        df2 = df.copy()
        # random subset of 10000
        df2 = df2.ix[np.random.choice(df2,size=10000,replace=False)]
        # atleast 2 ratings per user in the subset
        userIdsMoreThan1 = df2["user_id"].value_counts(sort=False)>1
        userIdsMoreThan1 = userIdsMoreThan1[userIdsMoreThan1].index
        df2 = df2.select(lambda x: df2.loc[x,"user_id"] in userIdsMoreThan1)
        assert np.all(df2["user_id"].value_counts()>1)



if __name__ == "__main__":
    s = Solution()
    s.main()
    # for i in [s.moviesDF,s.ratingsDF,s.usersDF]:
    #     s.describeDF(i)
    s.describeDF(s.mergedDF)
