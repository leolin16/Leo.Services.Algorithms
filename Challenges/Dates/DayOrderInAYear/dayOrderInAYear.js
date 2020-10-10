function dayOrderInAYear(sData){
    var sY = sData.substring(0,4);
    var sM = sData.substring(4,6);
    var sD = sData.substring(6);
    var newData = new Date(sY,(sM-1),sD,0,0,0);
    console.log(newData);
    var oldData = new Date(sY,0,1,0,0,0,0);
    var timer = (newData.getTime() - oldData.getTime())/(1000*86400);
    return timer + 1;
}

function monthName(month) {
    var monthArr = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]; 
    return monthArr[Number(month) - 1]
}

module.exports = {dayOrderInAYear,monthName};
