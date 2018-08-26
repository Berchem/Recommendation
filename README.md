# Recommender
## Usage
***recommendation_system*.*Recomemder(*dataset*)***

```
from recommendation_system import Recommender

# given a dataset
dataset = [['itemC', 'itemB', 'itemE'],
           ['itemE', 'itemG','itemA','itemB', 'itemD'，...],
           ...]

# new a Recommender object        
rs = Recommender(dataset)

# recommend user 0 5 items accroding to the most popular
popular = rs.popular(dataset[0], n=5)

# recommend user 0 5 items accroding to the user-based CF
user_based = rs.user_based(0)[:5]

# recommend user 0 some items accroding to the item-based CF
item_based = rs.item_based(0)
```

## Parameter
dataset:
> list of list

## Attributes
dataset

unique

usr_matrix

item_matrix

## Methods

popular(data)

user_based(subset, include_current_items=False)

item_based(subset, include_current_items=False)

most_similar_set_to(subset)

most_similar_item_to(subset)