#py -m pip install ggplot
from ggplot import *
print(mtcars.head())
plt1 = ggplot(aes(x='mpg'), data=mtcars) +\
 		geom_histogram(fill='darkblue', binwidth=2) +\
		xlim(10, 35) + ylim(0, 10) +\
		xlab("MPG") + ylab("Frequency") +\
		ggtitle("Histogram of MPG")
print(plt1)

