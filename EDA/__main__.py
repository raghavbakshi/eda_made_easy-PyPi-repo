import numpy as np

class eda_made_easy:
    
    """
        This class is created to ease EDA. User just need to pass the dataset and select the function and all the this will be done automatically.
        Functions available under this class are:
            impute_Nan : This function is going to fill all the NaN values in the dataset with method given by the user
            impute_outlier : This function will be used to replace all the ouliers with the median value
            scale_data : This funnction is going to down scale your data.
        
        """
    
    def __init__(self,data):
        self.data = data
        
    def impute_NaN(self,method):
        self.method = method
        
        
        '''
            This function is going to fill all the NaN values in the dataset with method given by the user
            method : {mean, median, mode}
            
            '''
        try:
            for i in self.data.columns:
                if self.data[i].dtypes != "O":
                    if self.method == 'mean':
                        print(self.data[i].mean())
                        self.data[i] = self.data[i].fillna(self.data[i].mean())
                    elif self.method == 'mode':
                        self.data[i] = self.data[i].fillna(self.data[i].mode())
                    elif self.method == 'median':
                        self.data[i] = self.data[i].fillna(self.data[i].median())
                else:
                    self.data[i] = self.data[i].fillna(self.data[i].mode()[0].split()[0])
        except Exception as e:
            return e
        
    def impute_oulier(self):
        
        '''
        This function will be used to replace all the ouliers with the median value
            '''
        
        try:
            for i in self.data.columns:
                if self.data[i].dtypes != "O":
                    Q1 = self.data[i].quantile(0.25)
                    Q3 = self.data[i].quantile(0.75)
                    #calculate IQR
                    IQR = Q3 - Q1
                    self.data[i].loc[((self.data[i] < (Q1 - 1.5 * IQR)) |(self.data[i] > (Q3 + 1.5 * IQR)))] = np.nan
                    self.data[i] = self.data[i].fillna(self.data[i].median())

        except Exception as e:
            return e
        
    def scale_data(self):
        
        '''
            This funnction is going to down scale your data.
            '''
        try:
            for i in self.data.columns:
                if self.data[i].dtypes != "O":
                    s = self.data[i].std()
                    u = self.data[i].mean()
                    lst = []
                    print(i,s)
                    if s == 0:
                        s=1
                        for j in df[i]:
                            print(u,s)
                            s = 1
                            var = (j-u)/s
                            lst.append(var)
                    else:
                        for j in df[i]:

                            var = (j-u)/s
                            lst.append(var)

                    self.data[i] = lst
                    

        except Exception as e:
            return e
        
if __name__ == '__main__':
    eda_made_easy