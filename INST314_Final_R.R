library("readxl")
data1 <- read_excel("C:\\Users\\jakew\\Documents\\INST314\\INST314_Final_dataset.xlsx", sheet="Sorted by National Estimate")
data2 <- read_excel("C:\\Users\\jakew\\Documents\\INST314\\INST314_Final_dataset.xlsx", sheet="Sorted by Gender")
data3 <- read_excel("C:\\Users\\jakew\\Documents\\INST314\\INST314_Final_dataset.xlsx", sheet="Sorted by Education")
data4 <- read_excel("C:\\Users\\jakew\\Documents\\INST314\\INST314_Final_dataset.xlsx", sheet="Sorted by Age")

summary(data1)
summary(data2)
summary(data3)
summary(data4)

sd(data1$Value)
sd(data2$Value)
sd(data3$Value)
sd(data4$Value)

plot(data1$`National Value`)
hist(data1$`National Value`)
plot(density(data1$`National Value`))
qqnorm(data1$`National Value`)
qqline(data1$`National Value`)

plot(data2$`Avg Sex`)
hist(data2$`Avg Sex`)
plot(density(data2$`Avg Sex`))
qqnorm(data2$`Avg Sex`)
qqline(data2$`Avg Sex`)

plot(data3$`Avg Edu`)
hist(data3$`Avg Edu`)
plot(density(data3$`Avg Edu`))
qqnorm(data3$`Avg Edu`)
qqline(data3$`Avg Edu`)

plot(data4$Value)
hist(data4$Value)
plot(density(data4$Value))
qqnorm(data4$Value)
qqline(data4$Value)

shapiro.test(data1$`National Value`)
shapiro.test(data2$`Avg Sex`)
shapiro.test(data3$`Avg Edu`)
shapiro.test(data4$`Avg Age`)

model0 <- lm(data1$`Time Period` ~ data1$Value)
plot(model0)

model1 <- lm(data1$`National Value` ~ data2$`Avg Sex`+data3$`Avg Edu`+data4$`Avg Age`)
plot(model1)
library(car)
data5 <- read_excel("C:\\Users\\jakew\\Documents\\INST314\\INST314_Final_dataset.xlsx", sheet="final")
scatterplotMatrix(data5[,2:4],  diagonal = TRUE, smooth = TRUE)

var.test(data1$`National Value`, data2$`Avg Sex`)
var.test(data1$`National Value`, data3$`Avg Edu`)
var.test(data1$`National Value`, data4$`Avg Age`)

t.test(data1$`National Value`, data2$`Avg Sex`)
t.test(data1$`National Value`, data3$`Avg Edu`)
t.test(data1$`National Value`, data4$`Avg Age`)

chisq.test(data2$`Value Male`, data1$`National Value`)
chisq.test(data2$`Value Female`, data1$`National Value`)

aov1 <- aov(data1$`National Value` ~ data3$`No HS` +data3$HS + data3$Assoc + data3$Bach)
aov2 <- aov(data1$`National Value` ~ data4$`18 - 29` + data4$`30 - 39` + data4$`40 - 49` + data4$`50 - 59` + data4$`60 - 69` + data4$`70 - 79` + data4$`80+`)
summary(aov1)
summary(aov2) 

install.packages("multcompView")
library(multcompView)
TukeyHSD(aov1)
TukeyHSD(aov2)

n<-length(data2$Value)
B<-10000
Testobs <- abs(mean(data2$Value[data2$Subgroup=="Male"]) - mean(data2$Value[data2$Subgroup=="Female"]))
Testobs
Bootviews <- matrix(sample(data2$Value,size=n*B, replace=TRUE),nrow=n,ncol=B)

Boot.test.stat <-rep(0,B)
for (i in 1:B){
  Boot.test.stat[i] <- abs( mean(Bootviews[1:100,i]) - mean(Bootviews[101:200,i]) )
}

Boot.test.stat >= Testobs
mean( Boot.test.stat >= Testobs)

Bootmeans <-rep(0,B)
for (i in 1:B){
  Bootmeans[i] <- mean(Bootviews[,i])
}
hist(Bootmeans)
ci<-c(mean(Bootmeans)-1.96*sd(Bootmeans),mean(Bootmeans),mean(Bootmeans)+sd(Bootmeans)*1.96)
cifreq<-c(quantile(Bootmeans,probs=0.025),quantile(Bootmeans,probs=.975))

model10 <- lm(data1$`National Value` ~ data1$`Time Period`)
plot(model10)
summary(model10)

