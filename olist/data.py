import os
import pandas as pd

class Olist:

    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrame loaded from csv files
        """
        # Hints: Build csv_path as "absolute path" in order to call this method from anywhere.
        # Do not hardcode your path as it only works on your machine ('Users/username/code...')
        # Use __file__ as absolute path anchor independant of your computer
        # Make extensive use of `import ipdb; ipdb.set_trace()` to investigate what `__file__` variable is really
        # Use os.path library to construct path independent of Unix vs. Windows specificities
        csv_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'data', 'csv')
        # Builds the list of keys for data DICT
        file_names = [f for f in os.listdir(csv_path) if not f.startswith('.')]
        key_names = []
        for file_name in file_names:
            key_name = file_name.replace('olist', "")
            key_name = key_name.replace('.csv', "")
            key_name = key_name.replace('dataset', "")
            key_name = key_name.strip('_')
            key_names.append(key_name)
        key_names
        # Builds the list of values for data DICT
        value_names = []
        for file_name in file_names:
            dataframe = pd.read_csv(os.path.join(csv_path, f'{file_name}'))
            value_names.append(dataframe)
        # Builds data as DICT using key_values and name_values
        data = dict(zip(key_names, value_names))
        return data
        
    def get_matching_table(self):
        """
        01-01 > This function returns a matching table between
        columns [ "order_id", "review_id", "customer_id", "product_id", "seller_id"]
        """
        data = Olist.get_data(self)
        # Extracts columns of interest from dataframes
        orders = data['orders'][['order_id', 'customer_id']]
        order_reviews = data['order_reviews'][['review_id', 'order_id']]
        order_items = data['order_items'][['order_id', 'product_id', 'seller_id']]
        # Merges sub-dataframes together into matching_table
        matching_table = orders.merge(order_reviews, on='order_id', how='outer')
        matching_table = matching_table.merge(order_items, on='order_id', how='outer')
        
        return matching_table

    def ping(self):
        """
        You call ping I print pong.
        """
        print('pong')
