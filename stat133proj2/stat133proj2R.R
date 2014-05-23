pricedata=read.csv("/Users/brandonflannery/src1/stat133/stat133proj2/stat133projdataprice.csv", header=TRUE, sep=",")
data=read.table("/Users/brandonflannery/src1/stat133/stat133proj2/stat133proj2data.csv", header=TRUE, sep=",")
data$Day=sub("/", ".", data$Day)
data$Day= sub('/', '.', data$Day)
data$Day=paste("X", data$Day, sep="")
Day=as.name(data$Day)
#to access dataprice use "pricedata[,data$Day[day]]"
Daydict=vector(mode='list', length=length(data$Day))
names(Daydict)=data$Day
Daydict[1:length(data$Day)]= c(1:length(data$Day))

findprices=function(day){
  if(any(names(pricedata)== day)){
  index=as.integer(Daydict[day])
  return(pricedata[,data$Day[index]])
  }
  else{return(NA)}
  
}

timetomins=function(timeofspeech){
  x=sub(":", " ", timeofspeech)
  a=strsplit(x, " ")
  a=unlist(a)
  b=as.numeric(a[1])
  c=as.numeric(a[2])
  if (b<8){
    b=b+12
  }
  return(b*60+c)
  
}

timetointervalsp= function(time){
  mins=timetomins(time)
  if(mins < (390+60)){
    return(c(406, 406-180))
  }
  if(mins > 780-120){
    return(c(2+180, 2))
  }
  else{
    return(c(406-(mins-390-60), (406-(mins-390+120))))
  }
}

timetointervalvix= function(time){
  mins=timetomins(time)
  if(mins < (390+60)){
    return(c(1219, 1219-180))
  }
  if(mins > 780-120){
    return(c(2+180, 2))
  }
  else{
    return(c(1219-(mins-390-60), (1219-(mins-390+120))))
  }
}

percentchangesp=function(day, time){
  x=timetointervalsp(time)
  prices=findprices(day)
  first=x[1]
  last=x[2]
  pfirst=as.numeric(as.character(prices[first]))
  plast=as.numeric(as.character(prices[last]))
  return((plast-pfirst)/pfirst)
}

percentchangevix=function(day, time){
  x=timetointervalvix(time)
  prices=findprices(day)
  first=x[1]
  last=x[2]
  pfirst=as.numeric(as.character(prices[first]))
  plast=as.numeric(as.character(prices[last]))
  return((plast-pfirst)/pfirst)
}

data$ChangeVix= mapply(percentchangevix, data$Day, data$Time)
data$ChangeSP= mapply(percentchangesp, data$Day, data$Time)

