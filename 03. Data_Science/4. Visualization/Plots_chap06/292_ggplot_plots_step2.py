#py -m pip install ggplot
from ggplot import *

print(meat.head())

plt2 = ggplot(aes(x='date', y='beef'), data=meat) +\
 		geom_line(color='purple', size=1.5, alpha=0.75) + \
        xlab("Year") + ylab("Head of Cattle Slaughtered") +\
 		ggtitle("Beef Consumption Over Time")


print(plt2)
