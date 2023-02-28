#! /usr/bin/Rscript

f<-file("stdin")
open(f)
record<-c()
while(length(line<-readLines(f,n=1))>0){
  #write(line,stderr())
  record<-c(record,line)  
}
colnames<-gsub('^.|.$', '', record[length(record)])
colnames<-gsub('[^,a-zA-Z0-9 %.\\s]', '', colnames)
print(colnames)
print(as.list(strsplit(colnames,split=",")[[1]]))

numbers<-record[1:length(record)-1]
numbers_<-c()
for (j in numbers){
  numbers_<-c(numbers_,gsub('^.|.$', '', j))
}
rm(numbers)
#print(numbers_)


numbers<-data.frame()
count<-1
for (n in numbers_){
  Quantity<-as.list(strsplit(n,split=",")[[1]])
  #print(length(N))
  Quantity<-as.numeric(Quantity)
  Product<-as.list(strsplit(colnames,split=",")[[1]])
  Attempt<-rep(count,length(Quantity))
  count<-count+1
  mini<-data.frame(cbind(Attempt,Product,Quantity))
  mini[]<-lapply(mini,unlist)
  #print(mini)
  numbers<-rbind(numbers,mini)
}

# print(numbers)

library(ggplot2)
library(plotly)
library(thematic)
thematic::thematic_on(bg = "#FFF8EE", fg = "black", accent = "#005B4B", font = "Yu Gothic")
print(typeof(numbers$Quantity))

pp<-ggplot(numbers,aes( y = Quantity, x = Product, fill = Product))+
  geom_col(position = "identity",aes(frame = Attempt))+theme(
    panel.background = element_rect(
      fill = "#FCF2E3", 
      colour = "black",
      linewidth = 1.3, linetype = "solid"
    )
  )

ff<-ggplotly(pp) %>%
  animation_opts(frame = 100,transition = 90,redraw=TRUE, mode = "next", easing = "elastic-in")

htmlwidgets::saveWidget(as_widget(ff), "./time.html", selfcontained = TRUE)


print("Done!")
